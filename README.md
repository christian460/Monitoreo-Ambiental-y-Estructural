# Sistema de Monitoreo Ambiental y Estructural con Telemetría IoT

**Entidad:** Universidad Nacional de San Agustín de Arequipa (UNSA)  
**Unidad:** Unidad de Gestión de la Investigación (UGINY - UNSA)  
**Alcance:** Auditoría técnica de adquisición de bienes, verificación de compatibilidad de hardware, diseño de arquitectura de software y planificación para dashboard web escalable hacia visión artificial.

---

## 📋 Descripción del Proyecto

Este repositorio contiene la **auditoría técnica documental exhaustiva** realizada a la propuesta de adquisición de equipamiento tecnológico presentada para el proyecto de monitoreo ambiental y estructural, así como la **especificación técnica de desarrollo de software** que servirá como base para la construcción del backend, base de datos de series temporales y dashboard web.

> [!CRITICAL]
> **Condición de Adquisición:** Según las bases técnicas del proyecto, una vez aprobada la compra no se permitirán compras adicionales para corregir incompatibilidades u omisiones. Por tal motivo, los informes identifican anticipadamente cualquier incumplimiento, incompatibilidad eléctrica, limitación de buses o accesorio faltante.

---

## 📁 Estructura del Repositorio

```text
├── Fuentes/                                  # Documentación fuente original del proceso
│   ├── PROPUESTA 1.pdf                       # Cotización formal y fichas técnicas del postor SERCIA EIRL
│   ├── Requerimientos_1.jpeg                 # Bases técnicas oficiales UNSA - Ítems 1 al 5
│   └── Requerimientos_2.jpeg                 # Bases técnicas oficiales UNSA - Ítems 6 al 9 (visado institucional)
│
├── informe/                                  # Informes técnicos de auditoría y desarrollo
│   ├── 01_informe_auditoria_cumplimiento.md  # Informe Maestro de Auditoría de Adquisición (20 apartados)
│   ├── 02_especificacion_tecnica_desarrollo.md # Especificación de Software, Base de Datos y Dashboard
│   ├── 03_matriz_cumplimiento.csv            # Matriz de trazabilidad y cumplimiento (68 requisitos)
│   ├── 04_consultas_al_proveedor.md          # Pliego de 9 consultas técnicas formales al postor
│   └── 05_fuentes_y_evidencias.md            # Registro de evidencias, fichas oficiales y normativas
│
└── scratch/                                  # Scripts técnicos de automatización y generación
    ├── generate_audit_report.py
    ├── generate_csv.py
    ├── generate_dev_spec.py
    ├── generate_sources_evidence.py
    └── generate_supplier_queries.py
```

---

## 📊 Resumen de Resultados de la Auditoría Técnica

De un total de **68 requisitos y parámetros evaluados**:

| Estado de Cumplimiento | Cantidad | Porcentaje | Significado Metrológico / Técnico |
|---|---|---|---|
| **CUMPLE** | 44 | 64.71 % | Parámetro demostrado con evidencia documental verificable. |
| **NO CUMPLE** | 11 | 16.18 % | Discrepancia frontal con las bases u omisión total del bien. |
| **CUMPLE PARCIALMENTE** | 8 | 11.76 % | Cumple bajo rangos restringidos o con limitaciones operativas. |
| **NO VERIFICABLE** | 4 | 5.88 % | Información insuficiente o falta de fichas técnicas en la oferta. |
| **CONTRADICTORIO** | 1 | 1.47 % | Datos incompatibles entre cotización y especificación de silicio. |

### Hallazgos Críticos:
1. **Omisión del Ítem 9 (Sensor Telúrico):** El postor cotizó únicamente 8 ítems, omitiendo por completo el acelerómetro ADXL345 (±16g) y el geófono de 4.5 Hz.
2. **Incompatibilidad en Router (Teltonika RUT951):** Carece de interfaz USB 2.0 y requiere alimentación de 9V a 30V DC (las bases solicitaban USB 2.0 y 3.3V-4.3V).
3. **Discrepancia en Luminancia (TSL2591):** La cotización consigna características del sensor desfasado TSL2561 (tope en 40,000 lux y 3 direcciones I2C), el cual saturará ante radiación solar directa (las bases exigen 88,000 lux).
4. **Sensor de Radiación (DFRobot SEN0463):** No cuenta con interfaz USB Serial ni conector USB; entrega pulsos digitales en conector Gravity de 3 pines.
5. **Carencia de Fuentes y Accesorios:** Faltan fuentes de 5V reguladas, cable conector propietario JST ZHR-5 para sensor SPS30 y adaptadores de nivel lógico 3.3V/5V.

**Dictamen Técnico:** **NO FAVORABLE (NO APTO PARA APROBACIÓN EN SU ESTADO ACTUAL)** hasta que el postor subsane formalmente las omisiones y garantice los accesorios indispensables.

---

## 💻 Arquitectura de Software y Dashboard

La especificación técnica ([`informe/02_especificacion_tecnica_desarrollo.md`](informe/02_especificacion_tecnica_desarrollo.md)) detalla:

- **Nodo Sensor IoT:** Firmware modular para Arduino Nano 33 IoT (ATSAMD21G18A a 48 MHz) con adquisición concurrente I2C, I2S y GPIO con interrupciones.
- **Protocolo de Telemetría:** Mensajería JSON optimizada sobre MQTT con cifrado TLS v1.3.
- **Base de Datos:** PostgreSQL 16 con extensión TimescaleDB (hipertarimas particionadas cada 7 días para telemetría ambiental y compresión automática).
- **Backend y API:** Microservicio en FastAPI con autenticación JWT, RBAC y WebSockets para tiempo real.
- **Dashboard Web:** Interfaz SPA responsiva en React + TypeScript + Vite con indicadores de calidad de aire (PM2.5/PM10), ruido (dBA Leq), temperatura, humedad, luminancia, radiación y lluvia.
- **Arquitectura Evolutiva para Cámaras e IA:** Módulo perimetral de inferencia (YOLOv8) que publica metadatos ligeros de aforo/intrusión sin sobrecargar la base de datos de sensores con vídeo continuo.

---

## 🛠️ Tecnologías Empleadas

![C++](https://img.shields.io/badge/Firmware-Arduino%20C%2B%2B-00979D?logo=arduino&logoColor=white)
![Python](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python-009688?logo=fastapi&logoColor=white)
![TimescaleDB](https://img.shields.io/badge/Database-TimescaleDB%20%7C%20PostgreSQL-336791?logo=postgresql&logoColor=white)
![React](https://img.shields.io/badge/Frontend-React%20%7C%20TypeScript-61DAFB?logo=react&logoColor=black)
![MQTT](https://img.shields.io/badge/Telemetry-MQTT%20TLS-660066?logo=eclipsemosquitto&logoColor=white)
![OpenWrt](https://img.shields.io/badge/Gateway-Teltonika%20RutOS-005490?logo=openwrt&logoColor=white)