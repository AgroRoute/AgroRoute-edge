"""
Repository for monitoring record persistence.

Handles saving monitoring records to the database using Peewee ORM models.
"""
from monitoring.domain.entities import MonitoringRecord
from monitoring.infrastructure.models import MonitoringRecord as MonitoringRecordModel


class MonitoringRecordRepository:
    """
    Repository for managing MonitoringRecord persistence.
    """
    @staticmethod
    def save(monitoring_record) -> MonitoringRecord:
        """
        Save a MonitoringRecord entity to the database.
        Args:
            monitoring_record (MonitoringRecord): The monitoring record to save.
        Returns:
            MonitoringRecord: The saved monitoring record with assigned ID.
        """
        record = MonitoringRecordModel.create(
            device_id   =   monitoring_record.device_id,
            temperature=monitoring_record.temperature,
            humidity = monitoring_record.humidity,
            latitude = monitoring_record.latitude,
            longitude = monitoring_record.longitude,
            created_at  =   monitoring_record.created_at
        )
        return MonitoringRecord(
            monitoring_record.device_id,
            monitoring_record.temperature,
            monitoring_record.humidity,
            monitoring_record.latitude,
            monitoring_record.longitude,
            monitoring_record.created_at,
            record.id
        )
