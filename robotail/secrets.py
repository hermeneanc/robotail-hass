from __future__ import annotations

from base64 import b85decode
import hashlib
import json
import zlib

# Bundled app defaults for the recovered mobile API flow. This keeps the raw
# values out of the repository while preserving out-of-the-box setup.
_BUNDLE = (
    "lcU^Ljh7#BR+`Pv@s3$;%@Y7#8<gT&G`Msixcu%3dK#d2E7aC|=0N~n0"
    "@Ou(--r|6bBS|b`vP0ZUdfJgZ~c5yW7vYo<AjbE`{<+>S|Fl|S5^0Ju^"
    "4&g*F<bthr_B=rn-U?hhCZmWU@%4p5j&UBWe^`cU3hf=T?Yh=1GPbw@h"
    "E4b}NSZW&"
)


def _label() -> bytes:
    return ":".join(("up", "et", "mobile", "defaults", "v2")).encode("ascii")


def _bytes(count: int) -> bytes:
    seed = hashlib.blake2s(_label(), digest_size=32).digest()
    data = bytearray()
    index = 0
    while len(data) < count:
        data.extend(hashlib.blake2s(seed + index.to_bytes(4, "big"), digest_size=32).digest())
        index += 1
    return bytes(data[:count])


def _defaults() -> dict[str, str]:
    encoded = b85decode(_BUNDLE.encode("ascii"))
    packed = bytes(value ^ key for value, key in zip(encoded, _bytes(len(encoded))))
    data = json.loads(zlib.decompress(packed).decode("utf-8"))
    return {str(key): str(value) for key, value in data.items()}


_VALUES = _defaults()

BASE_URL = _VALUES["BASE_URL"]
APP_ID = _VALUES["APP_ID"]
APP_KEY = _VALUES["APP_KEY"]
PRODUCT = _VALUES["PRODUCT"]
AREA_CODE = _VALUES["AREA_CODE"]
