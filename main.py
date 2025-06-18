import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from iam.interfaces.services import router as iam_router
from monitoring.interfaces.services import router as monitoring_router
from shared.infrastructure.database import init_db
from control.interfaces.services import router as control_router
import iam.application.services

CLOUD_ENDPOINT = os.getenv("CLOUD_MONITORING_ENDPOINT")

# Initialize FastAPI app
app = FastAPI()

# Include IAM and Monitoring routers
app.include_router(iam_router)
app.include_router(monitoring_router)

app.include_router(control_router)

@app.on_event("startup")
async def startup_event():
    """Initialize the database and create a test device."""
    init_db()
    auth_service = iam.application.services.AuthApplicationService()
    auth_service.get_or_create_test_device()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

