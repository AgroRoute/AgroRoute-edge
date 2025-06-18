# monitoring/infrastructure/cloud_client.py
import os
import logging
import requests
from monitoring.domain.entities import MonitoringRecord

class CloudMonitoringClient:
    def __init__(self, endpoint: str = None):
        self.endpoint = endpoint or os.getenv("CLOUD_MONITORING_ENDPOINT")

    def send(self, record: MonitoringRecord) -> None:
        payload = {
            "device_id":  record.device_id,
            "temperature": record.temperature,
            "humidity":    record.humidity,
            "latitude":    record.latitude,
            "longitude":   record.longitude,
            "created_at":  record.created_at.isoformat() + "Z",
        }
        try:
            resp = requests.post(self.endpoint, json=payload, timeout=5)
            resp.raise_for_status()
            logging.info(f"[Cloud] Enviado record {record.id} → status {resp.status_code}")
        except Exception as e:
            logging.error(f"[Cloud] Error enviando record {record.id}: {e}")
