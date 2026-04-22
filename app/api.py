from fastapi import FastAPI # Importing FastAPI (Class),Anything starts with first letter is an class.
from routers import metrics, aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0",  #symentic versioning
    doc_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")    #the @app is called as decorator / will return mess
def hello():
    """
    This is a Hello API , just for testing
    """
    return {"message":"Hello Dosto, This is DevOps Utilites API"} #api returns json & keys

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")