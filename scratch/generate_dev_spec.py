# -*- coding: utf-8 -*-
"""
Script to generate informe/02_especificacion_tecnica_desarrollo.md
"""
import os

def generate_spec():
    doc_lines = []

    doc_lines.append("""# ESPECIFICACIÓN TÉCNICA Y GUÍA DE DESARROLLO DEL SISTEMA DE MONITOREO IoT

**Proyecto:** Plataforma Integral de Telemetría Ambiental, Gestión de Eventos y Dashboard Web  
**Entidad:** Universidad Nacional de San Agustín de Arequipa (UNSA)  
**Propósito:** Proveer la base arquitectónica, diseño de datos, protocolos y flujos de integración de software a partir del inventario de hardware evaluado, asegurando la escalabilidad hacia visión artificial y cámaras.  
**Estado:** Especificación Preliminar condicionada a la validación de hardware  
**Fecha:** 19 de Octubre de 2026  

---

## 1. Introducción y Enfoque de Ingeniería

Este documento técnico está dirigido al equipo de desarrollo de software (ingenieros de firmware, desarrolladores backend, ingenieros de datos y desarrolladores frontend). Su finalidad es definir con precisión la arquitectura de software, el diseño de la base de datos, los flujos de adquisición y las interfaces de usuario para el sistema de monitoreo.

> [!IMPORTANT]
> **Aislamiento Técnico:** Esta especificación se fundamenta en las capacidades técnicas reales comprobables de los equipos analizados. Las características no verificadas o pendientes de subsanación por el proveedor se identifican explícitamente como **[PENDIENTE DE CONFIRMACIÓN]** para evitar que los programadores implementen lógica basada en suposiciones no respaldadas por hardware.

---

## 2. Inventario Técnico Orientado al Software

A continuación se detalla el perfil de integración de cada dispositivo físico del sistema:

### 2.1 Microcontrolador / Controlador Nodo: Arduino Nano 33 IoT (ABX00027)
- **Fabricante:** Arduino S.r.l. / Microchip / u-blox.
- **Modelo Exacto:** Arduino Nano 33 IoT (SKU ABX00027).
- **Procesador y Memoria:** ATSAMD21G18A (ARM Cortex-M0+ a 48 MHz, 256 KB Flash, 32 KB SRAM).
- **Coprocesador Inalámbrico:** u-blox NINA-W102 (ESP32) con firmware WiFiNINA.
- **Chip Criptográfico:** Microchip ATECC608A (almacenamiento de claves privadas y aceleración SHA-256 / ECC).
- **Sensor Inercial Integrado (IMU):** LSM6DS3 (acelerómetro y giroscopio de 6 ejes) en bus I2C interno (dirección `0x6A`).
- **Interfaces Físicas Utilizadas:**
  - I2C (Wire) en pines A4 (SDA) y A5 (SCL) a 100 kHz.
  - I2S (reloj de bits SCK, selector de palabra WS, datos serie SD) para micrófono INMP441.
  - GPIOs con Interrupción Externa (EINT) para sensor de pulsos de radiación SEN0463 y balancín pluviométrico RK400-04.
  - UART Hardware (`Serial1`) en D0 (RX) y D1 (TX) a 115200 bps (disponible para SPS30 si se usa modo UART).
- **Protocolos de Salida del Nodo:** MQTT sobre TLS (puerto 8883) o HTTPS POST (puerto 443) mediante Wi-Fi 802.11 b/g/n.
- **Formato de Payload Generado:** Tramas JSON codificadas en UTF-8 con marcas de tiempo relativas (milisegundos desde arranque) e identificación de hardware única (MAC address / Serial number).
- **Dependencias de Software / Librerías Firmware:** `WiFiNINA.h`, `ArduinoMqttClient.h`, `Arduino_JSON.h`, `Wire.h`, `SensirionI2CSps30.h`, `SensirionI2CSht4x.h`, `Adafruit_TSL2591.h`, `I2S.h` / `ArduinoSound.h`.
- **Estado de Integración:** CONFIRMADO en arquitectura base; PENDIENTE DE VALIDACIÓN en coexistencia de I2S + Wi-Fi en 32 KB de SRAM.

### 2.2 Dispositivo de Red / Gateway Celular: Teltonika RUT951
- **Fabricante:** Teltonika Networks.
- **Modelo Exacto:** RUT951 (Variante estándar 4G LTE Cat 4 con Wi-Fi y 4x RJ45).
- **Rol en la Arquitectura:** Enrutador de acceso local (Access Point Wi-Fi) y Gateway de enlace ascendente celular hacia Internet/Nube.
- **Dirección de Comunicación:** Bidireccional (Wi-Fi AP local para el Arduino, túnel WAN LTE para reenvío al servidor).
- **Funcionalidad de Software en el Gateway:**
  - Modo AP Wi-Fi WPA2/WPA3 Personal (SSID local aislado para el nodo sensor).
  - Broker MQTT local embebido (Mosquitto en RutOS) opcional para actuar como buffer de borde (edge broker) o retransmisor hacia el broker central en nube.
  - Soporte de cliente NTP para sincronización de tiempo de red en la LAN.
  - Cortafuegos con bloqueo de tráfico entrante no solicitado desde la red celular.
- **Estado de Integración:** CONFIRMADO en conectividad inalámbrica IP; NO DISPONE DE ENLACE USB.

### 2.3 Sensor de Calidad de Aire (Material Particulado): Sensirion SPS30
- **Fabricante:** Sensirion AG.
- **Modelo Exacto:** SPS30 (Particulate Matter Sensor).
- **Magnitudes Medidas:**
  - Concentración en masa: PM1.0, PM2.5, PM4.0, PM10 en microgramos por metro cúbico ($\mu g/m^3$).
  - Concentración en número: PM0.5, PM1.0, PM2.5, PM4.0, PM10 en partículas por centímetro cúbico ($\#/cm^3$).
  - Tamaño de partícula típico (TPS) en micrómetros ($\mu m$).
- **Rango y Precisión:** 0 a 1000 $\mu g/m^3$; precisión para PM1/PM2.5 de $\pm 10\%$ del valor medido (en 100-1000 $\mu g/m^3$) y $\pm 5\,\mu g/m^3$ (en 0-100 $\mu g/m^3$).
- **Frecuencia de Actualización:** 1 Hz (1 medición por segundo).
- **Interfaz y Protocolo:**
  - Opción recomendada: I2C a 100 kHz en dirección `0x69`. Comandos con CRC-8 ($P(x) = x^8 + x^5 + x^4 + 1$).
  - Opción alternativa: UART a 115200 bps con protocolo SHDLC (tramas delimitadas por `0x7E` con byte-stuffing y suma de comprobación invertida).
- **Registros de Diagnóstico Interno:** Lectura del registro de estado de 32 bits (alertas de velocidad de ventilador bloqueado `FAN`, fallo de láser `LASER` y velocidad fuera de rango `SPEED`).
- **Mantenimiento por Software:** Ejecución semanal automática de ciclo de autolimpieza de ventilador (10 segundos a máxima velocidad).
- **Estado de Integración:** CONFIRMADO documentalmente; PENDIENTE DE PROVEER cable conector micro JST ZHR-5 y alimentación externa de 5V.

### 2.4 Sensor de Luminancia: TSL2591 / [PENDIENTE CONFIRMACIÓN TSL2561]
- **Fabricante:** ams-OSRAM.
- **Modelo Solicitado:** TSL2591 (Light-to-Digital Converter).
- **Magnitudes Medidas:** Iluminancia en Lux ($lx$), conteos de luz de espectro completo (Canal 0: visible + infrarrojo) y conteos infrarrojos puros (Canal 1: IR).
- **Rango:** 188 $\mu lx$ a 88,000 $lx$ con rango dinámico de $600,000,000:1$ (si se confirma TSL2591). Si el proveedor entrega TSL2561, el rango quedará limitado a 0.1 - 40,000 $lx$.
- **Resolución:** ADC de 16 bits de doble canal.
- **Interfaz y Protocolo:** I2C estándar (dirección `0x29` fija en TSL2591; configurable `0x29`/`0x39`/`0x49` en TSL2561).
- **Algoritmo de Conversión:**
  $$Lux = \frac{(C_0 - 1.64 \times C_1)}{Gain \times \frac{T_{int}}{100\,ms}} \times C_{factor}$$
  *(Los coeficientes exactos dependen de la curva espectral y deben ajustarse en firmware mediante calibración empírica).*
- **Estado de Integración:** PENDIENTE DE CONFIRMACIÓN del modelo exacto entregado por SERCIA.

### 2.5 Sensor de Radiación Ionizante: DFRobot SEN0463
- **Fabricante:** DFRobot.
- **Modelo Exacto:** SEN0463 (Gravity Geiger Counter Module con tubo M4011).
- **Magnitud Medida:** Tasa de dosis equivalente ambiental de radiación en microSieverts por hora ($\mu Sv/h$) y Cuentas Por Minuto (CPM).
- **Rango:** 0.08 a 1200 $\mu Sv/h$ (valor teórico máximo).
- **Sensibilidad de Fábrica:** $153.8\,CPM / (\mu Sv/h)$ bajo fuente de referencia Cesio-137 ($^{137}Cs$) o Cobalto-60 ($^{60}Co$). Fondo natural típico: $\approx 25\,CPM \approx 0.16\,\mu Sv/h$.
- **Interfaz y Protocolo de Software:** Salida de pulsos digitales TTL activos en bajo (Active-Low) en el pin `D` del conector Gravity.
- **Mecanismo de Integración en Microcontrolador:**
  - Configuración de interrupción externa en flanco de bajada (`FALLING`) en un pin digital del SAMD21 (ej. Pin D4).
  - Rutina de Servicio de Interrupción (ISR) atómica que incrementa un contador volátil: `volatile unsigned long pulse_count;`
  - Algoritmo en bucle principal: muestreo acumulativo en ventana de 60 segundos para cálculo de CPM y conversión:
    $$\text{Tasa Dosis } (\mu Sv/h) = \frac{CPM_{60s}}{153.8}$$
- **Estado de Integración:** CONFIRMADO en modo interrupción digital GPIO. NO DISPONE DE INTERFAZ USB SERIAL.

### 2.6 Sensor de Ruido Acústico: INMP441
- **Fabricante:** TDK InvenSense.
- **Modelo Exacto:** INMP441 (Omnidirectional Microphone with I2S Digital Output).
- **Magnitud Adquirida:** Señal digital de presión acústica instantánea en formato PCM lineal de 24 bits complemento a dos.
- **Interfaz Física:** Bus I2S (Inter-IC Sound):
  - `SCK` (Serial Clock): Generado por el SAMD21.
  - `WS` (Word Select / LRCLK): Selección de canal izquierdo/derecho (conectar pin L/R a GND para canal izquierdo).
  - `SD` (Serial Data): Entrada de datos de audio.
- **Frecuencia de Muestreo de Audio recomendada:** $f_s = 16,000\,Hz$ o $32,000\,Hz$.
- **Procesamiento de Señal en Software para Sonometría:**
  1. Captura de bloque de muestras PCM (ej. 512 a 1024 muestras mediante DMA).
  2. Aplicación de filtro digital de ponderación A (IIR filter acorde a IEC 61672-1:2013).
  3. Cálculo del valor cuadrático medio (RMS):
     $$V_{RMS} = \sqrt{\frac{1}{N}\sum_{i=1}^{N} x_A[i]^2}$$
  4. Conversión a Nivel de Presión Sonora equivalente ($L_{Aeq, T}$) en dBA:
     $$L_{Aeq} = 20 \log_{10}\left(\frac{V_{RMS}}{V_{ref}}\right) + C_{calib}$$
     *(Donde $C_{calib}$ es el factor de ajuste calibrado con sonómetro patrón).*
- **Estado de Integración:** CONFIRMADO por bus I2S; exige desarrollo de algoritmo DSP en firmware y validación de carga de CPU.

### 2.7 Sensor de Temperatura y Humedad Ambiental: Sensirion SHT45
- **Fabricante:** Sensirion AG.
- **Modelo Exacto:** SHT45 (SHT45-AD1B).
- **Magnitudes Medidas:** Temperatura del aire en grados Celsius ($^\circ C$) y Humedad Relativa del aire en porcentaje ($\%RH$).
- **Rango y Precisión:** $-40^\circ C$ a $+125^\circ C$ ($\pm 0.1^\circ C$ típica); $0$ a $100\% RH$ ($\pm 1.0\% RH$ típica).
- **Interfaz y Protocolo:** I2C estándar hasta Fast Mode Plus (1 MHz) en dirección `0x44`. Comandos de 8 bits con respuesta de 6 bytes:
  `[T_MSB][T_LSB][CRC_T][RH_MSB][RH_LSB][CRC_RH]`.
- **Fórmulas de Conversión Oficiales Sensirion:**
  $$T\,(^\circ C) = -45 + 175 \times \frac{S_T}{2^{16} - 1}$$
  $$RH\,(\%RH) = -6 + 125 \times \frac{S_{RH}}{2^{16} - 1}$$
  *(Con acotamiento por software de $RH$ al intervalo $[0, 100]$).*
- **Estado de Integración:** CONFIRMADO a nivel de protocolo; PENDIENTE DE CONFIRMACIÓN de que el proveedor entregue módulo con pines soldados.

### 2.8 Sensor Pluviómetro: Rika Sensors RK400-04
- **Fabricante:** Hunan Rika Electronic Technology Co., Ltd.
- **Modelo:** RK400-04 (Tipping Bucket Rain Gauge).
- **Magnitudes Medidas:** Precipitación acumulada en milímetros ($mm$) e Intensidad de precipitación en milímetros por hora ($mm/h$).
- **Resolución:** $0.2\,mm$ de lluvia por cada oscilación del balancín.
- **Interfaz Física:** Contacto seco tipo reed switch normalmente abierto.
- **Mecanismo de Integración en Microcontrolador:**
  - Conexión a pin digital con interrupción (`FALLING`) y resistencia pull-up externa de 10 kΩ conectada a 3.3V.
  - Filtro antirrebote por software (*debounce time* de 80 ms) para descartar falsas conmutaciones producidas por oscilación mecánica del balancín:
    $$\text{Precipitación Acumulada } (mm) = N_{pulsos} \times 0.2\,mm$$
- **Estado de Integración:** CONFIRMADO en modo pulso pasivo; PENDIENTE DE CONFIRMAR longitud de cable y variante suministrada.

### 2.9 Sensor Telúrico (Acelerómetro ADXL345 + Geófono): [OMITIDO EN PROPUESTA]
- **Estado:** NO DISPONIBLE EN EL HARDWARE ACTUAL COTIZADO.
- **Diseño Arquitectónico para Futura Inclusión:**
  - Acelerómetro ADXL345: I2C (dirección `0x53`) con FIFO interno para muestreo de vibraciones a 100-400 Hz.
  - Geófono de 4.5 Hz: Requiere circuito de amplificación previa (amplificador instrumental diferencial) antes de ingresar al convertidor ADC de 12 bits del SAMD21.
  - El software de base de datos y backend contemplará las tablas correspondientes para que su incorporación no requiera reescribir el sistema.

---

## 3. Flujo Integral de Datos

El flujo de información técnica recorre una cadena desde el fenómeno físico hasta la interfaz gráfica de usuario:

```mermaid
flowchart TD
    subgraph SENSORES["Instrumentación y Transductores"]
        S1["SPS30 (Calidad Aire)<br/>I2C 0x69 / 5V"]
        S2["TSL2591 (Luminancia)<br/>I2C 0x29 / 3.3V"]
        S3["SEN0463 (Radiación)<br/>Pulsos D / ISR / 3.3V-5V"]
        S4["INMP441 (Ruido)<br/>I2S Audio 24-bit / 3.3V"]
        S5["SHT45 (Temp/Hum)<br/>I2C 0x44 / 3.3V"]
        S6["RK400-04 (Lluvia)<br/>Reed Switch Pulso / 3.3V"]
        S7["ADXL345 + Geófono<br/>[PENDIENTE DE COMPRA]"]
    end

    subgraph ADQUISICION["Nodo Controlador de Borde"]
        MCU["Arduino Nano 33 IoT<br/>SAMD21G18A (48MHz, 32KB RAM)<br/>Muestreo, Filtrado, DSP y JSON"]
        CRIPTO["ATECC608A<br/>Claves TLS Hardware"]
        RADIO["u-blox NINA-W102<br/>Cliente Wi-Fi 802.11 b/g/n"]
        MCU --- CRIPTO
        MCU --- RADIO
    end

    subgraph GATEWAY["Enlace y Comunicaciones"]
        RUT["Teltonika RUT951<br/>AP Wi-Fi Local (192.168.1.1)<br/>Módem 4G LTE Cat 4 (Failover Dual SIM)"]
    end

    subgraph BACKEND["Infraestructura Servidor / Nube"]
        BROKER["Broker MQTT (EMQX / Mosquitto)<br/>TLS v1.3 Puerto 8883"]
        INGEST["Servicio Ingestion IoT (FastAPI / Node.js)<br/>Validación, Deduplicación y Alarmas"]
        TSDB[("Base de Datos Relacional y Temporal<br/>PostgreSQL 16 + TimescaleDB")]
        API["API RESTful / WebSocket<br/>Autenticación JWT / RBAC"]
    end

    subgraph DASHBOARD["Visualización y Clientes"]
        WEB["Dashboard Web SPA<br/>(React / TypeScript / Vite)<br/>Gráficos, KPIs, Mapas y Alertas"]
        MOB["Acceso Móvil Responsive"]
    end

    S1 -->|I2C 100kHz| MCU
    S2 -->|I2C 100kHz| MCU
    S3 -->|Pulso Digital GPIO| MCU
    S4 -->|I2S PCM Audio| MCU
    S5 -->|I2C 100kHz| MCU
    S6 -->|Pulso Digital GPIO| MCU
    S7 -.->|Pendiente Hardware| MCU

    RADIO -->|Wi-Fi 2.4GHz Local| RUT
    RUT -->|Túnel 4G LTE Internet| BROKER
    BROKER --> INGEST
    INGEST --> TSDB
    TSDB --> API
    API -->|HTTPS / WSS| WEB
    API -->|HTTPS / WSS| MOB
```

### 3.1 Secuencia de Adquisición y Transmisión de Datos
El siguiente diagrama describe la cronología de eventos durante un ciclo regular de muestreo y envío de telemetría:

```mermaid
sequenceDiagram
    autonumber
    participant Sensores as Sensores (I2C / GPIO / I2S)
    participant SAMD as Arduino SAMD21 (Firmware)
    participant NINA as Módulo u-blox NINA (Wi-Fi)
    participant Router as Teltonika RUT951 (LTE)
    participant Broker as Broker MQTT (Servidor)
    participant DB as PostgreSQL / TimescaleDB
    participant Dash as Dashboard Web

    loop Ciclo de Muestreo (Cada 5 a 60 segundos)
        SAMD->>Sensores: Solicitud lectura I2C (SHT45, TSL2591, SPS30)
        Sensores-->>SAMD: Retorno de bytes crudos con CRC
        SAMD->>SAMD: Verificación CRC y conversión matemática de unidades
        Note over SAMD: Lectura atómica de pulsos acumulados (Radiación y Pluviómetro)
        Note over SAMD: Cálculo de RMS dBA a partir de muestras I2S (INMP441)
        SAMD->>SAMD: Ensamble de trama JSON estructurada
        SAMD->>NINA: Envío de payload JSON por SPI interno
        NINA->>Router: Transmisión TCP/IP por Wi-Fi WPA2
        Router->>Broker: Reenvío celular 4G LTE por socket seguro TLS
        Broker->>DB: Inserción de mediciones con marca de tiempo UTC
        Broker->>Dash: Notificación instantánea vía WebSocket
        Dash->>Dash: Actualización de medidores y gráficos en tiempo real
    end
```

---

## 4. Requisitos de Integración y Procesamiento de Datos

### 4.1 Formato Estándar de Payload de Telemetría (JSON)
El nodo sensor publicará en el topic MQTT `unsa/monitoreo/{device_id}/telemetry` el siguiente objeto estructurado:

```json
{
  "device_id": "UNSA-NODE-01",
  "timestamp": 1729340000,
  "uptime_ms": 3600000,
  "metrics": {
    "temperature_c": 21.45,
    "humidity_rh": 48.2,
    "luminance_lux": 542.1,
    "pm1_0_ugm3": 12.3,
    "pm2_5_ugm3": 18.7,
    "pm4_0_ugm3": 24.1,
    "pm10_0_ugm3": 31.5,
    "radiation_usvh": 0.14,
    "radiation_cpm": 22,
    "noise_dba": 46.8,
    "rain_rate_mmh": 0.0,
    "rain_accum_mm": 2.4
  },
  "diagnostics": {
    "wifi_rssi_dbm": -58,
    "sps30_fan_ok": true,
    "sht45_crc_errors": 0,
    "free_memory_bytes": 14280
  }
}
```

### 4.2 Políticas de Integración y Robustez de Software
1. **Validación de Integridad Metrológica:** Cada medición debe ser verificada antes de almacenarse:
   - Rango físico admisible (ej. $-40 \le T \le 85$, $0 \le RH \le 100$, $0 \le PM \le 1000$, $Luminancia \ge 0$).
   - Descarte de valores fuera de rango o registros de error en el hardware (p. ej. banderas `NaN` o códigos `0xFFFF`).
2. **Tratamiento ante Pérdida de Conexión de Red:**
   - Si la red celular o el enlace Wi-Fi cae, el Arduino Nano 33 IoT conservará hasta un máximo de 50 lecturas en un buffer circular en SRAM (debido a la limitación de 32 KB).
   - Opcionalmente, se configurará el router Teltonika RUT951 como receptor local en LAN (mediante un microservicio o almacenamiento en pendrive si tuviera soporte, o buffer en memoria de RutOS) para retener datos pendientes de transmisión hacia la nube.
3. **Manejo de Duplicados e Identificación:** Cada mensaje contiene `device_id` y `timestamp` (o secuencia numérica incremental). La base de datos implementa restricciones `PRIMARY KEY (device_id, recorded_at)` con política `ON CONFLICT DO NOTHING`.

---

## 5. Diseño Preliminar de la Base de Datos

Se propone un diseño relacional enriquecido con optimizaciones de series temporales (PostgreSQL 16 con extensión TimescaleDB), garantizando alta velocidad de ingesta, compresión automática y consultas históricas instantáneas.

### 5.1 Diagrama Entidad-Relación

```mermaid
erDiagram
    LOCATIONS ||--o{ DEVICES : alberga
    DEVICES ||--o{ MEASUREMENTS : genera
    DEVICES ||--o{ DEVICE_STATUS : reporta
    DEVICES ||--o{ ALERTS : dispara
    USERS ||--o{ USER_ROLES : asignado
    ROLES ||--o{ USER_ROLES : define
    DEVICES ||--o{ CAMERA_EVENTS : vincula

    LOCATIONS {
        uuid id PK
        string name
        string building
        string floor
        string room
        geometry coordinates
    }

    DEVICES {
        string id PK
        string serial_number
        string model
        uuid location_id FK
        string mac_address
        string firmware_version
        boolean is_active
        timestamp created_at
    }

    MEASUREMENTS {
        timestamp recorded_at PK
        string device_id PK
        float temperature_c
        float humidity_rh
        float luminance_lux
        float pm1_0
        float pm2_5
        float pm4_0
        float pm10_0
        float radiation_usvh
        float noise_dba
        float rain_rate_mmh
        float rain_accum_mm
    }

    DEVICE_STATUS {
        timestamp recorded_at PK
        string device_id PK
        int wifi_rssi
        int free_memory
        boolean fan_status
        string connection_mode
    }

    ALERTS {
        uuid id PK
        string device_id FK
        timestamp triggered_at
        string severity
        string parameter_name
        float value_recorded
        float threshold_limit
        boolean is_resolved
        timestamp resolved_at
    }

    CAMERA_EVENTS {
        uuid id PK
        string camera_id
        uuid location_id FK
        timestamp event_time
        string event_type
        int people_count
        float confidence
        jsonb metadata
    }
```

### 5.2 Esquema Físico SQL (PostgreSQL / TimescaleDB)

```sql
-- Habilitar extensión para series temporales y UUIDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "timescaledb";

-- Tabla de Ubicaciones
CREATE TABLE locations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    building VARCHAR(100) NOT NULL,
    floor VARCHAR(20) NOT NULL,
    room VARCHAR(50),
    latitude NUMERIC(10, 7),
    longitude NUMERIC(10, 7),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla de Dispositivos (Inventario y Hardware)
CREATE TABLE devices (
    id VARCHAR(50) PRIMARY KEY, -- ej: 'UNSA-NODE-01'
    serial_number VARCHAR(100),
    model VARCHAR(100) NOT NULL,
    location_id UUID REFERENCES locations(id) ON DELETE SET NULL,
    mac_address MACADDR,
    firmware_version VARCHAR(30),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla de Mediciones de Sensores (Hipertarima de TimescaleDB)
CREATE TABLE measurements (
    recorded_at TIMESTAMPTZ NOT NULL,
    device_id VARCHAR(50) NOT NULL REFERENCES devices(id),
    temperature_c NUMERIC(5, 2),
    humidity_rh NUMERIC(5, 2),
    luminance_lux NUMERIC(8, 2),
    pm1_0 NUMERIC(6, 2),
    pm2_5 NUMERIC(6, 2),
    pm4_0 NUMERIC(6, 2),
    pm10_0 NUMERIC(6, 2),
    radiation_usvh NUMERIC(8, 4),
    noise_dba NUMERIC(5, 2),
    rain_rate_mmh NUMERIC(6, 2),
    rain_accum_mm NUMERIC(8, 2),
    PRIMARY KEY (recorded_at, device_id)
);

-- Conversión a Hipertarima con partición por tiempo (intervalos de 7 días)
SELECT create_hypertable('measurements', 'recorded_at', chunk_time_interval => INTERVAL '7 days');

-- Índices de consulta rápida
CREATE INDEX idx_measurements_device_time ON measurements (device_id, recorded_at DESC);

-- Tabla de Estado y Conectividad (Liveness & Health)
CREATE TABLE device_status (
    recorded_at TIMESTAMPTZ NOT NULL,
    device_id VARCHAR(50) NOT NULL REFERENCES devices(id),
    wifi_rssi_dbm SMALLINT,
    free_memory_bytes INTEGER,
    sps30_fan_ok BOOLEAN DEFAULT TRUE,
    connection_mode VARCHAR(20) DEFAULT 'WIFI_4G',
    PRIMARY KEY (recorded_at, device_id)
);
SELECT create_hypertable('device_status', 'recorded_at', chunk_time_interval => INTERVAL '7 days');

-- Tabla de Registro de Alertas
CREATE TABLE alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    device_id VARCHAR(50) NOT NULL REFERENCES devices(id),
    triggered_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    severity VARCHAR(20) NOT NULL CHECK (severity IN ('INFO', 'WARNING', 'CRITICAL')),
    parameter_name VARCHAR(50) NOT NULL,
    value_recorded NUMERIC(10, 3) NOT NULL,
    threshold_limit NUMERIC(10, 3) NOT NULL,
    message TEXT,
    is_resolved BOOLEAN DEFAULT FALSE,
    resolved_at TIMESTAMPTZ,
    resolved_by VARCHAR(100)
);
CREATE INDEX idx_alerts_active ON alerts (is_resolved, triggered_at DESC);

-- Tabla de Eventos de Visión Artificial (Cámaras Futuras)
CREATE TABLE camera_events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    camera_id VARCHAR(50) NOT NULL,
    location_id UUID REFERENCES locations(id),
    event_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    event_type VARCHAR(50) NOT NULL, -- 'PEOPLE_COUNT', 'INTRUSION', 'SMOKE_DETECTED'
    people_count INTEGER DEFAULT 0,
    confidence_score NUMERIC(4, 3), -- ej: 0.945
    metadata JSONB -- Guarda coordenadas de bounding box, zona, etc.
);
SELECT create_hypertable('camera_events', 'event_time', chunk_time_interval => INTERVAL '15 days');
```

### 5.3 Estimación de Almacenamiento y Capacidad
- **Frecuencia de Muestreo Prevista:** 1 registro de telemetría cada 30 segundos por nodo ($120\,\text{registros/hora} = 2,880\,\text{registros/día}$).
- **Tamaño de Fila en Disco:** $\approx 120\,\text{bytes}$ por registro.
- **Volumen Estimado por Nodo:**
  - Por día: $\approx 345\,\text{KB/día}$.
  - Por año (sin comprimir): $\approx 126\,\text{MB/año}$ por nodo.
  - Con compresión nativa TimescaleDB ($90\%$ de ratio de compresión): $\approx 15\,\text{MB/año}$ por nodo.
- **Conclusión de Infraestructura:** El volumen de telemetría ambiental es extremadamente ligero y puede ser soportado con holgura durante décadas en cualquier servidor básico o VPS en la nube.

---

## 6. Dashboard Online e Indicadores de Visualización

En la siguiente tabla se definen los indicadores visuales construibles a partir de los sensores efectivamente cotizados:

| Indicador | Variable de Origen | Unidad | Frecuencia de Actualización | Tipo de Visualización | Umbrales / Rangos Referenciales | Condición de Alerta | Histórico Requerido |
|---|---|---|---|---|---|---|---|
| **Calidad de Aire (PM2.5)** | `pm2_5` (SPS30) | $\mu g/m^3$ | 5 a 30 s | Tacómetro numérico y gráfico temporal continuo | 0-15: Buena<br>15-35: Moderada<br>>35: Nociva (ECA Perú / OMS) | Alerta si $>35\,\mu g/m^3$ durante más de 15 min | 24 horas y 30 días móviles |
| **Material Particulado (PM10)** | `pm10_0` (SPS30) | $\mu g/m^3$ | 5 a 30 s | Gráfico de barras / área apilada | 0-50: Buena<br>50-100: Moderada<br>>100: Mala | Alerta si $>100\,\mu g/m^3$ | 24 horas y 30 días |
| **Temperatura Ambiental** | `temperature_c` (SHT45) | $^\circ C$ | 5 a 30 s | Valor numérico instantáneo y línea de tendencia | Rango confort: $18^\circ C$ a $26^\circ C$ | Alerta si $<10^\circ C$ o $>35^\circ C$ | 7 días y estacional |
| **Humedad Relativa** | `humidity_rh` (SHT45) | $\%RH$ | 5 a 30 s | Gráfico radial / higrómetro | Rango normal: $30\%$ a $70\% RH$ | Alerta si $>85\% RH$ (riesgo condensación) | 7 días |
| **Luminancia Ambiental** | `luminance_lux` (TSL2591) | $lx$ | 5 a 30 s | Tarjeta KPI con gradiente de color | 0-100: Penumbra<br>100-500: Oficina<br>>1000: Luz día | Alerta por iluminación insuficiente en horario laboral | 24 horas |
| **Nivel de Ruido Ambiental** | `noise_dba` (INMP441) | $dBA$ | 1 a 5 s | Gráfico de ondas / Nivel sonoro equivalente | 0-50: Silencioso<br>50-70: Moderado<br>>70: Ruidoso (ECA Ruido) | Alerta si $L_{Aeq} > 75\,dBA$ sostenido | 8 horas (dosis acústica) |
| **Tasa de Dosis de Radiación** | `radiation_usvh` (SEN0463) | $\mu Sv/h$ | 30 a 60 s | Tacómetro de seguridad y conteo CPM | Normal natural: $0.08$ a $0.25\,\mu Sv/h$ | Alerta preventiva si $>0.5\,\mu Sv/h$ | 30 días y 1 año acumulado |
| **Intensidad de Precipitación** | `rain_rate_mmh` (RK400-04) | $mm/h$ | En evento / 1 min | Histograma pluviométrico | 0-2: Débil<br>2-15: Moderada<br>>15: Torrencial | Alerta inmediata ante inicio de evento de lluvia | 30 días y anual acumulado |
| **Salud y Enlace del Nodo** | `wifi_rssi_dbm` / `status` | $dBm$ / estado | 30 s | Semáforo de estado (Online/Offline) | RSSI $>-70\,dBm$: Óptimo<br>$<-85\,dBm$: Crítico | Alerta por desconexión mayor a 3 minutos | 30 días de disponibilidad |

---

## 7. Evaluación Comparativa de Tecnologías de Software

Para la implementación del backend, la base de datos y la interfaz de usuario, se analizaron tres alternativas tecnológicas:

| Criterio de Selección | Alternativa A: Grafana + InfluxDB / Telegraf | Alternativa B: React + TypeScript + FastAPI + PostgreSQL (TimescaleDB) | Alternativa C: ThingsBoard Community Edition |
|---|---|---|---|
| **Compatibilidad con Protocolos Reales** | Alta (mediante Telegraf o Mosquitto hacia BD). | Total (FastAPI procesa endpoints REST, WebSockets y consumidor MQTT). | Total (soporte nativo de broker MQTT, CoAP y HTTP integrado). |
| **Complejidad de Implementación** | **Muy Baja:** Despliegue mediante contenedores Docker listos para usar. | **Media-Alta:** Requiere programar frontend, backend, autenticación y API desde cero. | **Media:** Plataforma lista con panel web, pero requiere dominar su motor de reglas y widgets. |
| **Tiempo Estimado de Desarrollo** | **Inmediato:** 1 a 2 semanas para paneles operativos. | **Extenso:** 8 a 12 semanas de desarrollo de software a medida. | **Rápido:** 3 a 4 semanas para configuración y diseño de dashboards. |
| **Personalización de la Interfaz (UI/UX)** | Limitada a las plantillas y paneles predefinidos de Grafana. | **Máxima:** Diseño corporativo a medida de la UNSA, adaptable a cualquier dispositivo. | Media: Tableros configurables con widgets personalizables en JavaScript/Vue. |
| **Gestión de Dispositivos y Aprovisionamiento**| Inexistente (requiere configuración manual externa de bases de datos). | Personalizada (diseño a medida de tablas de dispositivos y ubicaciones). | **Excelente:** Gestión nativa de perfiles de dispositivos, credenciales y telemetría. |
| **Motor de Alertas y Notificaciones** | Integrado en Grafana (Email, Telegram, Webhooks). | Programable a medida (integración con WhatsApp API, Email, WebPush). | **Avanzado:** Motor de reglas gráfico (Rule Engine) con soporte de eventos y alarmas. |
| **Actualización en Tiempo Real** | Sondeo (Polling) periódico o streaming mediante Grafana Live. | Tiempo real nativo mediante WebSockets bidireccionales. | Tiempo real nativo por WebSockets y suscripciones MQTT. |
| **Integración Futura de Cámaras e IA** | Difícil (Grafana no está concebida para streaming de vídeo ni metadatos de visión). | **Ideal:** Capacidad total de incrustar flujos HLS/WebRTC y renderizar eventos de visión artificial. | Moderada (requiere plugins específicos o servicios complementarios). |
| **Costos Operativos y Licenciamiento** | Software Libre (Apache 2.0 / AGPL). Infraestructura ligera. | Software Libre (MIT / BSD). Infraestructura ligera y escalable. | Edición Community libre (Apache 2.0). Demanda mayor consumo de RAM (Java/Postgres). |

### Recomendación Técnica Condicionada
1. **Fase Inmediata (Prototipo y Validación Rápida):**  
   Implementar la **Alternativa C (ThingsBoard Community Edition)** o **Alternativa A (Grafana + PostgreSQL/TimescaleDB)**. Esto permitirá tener el sistema recibiendo telemetría y visualizando datos en menos de dos semanas tan pronto lleguen los equipos, sin incurrir en meses de programación de frontend básico.
2. **Fase Definitiva y Evolutiva (Sistema Institucional UNSA con Cámaras e IA):**  
   Desarrollar la **Alternativa B (Frontend React/Vite + Backend FastAPI + PostgreSQL con TimescaleDB)**. Esta arquitectura otorga control absoluto sobre el código fuente, permite integrar analítica de visión artificial sobre flujos de vídeo de cámaras sin depender de plataformas de terceros, y garantiza una interfaz institucional personalizada para la universidad.

---

## 8. Arquitectura Evolutiva para la Integración Futura de Cámaras y Visión Artificial

Aunque las cámaras no forman parte de la adquisición actual, el sistema debe estar preparado arquitectónicamente para su adhesión sin requerir cambios estructurales en el backend ni en la base de datos:

```mermaid
flowchart LR
    subgraph EDGE["Cámaras IP y Procesamiento Perimetral"]
        CAM["Cámara IP Seguridad<br/>(RTSP / ONVIF / H.264)"]
        AI_EDGE["Módulo Edge Inferencia<br/>(NVIDIA Jetson / NVR con IA / MiniPC)<br/>YOLOv8 / OpenCV / MediaPipe"]
    end

    subgraph INGESTION["Capa de Eventos Ligera"]
        MQTT_AI["Broker MQTT Central<br/>Topic: unsa/camaras/eventos"]
    end

    subgraph STORAGE_DASH["Servidor y Visualización"]
        DB_EV[("Tabla camera_events<br/>(PostgreSQL)")]
        DASH_UI["Dashboard Web<br/>Tarjeta de Aforo, Intrusión y Streaming"]
    end

    CAM -->|Flujo RTSP / ONVIF| AI_EDGE
    AI_EDGE -->|Detección personas / aforo| MQTT_AI
    MQTT_AI --> DB_EV
    DB_EV --> DASH_UI
    CAM -.->|HLS / WebRTC bajo demanda| DASH_UI
```

### 8.1 Requisitos Técnicos que Deberán Exigirse al Adquirir las Cámaras
- **Protocolos de Streaming Estándar:** RTSP (Real-Time Streaming Protocol) y compatibilidad ONVIF Perfil S/T.
- **Códec de Vídeo:** H.264 / H.265 con soporte de sub-stream (resolución reducida a 640x360 a 10-15 fps para el procesamiento de IA sin saturar la red).
- **Conectividad:** Interfaz Ethernet RJ45 con soporte PoE 802.3af/at para alimentación centralizada.

### 8.2 Principio Arquitectónico de No Saturación
> [!CAUTION]
> **Regla de Diseño:** Nunca debe almacenarse el flujo de vídeo continuo dentro de la base de datos de telemetría de sensores.
- El módulo de visión artificial procesará el vídeo en el borde o en un servidor local especializado.
- La base de datos únicamente recibirá **eventos estructurados discretos** (conteo de personas en sala, alertas de presencia fuera de horario, o banderas de humo/fuego) mediante la tabla `camera_events`.
- Si el usuario del dashboard desea ver la cámara en vivo, el backend actuará como proxy WebRTC/HLS transmitiendo el vídeo en tiempo real directamente al navegador solo bajo demanda del operador.

---

## 9. Seguridad, Protección de Datos y Despliegue Online

Para la exposición segura del dashboard y los servicios en Internet:

1. **Cifrado en Tránsito:**
   - Todo el tráfico web hacia el dashboard y la API REST utilizará **HTTPS** obligatorio con certificados TLS automáticos gestionados por Let's Encrypt / Certbot.
   - El canal de telemetría MQTT utilizará **MQTTS sobre TLS 1.3** (puerto 8883) o WebSockets seguros (WSS).
2. **Segmentación de Red y Acceso Perimetral:**
   - El router Teltonika RUT951 mantendrá su firewall activo con descarte por defecto de conexiones entrantes de WAN (*Drop WAN input*).
   - El acceso de administración remota al RUT951 se realizará exclusivamente mediante túnel VPN seguro (WireGuard u OpenVPN) o el sistema de gestión centralizado Teltonika RMS.
3. **Autenticación y Control de Acceso:**
   - Acceso al dashboard protegido mediante autenticación basada en tokens JWT (JSON Web Tokens) con caducidad corta y tokens de refresco.
   - Control de acceso basado en roles (RBAC): Administrador, Investigador/Operador, y Visitante (solo lectura de paneles públicos).
4. **Protección de Credenciales y Secretos:**
   - Prohibido codificar contraseñas, tokens de API o cadenas de conexión en el repositorio Git. Uso estricto de variables de entorno protegidas (`.env`) y archivos de configuración en el servidor.
5. **Políticas de Respaldo:**
   - Copias de seguridad automáticas diarias de la base de datos PostgreSQL mediante `pg_dump` con retención rotativa de 30 días y replicación hacia almacenamiento externo seguro.

---

## 10. Plan de Implementación por Etapas

| Etapa | Descripción y Tareas Clave | Entregables Principales | Dependencias | Criterios de Aceptación | Riesgos Asociados |
|---|---|---|---|---|---|
| **E1** | Validación física de equipos y pruebas de laboratorio de sensores individuales. | Informe de verificación de banco y prototipo cableado. | Recepción física de bienes. | Cada sensor entrega datos válidos en puerto serie. | Fallo de hardware o piezas SMD sin breakout. |
| **E2** | Cableado definitivo, adaptación de niveles 3.3V/5V y estabilización de fuentes. | Esquema eléctrico final y nodo integrado en protoboard/PCB. | E1, fuente de 5V y desplazadores lógicos. | Alimentación estable sin caídas de tensión en arranque de SPS30. | Sobrecalentamiento o cortocircuitos. |
| **E3** | Programación del firmware del Arduino Nano 33 IoT (adquisición, filtrado y JSON). | Código fuente compilado y documentado en repositorio Git. | E2, drivers de sensores. | Lectura continua sin congelamientos del microcontrolador por >48h. | Saturación de SRAM por I2S o desbordamiento de buffers. |
| **E4** | Configuración del router Teltonika RUT951 y enlace Wi-Fi local / 4G LTE. | Router configurado con AP Wi-Fi, SIM celular activa y túnel VPN. | SIM 4G provista por UNSA y RUT951. | Conexión automática a Internet y reconexión ante caídas. | Cobertura celular deficiente en la zona de instalación. |
| **E5** | Despliegue de infraestructura de backend (Broker MQTT y PostgreSQL/TimescaleDB). | Servidor Linux configurado con Docker, Mosquitto y TimescaleDB. | Servidor/VPS asignado por la universidad. | Inserción automática de tramas MQTT en base de datos. | Puertos bloqueados por firewall institucional. |
| **E6** | Implementación de API REST y WebSockets para telemetría en tiempo real. | Backend FastAPI con documentación interactiva Swagger/OpenAPI. | E5 (Base de datos). | Endpoints responden en <50 ms bajo carga normal. | Consultas históricas lentas si faltan índices. |
| **E7** | Desarrollo de Frontend del Dashboard Web (React / TypeScript / Vite). | Aplicación web responsiva con gráficos interactivos y KPIs. | E6 (API REST / WSS). | Visualización fluida de los 8 parámetros ambientales en PC y móvil. | Complejidad de diseño responsivo. |
| **E8** | Implementación del motor de alarmas y notificaciones automáticas. | Módulo de alertas configurables por umbrales con avisos por email/Telegram. | E6, E7. | Disparo de alerta en <5 s tras superación de umbral. | Disparos continuos en cascada por ruido en la señal. |
| **E9** | Pruebas de estrés, simulación de cortes de red y recuperación automática. | Informe de pruebas de confiabilidad y resiliencia. | E3, E4, E7. | El sistema se reconecta y recupera sin intervención humana. | Fuga de memoria (memory leak) en firmware o backend. |
| **E10** | Instalación física definitiva en campus de la UNSA y puesta en marcha. | Sistema operando en locación final con caja de protección. | Aprobación de ubicación por UNSA y gabinete IP65. | Transmisión continua ininterrumpida durante 7 días consecutivos. | Daño ambiental por lluvia o calor extremo. |
| **E11** | Capacitación a usuarios y entrega de manuales técnicos y de operación. | Manual de usuario, manual de arquitectura y código documentado. | E10. | Operadores de la UNSA gestionan alertas y exportan datos con autonomía. | Falta de disponibilidad de personal para capacitación. |
| **E12** | Preparación de interfaces para cámaras futuras y visión artificial. | Módulo receptor de eventos de cámara listo para activarse. | E5, E6. | Pruebas exitosas de inserción de eventos simulados en `camera_events`. | Ninguno (preparación lógica). |

---

## 11. Lista Priorizada de Cuestiones Pendientes

Antes de iniciar la programación definitiva o desplegar en campo, se deben resolver las siguientes interrogantes clasificadas por severidad:

### 11.1 Cuestiones Bloqueantes (Impiden Iniciar el Desarrollo)
1. **[BLOQUEANTE] Confirmación del Modelo Físico de Luminancia:** ¿Se entregará el sensor TSL2591 auténtico (con rango de 88,000 lux) o el TSL2561 (con límite en 40,000 lux y direcciones configurables)? La librería de firmware y las direcciones I2C a programar son totalmente incompatibles entre ambos modelos.
2. **[BLOQUEANTE] Formato de Entrega del Sensor SHT45:** ¿El sensor se entregará en módulo breakout con pines estándar de 2.54 mm o como chip suelto SMD DFN-4? Si es chip suelto, debe detenerse el proceso hasta disponer de una placa adaptadora soldada.
3. **[BLOQUEANTE] Arnés y Conector para Sensirion SPS30:** ¿El proveedor incluye el cable conector micro JST ZHR-5? Sin este arnés, no existe conexión física posible hacia el microcontrolador.
4. **[BLOQUEANTE] Provisión del Ítem 9 (Sensor Telúrico):** ¿Se adjudicará el acelerómetro y geófono con otro postor o se reprogramará la compra? El equipo de software necesita saber si debe inicializar los buses SPI/I2C para el ADXL345 en el firmware base.

### 11.2 Cuestiones Importantes (Afectan la Arquitectura y el Despliegue)
5. **[IMPORTANTE] Infraestructura de Red Celular y Tarjeta SIM:** ¿Quién proveerá la tarjeta SIM 4G con plan de datos M2M para el router RUT951? ¿Qué operador local cuenta con la mejor cobertura en el punto de instalación del campus?
6. **[IMPORTANTE] Entorno de Alojamiento del Servidor Backend:** ¿La UNSA proveerá un servidor físico local en su centro de cómputo, una máquina virtual interna, o una instancia en la nube (AWS / GCP / DigitalOcean)?
7. **[IMPORTANTE] Arquitectura de Alimentación Eléctrica en Campo:** ¿Se cuenta con toma de 220VAC en el punto exacto de monitoreo, o se requiere un sistema autónomo solar/batería para alimentar los 9V del router y 5V de los sensores?

### 11.3 Cuestiones Recomendables (Mejoras Operativas)
8. **[RECOMENDABLE] Calibración en Sitio del Micrófono INMP441:** ¿Se dispondrá de un sonómetro patrón de referencia de la facultad para calibrar el factor de escala y asegurar mediciones fiables en decibelios (dBA)?
9. **[RECOMENDABLE] Umbrales Institucionales de Alerta:** ¿Cuáles son los valores límites específicos fijados por el proyecto de investigación para notificar incidencias (ej. concentraciones máximas de PM2.5 según Estándares de Calidad Ambiental peruanos)?
""")

    content = "\n".join(doc_lines)
    dest_path = r"d:\Proyectos\Arquitectura\informe\02_especificacion_tecnica_desarrollo.md"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Technical spec generated successfully: {dest_path} ({len(content)} characters)")

if __name__ == "__main__":
    generate_spec()
