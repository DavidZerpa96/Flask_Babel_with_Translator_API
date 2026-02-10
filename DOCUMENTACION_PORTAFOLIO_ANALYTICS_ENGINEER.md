# Portafolio Técnico Profesional
## Posicionamiento: de BI Developer a Analytics Engineer

Fecha de corte del análisis: **10 de febrero de 2026**

---

## 1) Objetivo del documento

Documentar, de forma pública y sin datos sensibles, el trabajo desarrollado en este repositorio para:

- Mostrar proyectos reales entregados.
- Evidenciar stack técnico y habilidades desarrolladas.
- Explicar problemas de negocio resueltos.
- Comunicar impacto operativo (ahorro de tiempo, mejora de calidad, automatización y escalabilidad).
- Reforzar tu posicionamiento como **Analytics Engineer**.

---

## 2) Metodología de análisis

Se realizó una revisión técnica combinando:

- Análisis de estructura de carpetas y código fuente (`.py`, `.sql`, `.pbix`, `.md`, `.ipynb`).
- Lectura de documentación técnica por proyecto.
- Revisión de pipelines ETL y automatizaciones (orquestación, reintentos, upserts, alertas).
- Uso de MCP para validar contexto en plataforma:
  - **Power BI Modeling MCP**: sin conexiones activas detectadas en esta sesión.
  - **BigQuery MCP**: datasets y conteos reales para dimensionar escala de operación.

Regla de sanitización aplicada:

- No incluir credenciales, tokens, emails, teléfonos, IDs operativos ni payloads sensibles.
- Solo métricas agregadas, arquitectura y capacidades técnicas.

---

## 3) Alcance revisado (inventario técnico)

Conteo de archivos relevantes (excluyendo entornos virtuales y dependencias locales):

| Proyecto | Archivos | PY | SQL | PBIX | MD | IPYNB | JSON |
|---|---:|---:|---:|---:|---:|---:|---:|
| Marketing ads pipeline | 1097 | 23 | 23 | 20 | 0 | 0 | 937 |
| Carpathia | 123 | 9 | 3 | 25 | 29 | 0 | 3 |
| Flujos automatizados nextiva | 49 | 26 | 2 | 0 | 15 | 0 | 1 |
| Integraciones CRM's | 48 | 11 | 4 | 0 | 12 | 0 | 1 |
| MCP_Power_bi | 26 | 0 | 0 | 0 | 7 | 0 | 3 |
| ETL-GOOGLE-DIGITAL | 23 | 5 | 4 | 0 | 7 | 0 | 1 |
| NextivaProject | 17 | 2 | 0 | 3 | 2 | 1 | 1 |
| ETL-FACEBOOK-DIGITAL | 10 | 9 | 0 | 0 | 0 | 0 | 0 |
| Automatización Maniform | 8 | 4 | 1 | 0 | 0 | 0 | 0 |
| Scripts | 6 | 2 | 0 | 0 | 0 | 0 | 0 |

Conclusión de alcance: hay evidencia fuerte de trabajo transversal en **BI + Data Engineering + Automation + Integraciones operativas**, que corresponde más a un perfil de Analytics Engineering que a BI tradicional.

---

## 4) Evidencia de escala en BigQuery (MCP, 2026-02-10)

### Datasets detectados

- `Query_views`
- `becall`
- `becall_out`
- `my_analytics`
- `util`

### Métricas de escala (snapshot de consulta)

- Objetos tipo `OUT%` en `becall_out`: **788**
- Objetos en `Query_views`: **32**
- Filas en `Query_views.lead_view`: **137,019**
- Filas en `Query_views.calls_view`: **292,096**
- Filas en `Query_views.agent_states_view`: **1,160,893**
- Filas en `Query_views.vista_call_event_counts_table`: **1,741,684**
- Filas en `becall.CALL_DETAILS`: **550,910**
- Filas en `becall.REALTIME_USERS`: **3,022,303**

Observación técnica:

- Se detectaron vistas heredadas que no validan en dry run (`updated_calls_view`, `repsol_colombia_calls_view`), señalando oportunidad de hardening técnico y housekeeping de objetos legacy.

---

## 5) Stack consolidado

### Lenguajes y motores

- **Python** (ETL, automatización, integraciones API, CLI, orquestación)
- **SQL** (MySQL y BigQuery)
- **DAX / Power Query M** (modelado semántico y lógica analítica)
- **JSON/YAML** (configuración de APIs y credenciales estructuradas)

### Datos y almacenamiento

