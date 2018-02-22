import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.components.zone import DOMAIN as ZONE_DOMAIN
from homeassistant.components.zone import ENTITY_ID_FORMAT as ZONE_ENTITY_ID_FORMAT
from homeassistant.const import CONF_ENTITY_ID
from homeassistant.helpers.condition import zone as in_zone

DOMAIN = "weasley_clock"


def setup(hass, config):
    def handle_event(event):
        entity_id = event.data.get(CONF_ENTITY_ID)
        if entity_id != config[DOMAIN].get(CONF_ENTITY_ID):
            return

        import requests
        clock = "http://{}:8000/clock/ping".format(config[DOMAIN].get("clock_host"))
        for zone in config[ZONE_DOMAIN] + [{"name": "Home"}]:
            zone_entity_id = ZONE_ENTITY_ID_FORMAT.format(zone.get("name").lower())
            if in_zone(hass, zone_entity_id, entity_id):
                requests.post(clock, data={"zone": zone_entity_id.split(".")[-1]})
                return True

        requests.post(clock, data={"zone": "away"})
        return True

    hass.bus.listen('state_changed', handle_event)
    return True
