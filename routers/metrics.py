from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics

router = APIRouter()
#import pdb;pdb.set_trace()  #use for debugging.  
@router.get("/metrics",status_code=200)
def get_metrics():

    try:
        metrics = get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
