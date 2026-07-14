Automatización de Reportes Administrativos

Descripción
Este sistema ha sido diseñado para optimizar el procesamiento de datos administrativos mediante la validación automatizada de registros. El proyecto implementa un pipeline de Integración Continua (CI) que asegura la integridad de los datos, validando IDs administrativos y evitando inconsistencias en los valores financieros, garantizando así la calidad del reporte final.

Características Principales
Pipeline de CI/CD: Automatización completa de pruebas con GitHub Actions.

Validación de Datos: Reglas de negocio integradas para IDs administrativos (formato de 10 dígitos) y control de valores financieros no negativos.

Testing de Calidad: Cobertura de pruebas unitarias para asegurar la fiabilidad del procesamiento de datos.

Estructura del Proyecto
.github/workflows/: Contiene la configuración del pipeline de automatización.

src/: Código fuente con la lógica de procesamiento y reglas de negocio.

tests/: Suite de pruebas unitarias desarrolladas con pytest.

Tecnologías Utilizadas
Python 3.12

GitHub Actions (Pipeline de CI)

Pytest (Framework de pruebas)