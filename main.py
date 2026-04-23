# Application Entry Point
from app.api import app
import uvicorn  

if __name__ == "__main__":
    # ASGI Web Server  # loadbalancer, scalable
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
