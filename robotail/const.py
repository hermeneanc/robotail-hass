from __future__ import annotations

from datetime import timedelta

from homeassistant.const import Platform

DOMAIN = "robotail"
DEFAULT_SCAN_INTERVAL = timedelta(minutes=3)

try:
    from .secrets import (
        APP_ID as DEFAULT_APP_ID,
        APP_KEY as DEFAULT_APP_KEY,
        BASE_URL as DEFAULT_BASE_URL,
        PRODUCT as DEFAULT_PRODUCT,
        AREA_CODE as DEFAULT_AREA_CODE,
    )
except ImportError:
    DEFAULT_APP_ID = ""
    DEFAULT_APP_KEY = ""
    DEFAULT_BASE_URL = ""
    DEFAULT_PRODUCT = ""
    DEFAULT_AREA_CODE = "AT"

CONF_APP_KEY = "app_key"
CONF_APP_ID = "app_id"
CONF_DEVICE_ID = "device_id"
CONF_BASE_URL = "base_url"
CONF_PRODUCT = "product"
CONF_AREA_CODE = "area_code"

PLATFORMS = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.NUMBER,
    Platform.SWITCH,
    Platform.TIME,
    Platform.SELECT,
    Platform.BUTTON,
]
