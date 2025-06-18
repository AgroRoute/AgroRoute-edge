"""Domain entities for the Monitoring-Bounded Context."""
from datetime import datetime

class MonitoringRecord:
    """
        Monitoring record interface for handling device data.

        Attributes:
        - device_id (str): Unique identifier for the device.
        - temperature (float): Temperature reading from the device.
        - humidity (float): Humidity reading from the device.
        - latitude (float): Latitude of the device's location.
        - longitude (float): Longitude of the device's location.
        - created_at (datetime): Timestamp of when the data was created.
        - id (int, optional): Unique identifier for the data entry, used for database operations.
    """

    def __init__(self, device_id: str, temperature: float, humidity: float, latitude: float, longitude: float, created_at: datetime, id: int = None):
        self.id = id
        self.device_id = device_id
        self.temperature = temperature
        self.humidity = humidity
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = created_at
