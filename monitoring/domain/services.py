"""
    Domain services for the Monitoring-Bounded Context.
"""
from datetime import datetime, timezone

from dateutil.parser import parse

from monitoring.domain.entities import  MonitoringRecord

class MonitoringRecordService:
    """Service for managing monitoring records."""

    def __init__(self):
        """
            Initializes the MonitoringService.
        """

    @staticmethod
    def create_record(device_id: str, temperature: float, humidity: float, latitude: float, longitude: float, created_at: str | None) -> MonitoringRecord:
        """
            Creates a new MonitoringRecord instance.

            Args:
                device_id (str): Unique identifier for the device.
                temperature (float): Temperature reading from the device.
                humidity (float): Humidity reading from the device.
                latitude (float): Latitude of the device's location.
                longitude (float): Longitude of the device's location.
                created_at (str): Timestamp of when the data was created in ISO 8601 format.

            Returns:
                MonitoringRecord: A new instance of MonitoringRecord.
        """
        try:
            temperature = float(temperature)
            humidity = float(humidity)

            if latitude is None:
                latitude = 0.0
            else:
                latitude = float(latitude)

            if longitude is None:
                longitude = 0.0
            else:
                longitude = float(longitude)


            if not (-40 <= temperature <= 80):
                raise ValueError("Temperature must be between -40 and 80 degrees Celsius.")
            if not (0 <= humidity <= 100):
                raise ValueError("Humidity must be between 0 and 100 percent.")
            if not (-90 <= latitude <= 90):
                raise ValueError("Latitude must be between -90 and 90 degrees.")
            if not (-180 <= longitude <= 180):
                raise ValueError("Longitude must be between -180 and 180 degrees.")
            if created_at:
                parsed_created_at = parse(created_at).astimezone(timezone.utc)
            else:
                parsed_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid input data: {e}")

        return MonitoringRecord(device_id, temperature, humidity, latitude, longitude, parsed_created_at)

