from datetime import datetime

class ActuationCommand:
    def __init__(self, device_id: str, action: str, created_at: datetime, id: int = None):
        self.id = id
        self.device_id = device_id
        self.action = action        # e.g. "turn_on_fan", "turn_off_fan", etc.
        self.created_at = created_at
