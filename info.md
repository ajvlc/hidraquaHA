# Hidraqua Water

Tracks water consumption from the Hidraqua customer portal in Home Assistant, based on the Veolia Water integration.

- Home Assistant sensors for meter reading, period consumption and invoice details.
- Smart-meter sensors and historical statistics when the portal exposes those endpoints.
- Native Home Assistant setup flow with a configurable portal URL.

Default portal: `https://hidraqua.veolia.es`.

**Validation status:** The URL and independent integration identity are adapted. Login, site discovery, consumption page and data fields still require verification against a real Hidraqua account. See `HIDRAQUA-VALIDATION.md`.
