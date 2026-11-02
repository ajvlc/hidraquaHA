# Validación de Hidraqua

La integración original confirma Sorea; el portal Hidraqua no se validó aquí con una cuenta autenticada. La dirección base `https://hidraqua.veolia.es`, login Liferay y portlet `CustomLoginPortlet` se usan como hipótesis iniciales. Las rutas por defecto para inicio y consumos y el portlet `MisConsumos` pueden variar.

## Pasos

1. Instala dependencias Python `aiohttp`.
2. En una terminal local, define `VEOLIA_USER` y `VEOLIA_PASSWORD` para las credenciales del portal (no las compartas ni las incluyas en informes).
3. Ejecuta `python scripts/probe_portal.py https://hidraqua.veolia.es`.
4. Revisa el resultado localmente. El script redacciona credenciales y evita imprimir valores del contador/factura. Comprueba especialmente login, sitio descubierto, página de consumos y registros parseados.
5. Si falla, usa el nombre de sitio que observas en la URL después del login en las opciones de la integración. La ruta o portlet incorrectos requieren ajustar el perfil en `custom_components/hidraqua_water/portal.py`.

El portal puede aplicar límites anti automatización o cambiar su estructura. No guardes ni compartas archivos HAR, cookies, encabezados de autorización, token `p_auth`, códigos de acceso ni contraseñas.
