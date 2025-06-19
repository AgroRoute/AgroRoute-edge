# pip install paho-mqtt
import paho.mqtt.client as mqtt
from control.domain.entities import ActuationCommand
class ActuatorController:
    def __init__(self,
                 broker: str = "38.25.66.132",
                 port: int  = 1883):
        self.client = mqtt.Client()
        self.client.connect(broker, port)
        self.client.loop_start()

    def execute(self, cmd: ActuationCommand):
        parts = cmd.action.split("_")
        actuator = parts[-1]
        state    = "ON" if parts[1] == "on" else "OFF"

        topic = f"agroroute/{cmd.device_id}/{actuator}"
        self.client.publish(topic, state)
        print(f"[MQTT] {topic} → {state}")
