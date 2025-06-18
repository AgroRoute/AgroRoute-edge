from peewee import Model, AutoField, CharField, DateTimeField
from shared.infrastructure.database import db

class ActuationCommandModel(Model):
    id          = AutoField()
    device_id   = CharField()
    action      = CharField()
    created_at  = DateTimeField()

    class Meta:
        database   = db
        table_name = 'actuation_commands'
