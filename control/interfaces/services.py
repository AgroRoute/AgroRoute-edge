from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from control.application.services import ActuationApplicationService
from iam.interfaces.services import authenticate_request

router = APIRouter(prefix="/api/v1/control", tags=["Control"])
act_app = ActuationApplicationService()

@router.post("/execute", dependencies=[Depends(authenticate_request)])
async def trigger_actuation(request: Request):
    data = await request.json()
    mid  = data.get("monitoring_id")
    if mid is None:
        raise HTTPException(400, "Missing monitoring_id")
    api_key = request.headers.get("X-API-Key")

    try:
        cmds = act_app.execute_actuation(int(mid), api_key)
        return JSONResponse(status_code=201, content={"commands": cmds})
    except ValueError as e:
        raise HTTPException(401, str(e))