- **BigQuery** (datasets operativos, vistas de consumo y capas analíticas)
- **MySQL** (tablas dimensionales/factuales, staging y upserts transaccionales)
- **Power BI Semantic Models** (múltiples modelos empresariales)

### Integraciones y librerías

- Ads APIs: `google-ads`, `facebook-business`
- Automatización web: `playwright`, `selenium`
- Transformación/analítica: `pandas`, `numpy`
- DB connectors: `mysql-connector-python`, `pymysql`, `sqlalchemy`
- Scheduling y utilidades: `APScheduler`, `python-dotenv`, `requests`, `PyYAML`

### Observabilidad y operación

- Logging estructurado por ejecución
- Alertas por correo en éxito/fallo
- Reintentos con backoff exponencial
- Ejecución por cron/Task Scheduler
- Scripts de verificación y troubleshooting

---

## 6) Portafolio de proyectos (fichas de impacto)

## 6.1 Carpathia (Power BI + BigQuery + optimización semántica)

**Problema que resuelve**

- Modelos de reporting complejos con alto costo de recálculo y mantenimiento manual.
- Necesidad de consolidar múltiples fuentes de leads y operación en un marco analítico único.

**Qué se implementó**

- Modelos Power BI empresariales (Energía, Alarmas, Solvo y otros).
- Auditoría de rendimiento de modelos con refactor de `DimLeads` a snapshots técnicos.
- Pipeline BigQuery para construir vistas consolidadas de leads con segmentación por proyecto.
- Lógica de objetivos dinámicos en M + DAX.

**Stack**

- Power BI, DAX, Power Query M, BigQuery, Python, SQL.

**Habilidades evidenciadas**

- Modelado semántico avanzado.
- Optimización de rendimiento de modelo.
- Diseño de data products (vistas analíticas reutilizables).
- Gobernanza de campos/medidas y documentación técnica.

**Impacto**

- Reducción de cálculo fila a fila en dimensiones críticas.
- Eliminación de patrones pesados (`RELATEDTABLE`/`TOPN`) en olas de optimización.
- Mejora de mantenibilidad por snapshots y documentación funcional.

**Métricas relevantes**

- Energía Madrid: **145 medidas**, **53 relaciones**.
- Alarmas Madrid (post optimización): **347 medidas**, **89 relaciones**, **108 tablas**.
- Solvo: **77 medidas**, **39 relaciones**, **47 tablas**.
- Eliminación documentada de **41** ocurrencias de patrones DAX pesados en Alarmas.

---

## 6.2 BigQuery Lead Views (Carpathia/BigQuery)

**Problema que resuelve**

- Unificación de cientos de tablas OUT heterogéneas y crecimiento continuo de cargues.
- Limitación técnica de tamaño de definición de vistas en BigQuery.

**Qué se implementó**

- Script `create_lead_view.py` que:
  - filtra automáticamente tablas con bajo volumen,
  - divide en vistas intermedias para evitar límite de 256K caracteres,
  - genera vista consolidada y vistas por proyecto.

**Stack**

- Python + BigQuery SQL.

**Habilidades evidenciadas**

- Data modeling en capa de vistas.
- Diseño resiliente frente a límites de plataforma.
- Normalización de esquemas inconsistentes.

**Impacto**

- Proceso repetible de alta escalabilidad para ingestión analítica de leads.
- Menor tiempo manual al incorporar nuevos cargues y tablas.

**Métricas relevantes**

- Documentación operativa: **36 tablas útiles de 192** (umbral `>=30` registros, en ese corte histórico).
- Tiempo de ejecución reportado: **~5-10 minutos**.

---

## 6.3 ETL-GOOGLE-DIGITAL

**Problema que resuelve**

- Extracción manual/no estandarizada de métricas de Google Ads para BI.

**Qué se implementó**

- ETL completo hacia esquema MySQL tipo star schema.
- Carga incremental con `time_update_digital` y solape de 2 días.
- Upserts por lotes y control de consistencia.

**Stack**

- Python, Google Ads API, MySQL, SQL.

**Habilidades evidenciadas**

- Diseño ETL incremental.
- Manejo de APIs externas con robustez operativa.
- Integración Marketing Analytics + BI.

**Impacto**

- Reduce operaciones manuales de descarga/limpieza de campañas.
- Mejora frescura y trazabilidad de datos para decisiones de inversión.

---

## 6.4 ETL-FACEBOOK-DIGITAL

**Problema que resuelve**

- Falta de pipeline robusto para Meta Ads con múltiples cuentas y throttling.

**Qué se implementó**

