"""
    Domain entities for the IAM bounded context.
"""

class Device:
    """
        Represent a device entity in the IAM context.

        Attributes:
            device_id (str): Unique identifier for the device.
            api_key (str): API key for device authentication.
            created_at (datetime): Timestamp when the device was created.
    """
    def __init__(self, device_id: str, api_key: str, created_at):
        self.device_id = device_id
        self.api_key = api_key
        self.created_at = created_at
