"""
    Database initialization for the Agroroute Edge Service.
    Sets up the SQLite database and creates required tables for devices and monitoring records.
"""

from peewee import SqliteDatabase


# Initialize the SQLite database
db = SqliteDatabase('agroroute_edge_service.db')

def init_db() -> None:
    """
        Initialize the database and create tables for Device and MonitoringRecord models.
    """
    db.connect()
    from iam.infrastructure.models import Device
    from monitoring.infrastructure.models import MonitoringRecord
    from control.infrastructure.models import ActuationCommandModel
    db.create_tables([Device, MonitoringRecord, ActuationCommandModel], safe=True)
    db.close()

