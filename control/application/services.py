from monitoring.infrastructure.repositories import MonitoringRecordModel
from iam.infrastructure.repositories import DeviceRepository
from control.domain.services import ActuationService
from control.infrastructure.repositories import ActuationRepository
from control.infrastructure.actuator_controller import ActuatorController

class ActuationApplicationService:

    def __init__(self):
        self.device_repo   = DeviceRepository()
        self.act_service   = ActuationService()
        self.act_repo      = ActuationRepository()
        self.actuator_ctrl = ActuatorController()

    def execute_actuation(self, monitoring_id: int, api_key: str) -> list[dict]:
        rec = MonitoringRecordModel.get_by_id(monitoring_id)

        if not self.device_repo.find_by_id_and_api_key(rec.device_id, api_key):
            raise ValueError("Device not authorized")

        commands = self.act_service.evaluate(rec)

        results = []
        for cmd in commands:
            saved = self.act_repo.save(cmd)
            self.actuator_ctrl.execute(saved)
            results.append({
                "id":         saved.id,
                "device_id":  saved.device_id,
                "action":     saved.action,
                "created_at": saved.created_at.isoformat() + "Z"
            })
        return results
