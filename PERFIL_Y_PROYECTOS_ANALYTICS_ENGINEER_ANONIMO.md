# Perfil y Proyectos (Version Anonimizada)
## Enfoque: Analytics Engineer

Fecha: **10 de febrero de 2026**

---

## Resumen profesional

Soy un perfil tecnico orientado a **Analytics Engineering**: conecto fuentes de datos operativas, diseno pipelines confiables, construyo modelos semanticos en Power BI y automatizo procesos criticos de negocio para convertir trabajo manual en sistemas escalables.

Mi diferencial no es solo crear dashboards, sino disenar el flujo completo:

- **Ingesta** (APIs, CRM, plataformas de contact center, datos cloud).
- **Modelado** (SQL + DAX + Power Query M).
- **Calidad y gobernanza** (validaciones, documentacion, trazabilidad).
- **Operacion** (automatizacion, observabilidad, alertas, reintentos).

---

## Que puedo aportar a una empresa

- Reducir dependencia de procesos manuales en reporting y operacion.
- Mejorar confiabilidad de pipelines (menos fallos, menos reprocesos).
- Acelerar tiempos de decision con datos mas frescos y consistentes.
- Escalar modelos analiticos sin degradar rendimiento.
- Estandarizar buenas practicas de modelado, documentacion y mantenimiento.
- Conectar analytics con operacion real (equipos comerciales, marketing y contact center).

---

## Proyectos representativos (anonimizados)

## 1) Optimizacion de modelos semanticos Power BI

**Problema que resolvia**

Modelos de analitica operativa con alta carga de negocio, donde el crecimiento funcional habia generado recalculos costosos, dificultad para mantener medidas y riesgo de romper reportes al hacer cambios.

**Complejidad tecnica**

- Modelos con **300+ medidas** y **80+ relaciones**.
- Logica fila a fila en dimensiones clave.
- Relaciones activas/inactivas con dependencia de medidas de tiempo.
- Necesidad de optimizar sin afectar visuales ya en produccion.

**Arquitectura y enfoque de solucion**

- Auditoria tecnica del modelo (medidas, relaciones, columnas, refresh y exposicion).
- Descarga de logica pesada hacia tablas snapshot tecnicas.
- Reemplazo de patrones de alto costo por lookups controlados.
- Normalizacion de descripciones y curacion del panel de campos.
- Definicion de checklist de calidad para futuras publicaciones.

**Que implemente (concretamente)**

- Refactor de logica pesada por fila hacia tablas snapshot y lookups.
- Limpieza de exposicion (ocultacion de campos tecnicos).
- Estandarizacion de descripciones de medidas/columnas.
- Auditorias de rendimiento y guia de replicacion.

**Stack tecnico**

- Power BI Desktop
- DAX
- Power Query M
- Modelo tabular

**Librerias destacables**

- Funciones DAX: `CALCULATE`, `LOOKUPVALUE`, `USERELATIONSHIP`, `TREATAS`
- Patrones M para transformacion y tablas auxiliares

**Resultados**

- Reduccion de complejidad en calculos DAX costosos.
- Mejor mantenibilidad del modelo y experiencia de autoservicio.
- Menor riesgo operativo al evolucionar modelos complejos.
- Modelos documentados con mas gobernanza tecnica.

---

## 2) Data products en BigQuery para consolidacion de leads

**Problema que resolvia**

La informacion de leads estaba distribuida en muchas tablas OUT con estructuras variables, lo que hacia lento y fragil el consumo para BI y operacion.

**Complejidad tecnica**

- Cientos de tablas fuente y crecimiento continuo.
- Esquemas parcialmente inconsistentes entre tablas.
- Limite tecnico de tamano en definiciones de vistas.
- Necesidad de trazabilidad por proyecto sin hardcodeo manual permanente.

**Arquitectura y enfoque de solucion**

- Capa de vistas intermedias + vista consolidada final.
- Filtro automatico de tablas por umbral de volumen.
- Mapeo de proyecto desde tabla de control.
- Generacion automatica de vistas filtradas por dominio.

**Que implemente (concretamente)**

- Construccion de vistas consolidadas y segmentadas por dominio.
- Filtro automatico de tablas de bajo volumen.
- Estrategia de vistas intermedias para evitar limites tecnicos de plataforma.
- Automatizacion del proceso para incorporar nuevas tablas sin rediseno manual.

**Stack tecnico**

- BigQuery
- SQL
- Python
- Data warehouse views

**Librerias destacables**

- `google-cloud-bigquery`
- `python-dotenv`

**Resultados**

- Flujo repetible y escalable para nuevas cargas.
- Menor esfuerzo operativo de mantenimiento.
- Capa de datos mas consistente para analisis y reporting.
- Menos tiempo de preparacion de datos para equipos de negocio.

