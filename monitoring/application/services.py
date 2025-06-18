"""Application services for the Monitoring-bounded context."""

from monitoring.domain.entities import MonitoringRecord
from monitoring.domain.services import MonitoringRecordService
from monitoring.infrastructure.repositories import MonitoringRecordRepository
from iam.infrastructure.repositories import DeviceRepository
from monitoring.infrastructure.cloud_client import CloudMonitoringClient

class MonitoringRecordApplicationService:
    """Application service for creating monitoring records."""

    def __init__(self):
        """Initialize the MonitoringRecordApplicationService."""
        self.monitoring_record_repository = MonitoringRecordRepository()
        self.monitoring_record_service = MonitoringRecordService()
        self.device_repository = DeviceRepository()
        self.cloud_client = CloudMonitoringClient()

    def create_monitoring_record(self, device_id: str, temperature:float, humidity: float, latitude:float, longitude:float, created_at: str, api_key: str) -> MonitoringRecord:
        """Create a monitoring record after validating the device.

        Args:
            device_id (str): Device identifier.
            temperature (float): Temperature reading.
            humidity (float): Heart rate in beats per minute.
            latitude (float): Latitude of the device's location.
            longitude (float): Longitude of the device's location.
            created_at (str): ISO 8601 timestamp.
            api_key (str): API key for device authentication.

        Returns:
            MonitoringRecord: The created monitoring record.

        Raises:
            ValueError: If the device_id and api_key are invalid.
        """
        # Validate device_id exists in IAM context
        if not self.device_repository.find_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found")
        record = self.monitoring_record_service.create_record(device_id, temperature, humidity, latitude, longitude, created_at)

        saved = self.monitoring_record_repository.save(record)

        try:
            self.cloud_client.send(saved)
        except Exception as e:
            print(f"[Cloud] Error al enviar record {saved.id}: {e}")

        return saved