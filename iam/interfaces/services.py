from fastapi import FastAPI, APIRouter, Request, HTTPException, Depends
from iam.application.services import AuthApplicationService

# Initialize FastAPI app and router
app = FastAPI()
router = APIRouter(prefix="/iam", tags=["IAM"])

# Initialize dependencies
auth_service = AuthApplicationService()

def _extract_body(request: Request) -> dict:
    """Helper to safely extract JSON body from the request."""
    try:
        return request.json()  # not awaited here; used in sync context below
    except Exception:
        return {}

async def authenticate_request(request: Request):
    """Dependency to authenticate incoming HTTP requests."""
    try:
        body = await request.json()
    except Exception:
        body = {}

    device_id = body.get("device_id")
    api_key = request.headers.get("X-API-Key")

    if not device_id or not api_key:
        raise HTTPException(
            status_code=401,
            detail={"error": "Missing device_id or X-API-Key"}
        )

    if not auth_service.authenticate(device_id, api_key):
        raise HTTPException(
            status_code=401,
            detail={"error": "Invalid device_id or API key"}
        )
