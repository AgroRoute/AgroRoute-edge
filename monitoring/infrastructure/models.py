"""
    Peewee ORM model for monitoring records.
    Define the MonitoringRecord database table structure for storing monitoring data.
"""
from peewee import Model, AutoField, FloatField, CharField, DateTimeField

from shared.infrastructure.database import db


class MonitoringRecord(Model):
    """
    ORM model for the monitoring_records table.
    Represents a monitoring record entry in the database.
    """
    id = AutoField()
    device_id = CharField()
    temperature = FloatField()
    humidity = FloatField()
    latitude = FloatField()
    longitude = FloatField()
    created_at = DateTimeField()

    class Meta:
        database = db
        table_name = 'monitoring_records'