- ETL de campañas/adsets/ads/métricas con reintentos y backoff.
- Extracción de credenciales cifradas desde base de datos.
- Orquestador con logs y alertas por email.

**Stack**

- Python, Facebook Business API, MySQL.

**Habilidades evidenciadas**

- Manejo de errores de API en producción.
- Seguridad básica de credenciales.
- Operación automatizada con monitorización.

**Impacto**

- Mayor continuidad de carga pese a límites de API y errores transitorios.
- Menor dependencia de ejecución manual.

---

## 6.5 Marketing ads pipeline (orquestación multifuente + BI)

**Problema que resuelve**

- Necesidad de centralizar Google + Meta en un flujo único para análisis de performance.

**Qué se implementó**

- Orquestadores que ejecutan ambos pipelines.
- Logging, manejo de errores y notificaciones.
- Base de reportes Power BI asociados a marketing y operación.

**Stack**

- Python, Ads APIs, MySQL, Power BI.

**Habilidades evidenciadas**

- Integración multi-plataforma.
- Operación de pipelines de marketing en lote.
- Construcción de capa analítica para reporting ejecutivo.

**Impacto**

- Unificación operativa de fuentes paid media.
- Menos fricción entre extracción, modelado y visualización.

---

## 6.6 Automatización CRM Repsol

**Problema que resuelve**

- Proceso manual frágil de exportación CRM (SSO + OTP + descarga + carga).

**Qué se implementó**

- Pipeline end-to-end con login SSO, lectura OTP en Outlook, exportación 360, limpieza y upsert a MySQL.
- Reintentos robustos, validación de integridad y envío de métricas por email.

**Stack**

- Python, Playwright/Selenium, Pandas, MySQL.

**Habilidades evidenciadas**

- Browser automation empresarial.
- Integración de seguridad operacional (OTP).
- Carga incremental y trazabilidad de ejecución.

**Impacto**

- Conversión de proceso crítico manual a job automatizado.
- Aumento fuerte de fiabilidad operacional.

**Métricas relevantes**

- Mejora estimada de tasa global: **~30% -> ~90-95%**.
- Tiempo típico de ejecución: **5-10 minutos**.
- Volumen operativo reportado: **~1000-2000 registros diarios**.

---

## 6.7 Automatización CRM ADT

**Problema que resuelve**

- Descarga/carga diaria de contratos con riesgo de fallos por UI/cambios del portal.

**Qué se implementó**

- Automatización Playwright (headless).
- Reintentos por etapa y globales.
- Deduplicación, auto-migración de columnas y upsert en MySQL.
- Reporte automático por email.

**Stack**

- Python, Playwright, MySQL, Pandas.

**Habilidades evidenciadas**

- Robustez de scraping en entorno cambiante.
- Data quality pre-carga.
- Operación de jobs con alerting.

**Impacto**

- Menos intervención manual en operación diaria.
- Mayor continuidad de carga y confiabilidad del dato.

---

## 6.8 Automatización CRM GANA

**Problema que resuelve**

- Sincronización de ventas de portal con base operativa, con riesgo de duplicados y fallos transitorios.

**Qué se implementó**

- Extracción automática con Playwright y paginación.
- Sincronización inteligente con reintentos e incremental wait.
- Integración con MySQL y notificaciones por email.

**Stack**

- Python, Playwright, MySQL.

**Habilidades evidenciadas**

- Diseño de sincronización robusta.
- Gestión de errores y tolerancia a fallos.
- Integración operacional de CRM.

**Impacto**

- Pipeline estable para actualización de ventas sin operación manual repetitiva.

---

## 6.9 Flujo No Interesa -> Nextiva/Thrio

**Problema que resuelve**

- Reprocesar de forma ordenada leads con disposición de rechazo para estrategias de seguimiento.

**Qué se implementó**

- Flujo semanal automático (lunes) desde BigQuery hacia listas outbound Nextiva/Thrio.
- Filtros por disposiciones objetivo, control de duplicados, dry-run y runners para cron/scheduler.

**Stack**

- Python, BigQuery, API Nextiva/Thrio.

**Habilidades evidenciadas**

- Integración entre warehouse y plataforma de contact center.
- Orquestación batch programada.
- Controles de calidad para evitar contaminación de listas.

**Impacto**

- Automatiza un proceso comercial recurrente.
- Disminuye carga operativa manual del equipo.

**Métricas relevantes**

- Ejecución documentada: **212 leads procesados correctamente**.
- Limpieza histórica reportada: **~1,434 duplicados** removidos (changelog).

---

## 6.10 Integración DNC Thrio/Nextiva

