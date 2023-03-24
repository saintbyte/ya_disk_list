import os
class Settings:
    @staticmethod
    def get_settings() -> dict:
        """

        :rtype: object
        """
        return {
            "YANDEX_CLIENT_ID": os.environ.get("YANDEX_CLIENT_ID", False),
            "DEVICE_ID": os.environ.get("DEVICE_ID", False),
            "DEVICE_NAME": os.environ.get("DEVICE_NAME", False),
            "ITEMS_LIMIT": int(os.environ.get("ITEMS_LIMIT", 100)),
            "OUTPUT_CSV_FILENAME": os.environ.get("OUTPUT_CSV_FILENAME", "1.csv"),
            "YA_DISK_ROOT": os.environ.get("YA_DISK_ROOT", "disk:/"),
            "DEBUG": os.environ.get("DEBUG", "False").lower() in ("true", "1", "t"),
        }
