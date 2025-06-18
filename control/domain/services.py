from datetime import datetime
from monitoring.domain.entities import MonitoringRecord
from control.domain.entities import ActuationCommand

class ActuationService:
    """
    Lógica de negocio: decide qué acciones (on/off) tomar según las lecturas.
    """

    def __init__(self,
                 temp_high: float = 30.0,
                 temp_low: float  = 15.0,
                 hum_low: float   = 40.0):
        self.temp_high = temp_high
        self.temp_low  = temp_low
        self.hum_low   = hum_low

    def evaluate(self, record: MonitoringRecord) -> list[ActuationCommand]:
        now = datetime.utcnow()
        cmds: list[ActuationCommand] = []

        # --- Fan control (high temp) ---
        if record.temperature > self.temp_high:
            cmds.append(ActuationCommand(record.device_id, "turn_on_fan", now))
        elif record.temperature <= self.temp_high:
            cmds.append(ActuationCommand(record.device_id, "turn_off_fan", now))

        # --- Heater control (low temp) ---
        if record.temperature < self.temp_low:
            cmds.append(ActuationCommand(record.device_id, "turn_on_heater", now))
        elif record.temperature >= self.temp_low:
            cmds.append(ActuationCommand(record.device_id, "turn_off_heater", now))

        # --- Humidifier control (low humidity) ---
        if record.humidity < self.hum_low:
            cmds.append(ActuationCommand(record.device_id, "turn_on_humidifier", now))
        elif record.humidity >= self.hum_low:
            cmds.append(ActuationCommand(record.device_id, "turn_off_humidifier", now))

        return cmds