**Problema que resuelve**

- Gestión de bloqueo de contactos (Do Not Call) y reducción de riesgo operativo/compliance.

**Qué se implementó**

- CLI + librería para bloquear, consultar y desbloquear teléfonos.
- Soporte de bloqueo automático y manual (comm types diferenciados).
- Scripts de bloqueo masivo.

**Stack**

- Python, API Thrio/Nextiva.

**Habilidades evidenciadas**

- Diseño de utilidades operativas reutilizables.
- Integración con APIs de contact center.
- Enfoque en cumplimiento y control.

**Impacto**

- Estandariza y acelera la gestión DNC.
- Reduce probabilidad de contactos no permitidos.

---

## 6.11 Automatización reportes Thrio/Nextiva (positivos Repsol)

**Problema que resuelve**

- Dependencia de ejecución manual para actualizar rango, descargar y preparar reportes.

**Qué se implementó**

- Flujo para actualizar rango del reporte por API, descargar datos, limpiar y exportar CSV.
- Modo enriquecido con cruce a MySQL (CRM Repsol).

**Stack**

- Python, requests, pandas, MySQL.

**Habilidades evidenciadas**

- Integración API + enriquecimiento de datos.
- Preparación de datasets listos para operación/comercial.

**Impacto**

- Acelera generación de reportes accionables para seguimiento comercial.

---

## 6.12 Automatización Maniform

**Problema que resuelve**

- Necesidad de ingestión frecuente de detalle de llamadas por campaña.

**Qué se implementó**

- ETL con ventana móvil de tiempo y normalización de teléfonos.
- Upsert por `id` en MySQL.
- Scheduler cada 20 minutos en horario laboral.

**Stack**

- Python, API Maniterm, APScheduler, MySQL.

**Habilidades evidenciadas**

- Near-real-time ingestion.
- Programación y operación de jobs recurrentes.
- Normalización de datos de telecom.

**Impacto**

- Reduce latencia de disponibilidad de llamadas para análisis operativo.

---

## 6.13 Automatización Masvoz API

**Problema que resuelve**

- Falta de extracción automatizada por dirección/ventana de llamadas.

**Qué se implementó**

- Ingesta por API con mapeo de campos heterogéneos.
- Upsert dinámico en tabla configurable y almacenamiento de payload raw.

**Stack**

- Python, API Masvoz, MySQL.

**Habilidades evidenciadas**

- Integración API resiliente.
- Diseño de mapeos flexibles para contratos de datos variables.

**Impacto**

- Estandariza captura de llamadas sin intervención manual.

---

## 6.14 Scripts de calidad de datos y notebook analítico

**Problema que resuelve**

- Detección de discrepancias de leads entre fuentes (CSV/Excel/portal/DB).

**Qué se implementó**

- Scripts de reconciliación por teléfono normalizado y exportes de no-matcheados.
- Notebook de análisis de inconsistencias temporales y de deuda.

**Stack**

- Python, Pandas, Jupyter.

**Habilidades evidenciadas**

- Data quality y conciliación entre sistemas.
- Diagnóstico rápido de inconsistencias operativas.

**Impacto**

- Menor tiempo de investigación manual en incidencias de datos.

---

## 6.15 MCP_Power_bi (tooling/plataforma)

**Problema que resuelve**

- Necesidad de acelerar operaciones de modelado semántico asistidas por agentes.

**Qué se implementó / integró**

- Paquete local del servidor **Power BI Modeling MCP** (v0.1.8) con capacidades de bulk operations y automatización de modelado.

**Stack**

- TypeScript/Node (paquete de extensión), MCP, Power BI.

**Habilidades evidenciadas**

- Orientación a plataforma interna.
- Adopción de tooling AI para productividad en semántica.

**Impacto**

- Potencial de reducción de tareas repetitivas de modelado/documentación.

---

## 7) Habilidades consolidadas (mapa para perfil)

### Núcleo de Analytics Engineering

- Diseño de pipelines de datos confiables.
- Modelado semántico orientado a negocio.
- Orquestación y automatización de procesos críticos.
- Estándares de calidad, documentación y gobernanza.
- Integración entre capas: API -> DWH/DB -> semantic model -> reporting.

### Habilidades diferenciales observadas

- Optimización de rendimiento en modelos Power BI complejos.
- Patrones de resiliencia operativa (retry/backoff, alerting, validaciones).
- Capacidad de mover lógica de negocio de procesos manuales a sistemas automatizados.
- Enfoque pragmático de impacto (tiempo, fiabilidad, escalabilidad).

---