---

## 3) ETLs de Marketing Analytics (Google Ads + Meta Ads)

**Problema que resolvia**

Los datos de plataformas de ads venian de APIs distintas, con reglas de extraccion diferentes y riesgo de inconsistencias al consolidar rendimiento de campanas.

**Complejidad tecnica**

- Multiples cuentas y jerarquias (cuenta, campana, adset, anuncio).
- Limites y throttling de API.
- Necesidad de incrementalidad para no reprocesar historicos completos.
- Dependencia de calidad de claves para star schema y reporting comparativo.

**Arquitectura y enfoque de solucion**

- ETL desacoplado por plataforma con una capa comun de carga a MySQL.
- Control incremental por tabla de watermark y ventana de solape.
- Upsert por lotes para idempotencia.
- Orquestador unico con resumen final y alertas de fallo.

**Que implemente (concretamente)**

- ETLs incrementales con control de ultima sincronizacion.
- Upserts por lotes en modelo tipo star schema.
- Manejo de errores de API con retry/backoff.
- Orquestacion y monitoreo por logs + correo.

**Stack tecnico**

- Python
- Google Ads API
- Meta Ads API
- MySQL
- SQL

**Librerias destacables**

- `google-ads`
- `facebook-business`
- `mysql-connector-python`
- `requests`
- `python-dateutil`
- `python-dotenv`
- `PyYAML`

**Resultados**

- Mayor continuidad operativa de carga.
- Datos mas oportunos para optimizacion de inversion.
- Menos trabajo manual de extraccion y normalizacion.
- Base analitica estable para comparar performance entre canales.

---

## 4) Automatizacion de procesos CRM con autenticacion empresarial

**Problema que resolvia**

Un proceso de negocio critico dependia de ejecucion manual diaria y era sensible a cambios de interfaz, tiempos de carga, autenticacion y errores humanos.

**Complejidad tecnica**

- Flujo autenticado con SSO + OTP.
- Navegacion en interfaces dinamicas con iframes/modales.
- Descarga de archivos y validacion de integridad.
- Carga incremental con deduplicacion y actualizacion de existentes.

**Arquitectura y enfoque de solucion**

- Pipeline end-to-end: autenticacion -> extraccion -> limpieza -> carga -> notificacion.
- Reintentos por etapa y reintento global con backoff.
- Logging detallado + artefactos de debug para fallos UI.
- Reporte automatico de metricas de ejecucion.

**Que implemente (concretamente)**

- Automatizacion end-to-end (navegacion, autenticacion, descarga, transformacion, carga).
- Integracion con MySQL via upsert incremental.
- Instrumentacion con metricas de ejecucion y alertas.
- Endurecimiento con reintentos multi-etapa.

**Stack tecnico**

- Python
- Browser automation
- MySQL
- SQL

**Librerias destacables**

- `playwright`
- `selenium`
- `pandas`
- `numpy`
- `openpyxl`
- `beautifulsoup4`
- `mysql-connector-python`
- `python-dotenv`

**Resultados**

- Mejora fuerte de tasa de exito operacional (de escenario fragil a estable).
- Reduccion de tiempos de intervencion humana.
- Mayor trazabilidad y control de fallos.
- Operacion mas predecible para procesos comerciales diarios.

---

## 5) Integraciones con Nextiva (sincronizacion operativa y DNC)

**Problema que resolvia**

El equipo necesitaba sincronizar listas de seguimiento y gestionar restricciones de contacto de forma consistente, sin procesos manuales repetitivos.

**Complejidad tecnica**

- Integracion entre warehouse y API operativa.
- Ventanas temporales semanales con reglas de negocio.
- Riesgo de duplicados y registros no validos.
- Gestion de estados DNC con impacto en compliance operativo.

**Arquitectura y enfoque de solucion**

- Job batch programado (semanal) con query en BigQuery.
- Capa de validacion y deduplicacion previa a insercion en Nextiva.
- Scripts CLI para operaciones DNC unitarias y masivas.
- Wrappers para ejecucion automatica (cron / scheduler) y monitoreo.

**Que implemente (concretamente)**

- Flujos batch semanales desde cloud data warehouse hacia listas outbound de **Nextiva**.
- Validaciones de calidad y prevencion de duplicados.
- Herramientas CLI y librerias para gestion DNC (bloquear/consultar/desbloquear).

**Stack tecnico**

- Nextiva API
- Python
- BigQuery
- SQL

**Librerias destacables**

- `requests`
- `google-cloud-bigquery`
- `python-dotenv`
- `argparse` (CLI)

**Resultados**

- Menor carga operativa manual del equipo.
- Mejor control de listas y cumplimiento operativo.
- Mayor consistencia entre analitica y ejecucion comercial.
- Proceso auditable y mas robusto ante errores de carga.

