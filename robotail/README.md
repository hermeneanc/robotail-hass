# ROBOTAIL / Airrobo Cat Litter Box for Home Assistant

Custom Home Assistant integration for the **Robotail** smart cat litter box (also
rebranded as Airrobo). It connects directly to the Robotail cloud backend,
polls the litter box over the Airrobo IM/MQTT channels, and exposes sensors,
switches, numbers, selects, buttons, and time controls for the box and your cats.

**Version:** 1.0.0

---

## About this integration

This integration is based on the [UPet HACS integration](https://github.com/CrazzyBerg/upet-hass)
and shares its Airrobo backend and the same MQTT data model. The two products
are very similar under the hood — which is exactly what makes the differences
matter.

The stock UBPet integration could **not** be used for Robotail as-is:

- UBPet ships with a fixed app namespace that targets the Airrobo app
  (`appId 970010026`) and an empty region code. The Robotail box lives in a
  different namespace (`appId 970010096`) and refuses to authenticate without
  an ISO country code (`areaCode`, e.g. `AT`).
- With the UBPet defaults the Robotail account signs in, but the backend never
  returns the litter box — the device is simply invisible.

So instead of reusing UBPet, we reverse-engineered the Robotail app's API flow:

- the `X-UBT-Sign` request-signing scheme (MD5 of timestamp + app key + nonce +
  device id),
- the login endpoint and its flat `{token, user}` response,
- the IM login, device list, and cat list endpoints,
- and the MQTT topic layout used to push live box state.

`custom_components/robotail` is the result: a working fork of UBPet, adapted to
the Robotail namespace with configurable region code.

---

## Features

- Device entity for the litter box (serial `FBE002UBT50000342` family) with box
  status, firmware version, waste bin level, deodorant days, usage counts, and
  more.
- Cat entities (weight, nickname, activity) per registered cat.
- Controls: auto clean + delay, deodorant alert, empty-waste-bin reminder, do
  not disturb, light schedule, camera/child lock, box cleaning.
- Live state over MQTT with automatic re-login when the token expires.

## Installation

1. Copy the `custom_components/robotail/` folder into your Home Assistant
   `custom_components/` directory.
2. Restart Home Assistant.
3. Settings → Devices & Services → Add Integration → search for **ROBOTAIL**.
4. Enter your Robotail/Airrobo account email and password (or rely on the
   bundled `secrets.py` defaults; region code defaults to `AT`).
5. Done — the litter box and cats appear as devices.

## Configuration

All cloud/API credentials default to the values reverse-engineered from the
Robotail app and can be overridden in `secrets.py` (see `secrets.py.example`)
or in the config flow:

| Setting | Default |
| --- | --- |
| `BASE_URL` | `https://apis-eu.airrobo-home.com` |
| `APP_ID` | `970010096` |
| `APP_KEY` | (bundled signing key) |
| `PRODUCT` | `97001` |
| `AREA_CODE` | `AT` |

## Credits

Based on [UPet HACS](https://github.com/CrazzyBerg/upet-hass). Reverse-engineering
and Robotail adaptation done for this project.

---

## Community

A Reddit thread / link for discussion is coming soon — stay tuned!