## 8) Mensaje profesional sugerido (LinkedIn/Web)

### Titular (opción recomendada)

**Analytics Engineer | Data & BI Solutions | Power BI, BigQuery, Python, Automation**

### Extracto profesional sugerido

Ingeniero de Analítica especializado en convertir operaciones manuales y datos dispersos en sistemas analíticos escalables. Diseño y opero pipelines de datos, modelos semánticos en Power BI y automatizaciones de procesos CRM/contact center, integrando APIs, BigQuery/MySQL y reporting ejecutivo. Mi foco está en fiabilidad, rendimiento y valor de negocio: menos trabajo manual, mejor calidad de dato y decisiones más rápidas.

### 6 logros tipo bullet para perfil

- Diseñé y optimicé modelos Power BI de alta complejidad (hasta 347 medidas y 89 relaciones), mejorando mantenibilidad y rendimiento.
- Construí data products en BigQuery para unificar leads de múltiples fuentes con lógica escalable ante crecimiento de tablas.
- Implementé ETLs incrementales para Google Ads y Meta Ads con upserts y control de consistencia.
- Automaticé pipelines CRM (SSO/OTP/exportación/carga) elevando la fiabilidad de ejecución de ~30% a ~90-95%.
- Integré BigQuery con Nextiva/Thrio para sincronizaciones operativas semanales y gestión de listas de seguimiento.
- Desarrollé utilidades de cumplimiento DNC y scripts de data quality para reducir riesgo operativo y tiempos de diagnóstico.

---

## 9) Checklist para publicación sin datos sensibles

Antes de publicar casos en LinkedIn/web:

- Sustituir nombres de tablas específicas por nombres funcionales (ej. `tabla_outbound_A`).
- No publicar tokens, correos, números, IDs de cuenta ni rutas con credenciales.
- Compartir solo métricas agregadas y rangos porcentuales.
- Anonimizar clientes cuando aplique (sector/caso de uso en vez de identificador exacto).
- Publicar arquitectura y resultados, no artefactos de acceso.

---

## 10) Fuentes principales (internas del repositorio)

- `Carpathia/Documentacion_Informe_General_Energia_Madrid/README.md`
- `Carpathia/Documentacion_Informe_General_Alarmas_Madrid/README.md`
- `Carpathia/Documentacion_Informe_General_Alarmas_Madrid/03_Comparativa_Energia_vs_Alarmas.md`
- `Carpathia/Documentacion_Informe_General_Solvo/README.md`
- `Carpathia/docs/auditoria_modelo_energia_madrid_2026-02-06.md`
- `Carpathia/docs/auditoria_modelo_alarmas_madrid_2026-02-06.md`
- `Carpathia/BigQuery/README.md`
- `Carpathia/BigQuery/scripts/create_lead_view.py`
- `ETL-GOOGLE-DIGITAL/README.md`
- `ETL-GOOGLE-DIGITAL/DOCUMENTACION_COMPLETA.md`
- `ETL-FACEBOOK-DIGITAL/ETL META DIGITAL/RUN_DIGITAL.py`
- `ETL-FACEBOOK-DIGITAL/ETL META DIGITAL/API_META_SCRIPT_DIGITAL.py`
- `Integraciones CRM's/Automatizacion CRM Repsol/README.md`
- `Integraciones CRM's/Automatizacion CRM Repsol/documentacion-web-scraping-crm-repsol.md`
- `Integraciones CRM's/Automatizacion-CRM-ADT/README.md`
- `Integraciones CRM's/Automatización-CRM-GANA/README.md`
- `Flujos automatizados nextiva/No interesa-outboundlist/README.md`
- `Flujos automatizados nextiva/No interesa-outboundlist/CHANGELOG.md`
- `Flujos automatizados nextiva/No interesa-outboundlist/docs/RESUMEN_PROYECTO.md`
- `Flujos automatizados nextiva/Thrio_DNC_Integration/README.md`
- `NextivaProject/Automatización-wa-positivos-repsol-nextiva/README.md`
- `NextivaProject/Automatización-wa-positivos-repsol-nextiva/DOCUMENTACION.md`
- `Automatización Maniform/main.py`
- `Automatizacion-masvoz-api/fetch_and_ingest_masvoz.py`
- `Scripts/matchesLeads.py`
- `Scripts/checkingLeadsOCM.py`
- `Análisis notebook/FinetworkAnalisis/FinetworkAnalisis.ipynb`
- `MCP_Power_bi/analysis-services.powerbi-modeling-mcp-0.1.8@win32-x64/extension/README.md`