---

## 6) Automatizaciones de telemetria de llamadas (near real-time)

**Problema que resolvia**

La operacion necesitaba visibilidad frecuente del detalle de llamadas y estado de actividad, sin esperar cierres diarios ni procesos manuales.

**Complejidad tecnica**

- Ventanas temporales cortas y continuas.
- Diferencias de timezone y formatos de fecha.
- Campos heterogeneos por proveedor de telefonia.
- Necesidad de idempotencia para evitar duplicados en reintentos.

**Arquitectura y enfoque de solucion**

- ETL por ventana movil con parametrizacion por entorno.
- Normalizacion de identificadores telefonicos.
- Carga incremental por clave unica y upsert.
- Scheduler operativo en franjas horarias de negocio.

**Que implemente (concretamente)**

- ETLs con ventanas moviles de tiempo.
- Normalizacion de telefonos y campos heterogeneos.
- Upserts idempotentes en MySQL.
- Scheduling recurrente en horario operativo.

**Stack tecnico**

- Python
- APIs de telefonia/call detail
- MySQL
- SQL
- Scheduling

**Librerias destacables**

- `requests`
- `mysql-connector-python`
- `APScheduler`
- `pytz`
- `python-dotenv`

**Resultados**

- Menor latencia entre operacion y analisis.
- Mayor confiabilidad del dato para monitoreo diario.
- Base mas solida para seguimiento operativo casi en tiempo real.

---

## 7) Data Quality y reconciliacion entre fuentes

**Problema que resolvia**

Existian diferencias frecuentes entre fuentes (archivos, bases y sistemas operativos), lo que afectaba confianza en KPIs y generaba mucho tiempo de investigacion manual.

**Complejidad tecnica**

- Fuentes con formatos y granularidad distintos.
- Claves sucias (telefonos, nombres, fechas, estados).
- Necesidad de explicar discrepancias con evidencia trazable.

**Arquitectura y enfoque de solucion**

- Scripts de reconciliacion reproducibles.
- Estandares de normalizacion de claves.
- Salidas de diagnostico para negocio y para equipo tecnico.
- Notebooks para analisis exploratorio y explicacion de hallazgos.

**Que implemente (concretamente)**

- Scripts de conciliacion por claves normalizadas (por ejemplo, telefono).
- Reportes de no-coincidencias y diferencias de estado/fecha.
- Notebooks de diagnostico para investigacion rapida.

**Stack tecnico**

- Python
- Jupyter Notebook
- CSV/Excel
- Pandas-based analysis

**Librerias destacables**

- `pandas`
- `openpyxl`
- `ipykernel` / `jupyter`

**Resultados**

- Menos tiempo invertido en troubleshooting manual.
- Identificacion temprana de problemas de calidad de datos.
- Mejor confianza en reportes y toma de decisiones.

---

## Stack tecnico global

### Lenguajes y modelado

- Python
- SQL
- DAX
- Power Query M

### Plataformas y datos

- Power BI (modelado semantico y reporting)
- BigQuery
- MySQL
- Nextiva (integraciones operativas)

### Librerias y herramientas clave

- `pandas`, `numpy`
- `google-ads`, `facebook-business`
- `playwright`, `selenium`
- `mysql-connector-python`, `sqlalchemy`
- `requests`, `python-dotenv`, `PyYAML`
- `APScheduler`

---

## Evidencia de impacto (presentable en perfil)

- Experiencia con modelos de alta complejidad (hasta **300+ medidas** y **80+ relaciones** en un modelo).
- Optimizacion de logica analitica para reducir costo de recalculo y mejorar mantenibilidad.
- Automatizaciones CRM con mejora de confiabilidad reportada de aproximadamente **~30% a ~90-95%** en escenarios criticos.
- Procesos diarios de carga con volumen operativo de **miles de registros**.
- Flujos semanales automaticos de sincronizacion comercial con validaciones de calidad y control de duplicados.
- Operacion sobre datasets de escala **millones de filas** en entornos cloud.

---

## Propuesta de valor para tu marca profesional

Si te vendes como **Analytics Engineer**, este es el mensaje que mejor encaja con lo que ya demostraste:

- No solo construyes reportes: construyes **sistemas analiticos end-to-end**.
- No solo calculas KPIs: garantizas **calidad, confiabilidad y operacion**.
- No solo conectas datos: traduces datos en **eficiencia operacional y decisiones mas rapidas**.

---

## Extracto breve sugerido (LinkedIn/Web)

Analytics Engineer especializado en integrar datos operativos y comerciales en soluciones analiticas escalables. Diseno pipelines de datos, modelos semanticos en Power BI y automatizaciones de procesos criticos (CRM, marketing y contact center), con foco en rendimiento, confiabilidad y valor de negocio.
