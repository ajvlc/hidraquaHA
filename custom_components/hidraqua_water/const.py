"""Constants for the Hidraqua Water integration."""
from __future__ import annotations

DOMAIN = "hidraqua_water"
PLATFORMS = ["sensor"]

# Configuration keys (set via config_flow and options_flow).
CONF_PORTAL_URL = "portal_url"
CONF_PORTAL_SITE = "portal_site"
CONF_CONTRACT_NUMBER = "contract_number"
CONF_SCAN_INTERVAL_HOURS = "scan_interval_hours"

DEFAULT_SCAN_INTERVAL_HOURS = 6

# External-statistics source domain (anything that's not a HA integration name).
STATS_SOURCE = "hidraqua_water"
