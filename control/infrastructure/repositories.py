from control.domain.entities import ActuationCommand
from control.infrastructure.models import ActuationCommandModel

class ActuationRepository:
    @staticmethod
    def save(cmd: ActuationCommand) -> ActuationCommand:
        rec = ActuationCommandModel.create(
            device_id  = cmd.device_id,
            action     = cmd.action,
            created_at = cmd.created_at
        )
        return ActuationCommand(rec.device_id, rec.action, rec.created_at, rec.id)
