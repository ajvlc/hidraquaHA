# Hidraqua Water para Home Assistant

Integración HACS adaptada de veoliaHA para consultar consumos de agua, lecturas, facturas y telelectura desde el portal de Hidraqua.

## Configuración

Añade el repositorio como integración personalizada en HACS, instala **Hidraqua Water**, reinicia Home Assistant y añade la integración desde **Ajustes → Dispositivos y servicios**. La URL predeterminada es `https://hidraqua.veolia.es`; introduce las credenciales de tu área de cliente.

El perfil intenta detectar automáticamente el sitio Liferay después del inicio de sesión. Si no lo detecta, configura **Portal site name** en las opciones con el nombre que aparece en la ruta `/group/<sitio>/...`.

## Estado de validación

La URL y el flujo de autenticación se han adaptado desde la implementación original. Aún falta validar con una cuenta Hidraqua real la ruta de la página de consumos, el identificador del portlet, los campos de respuesta y las entidades de datos. Hasta validar esos puntos, esta variante es una adaptación experimental y no se garantiza que todos los sensores funcionen.

Para diagnosticar sin compartir valores privados, sigue `HIDRAQUA-VALIDATION.md`. No publiques credenciales, cookies, tokens ni valores de factura/contador.

Sensores, estadísticas, intervalo de consulta y notas de privacidad siguen el comportamiento descrito en la documentación original, sujeto a esa validación.
