from fastapi import FastAPI, APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

from monitoring.application.services import MonitoringRecordApplicationService
from iam.interfaces.services import authenticate_request


from control.application.services import ActuationApplicationService

app = FastAPI()
router = APIRouter(prefix="/api/v1/monitoring", tags=["Monitoring"])

monitoring_svc = MonitoringRecordApplicationService()
actuation_svc = ActuationApplicationService()

@router.post("/data-records", dependencies=[Depends(authenticate_request)])
async def create_monitoring_record(request: Request):
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(400, "Invalid JSON")

    try:
        device_id  = payload["device_id"]
        temperature= payload["temperature"]
        humidity   = payload["humidity"]
        latitude   = payload.get("latitude")
        longitude  = payload.get("longitude")
        created_at = payload.get("created_at")
        api_key    = request.headers.get("X-API-Key")
    except KeyError as e:
        raise HTTPException(400, f"Missing field {e}")

    try:
        record = monitoring_svc.create_monitoring_record(
            device_id, temperature, humidity, latitude, longitude, created_at, api_key
        )
    except ValueError as e:
        raise HTTPException(401, str(e))

    response = {
        "id": record.id,
        "device_id": record.device_id,
        "temperature": record.temperature,
        "humidity": record.humidity,
        "latitude": record.created_at and record.created_at.isoformat() + "Z",
        "longitude": record.longitude,
        "created_at": record.created_at.isoformat() + "Z"
    }

    try:
        commands = actuation_svc.execute_actuation(record.id, api_key)
        print(f"[CONTROL] Disparados comandos MQTT para record {record.id}: {commands}")
        response["commands"] = commands
    except Exception as e:
        print(f"[CONTROL] Error al disparar actuadores: {e}")

    return JSONResponse(status_code=201, content=response)
