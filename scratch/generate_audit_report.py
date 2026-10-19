# -*- coding: utf-8 -*-
"""
Script to generate informe/01_informe_auditoria_cumplimiento.md
"""
import os
import csv

def generate_report():
    csv_path = r"d:\Proyectos\Arquitectura\informe\03_matriz_cumplimiento.csv"
    matrix_rows = []
    with open(csv_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            matrix_rows.append(row)

    report_lines = []

    # 1. Portada
    report_lines.append("""# AUDITORÍA TÉCNICA DE ADQUISICIÓN DE EQUIPOS IoT Y SISTEMA DE MONITOREO AMBIENTAL

**Proyecto:** Sistema de Monitoreo Ambiental y Estructural con Telemetría IoT, Almacenamiento y Visualización en Dashboard Online  
**Entidad Contratante:** Universidad Nacional de San Agustín de Arequipa (UNSA)  
**Unidad Formuladora:** Unidad de Gestión de la Investigación (UGINY - UNSA)  
**Proveedor Evaluado:** SERCIA E.I.R.L. (RUC 2060469242)  
**Cotización Evaluada:** Declaración Jurada de Cotización de Bienes de fecha 09/08/2026 (Ref. PROPUESTA 1.pdf)  
**Fecha de Auditoría:** 19 de Octubre de 2026  
**Equipo Auditor Multidisciplinario:**
- Ingeniero Electrónico Especialista en Instrumentación y Sensores
- Ingeniero IoT Especialista en Telemetría y Comunicaciones
- Arquitecto de Software Especialista en Sistemas de Monitoreo y Bases de Datos
- Ingeniero de Aseguramiento de la Calidad (QA) y Verificación de Requisitos
- Auditor Técnico de Adquisiciones Tecnológicas

---

## 2. Resumen Ejecutivo

El presente informe constituye la auditoría técnica documental exhaustiva sobre la propuesta presentada por la empresa **SERCIA E.I.R.L.** para la adquisición de equipamiento de telemetría, controladores y sensores destinados al proyecto de monitoreo ambiental y estructural de la Universidad Nacional de San Agustín de Arequipa (UNSA).

### Condición Crítica Contractual
Conforme a los términos de referencia y bases del proyecto, **una vez aprobada la propuesta y emitidas las órdenes de compra correspondientes, la entidad contratante NO podrá realizar compras adicionales ni ampliaciones presupuestarias para subsanar omisiones, incompatibilidades o carencias de accesorios.** Esta condición impone un estándar de tolerancia cero a la ambigüedad y exige la verificación rigurosa de cada componente, bus, interfaz de comunicación, rango metrológico y requerimiento de alimentación eléctrica antes de emitir cualquier visto bueno.

### Resultados Cuantitativos de la Evaluación
De un total de **68 requisitos y parámetros evaluados** (que abarcan las especificaciones de las bases, condiciones generales y complementarias):
- **CUMPLE:** 44 requisitos (**64.71%**)
- **NO CUMPLE:** 11 requisitos (**16.18%**)
- **CUMPLE PARCIALMENTE:** 8 requisitos (**11.76%**)
- **NO VERIFICABLE:** 4 requisitos (**5.88%**)
- **CONTRADICTORIO:** 1 requisito (**1.47%**)

### Principales Hallazgos Críticos
1. **Omisión Total del Ítem 9 (Sensor Telúrico):** Las bases técnicas de contratación (Imágenes 1 y 2) exigen 9 ítems de equipamiento. El Ítem 9 requiere un sensor telúrico compuesto por un acelerómetro triaxial ADXL345 (±16g, 13 bits) y un geófono de 4.5 Hz - 1 kHz (sensibilidad 80 V/m/s). **La propuesta económica y técnica de SERCIA E.I.R.L. cotiza únicamente los Ítems 1 al 8, omitiendo por completo el Ítem 9.** Al no haberse cotizado ni incluido documentación de este sensor, el proyecto quedaría desprovisto de medición sísmica/estructural sin posibilidad de compra posterior.
2. **Incompatibilidad de Interfaz y Alimentación del Router Celular (Ítem 2 - Teltonika RUT951):** El requerimiento exigía un dispositivo con interfaz USB 2.0 y alimentación de 3.3V a 4.3V (especificación propia de un módem/dongle celular integrado). El proveedor ofertó un router industrial de riel DIN Teltonika RUT951 que **NO tiene puerto USB**, cuenta exclusivamente con puertos Ethernet RJ45 y Wi-Fi, y exige obligatoriamente una alimentación de 9V a 30V DC. Si bien el RUT951 es un equipo de comunicaciones robusto, no se conecta por USB al controlador ni puede alimentarse desde la línea de 3.3V/5V del nodo.
3. **Contradicción e Incumplimiento en Sensor de Luminancia (Ítem 4 - TSL2591):** El requerimiento exigía un sensor con rango dinámico de 188 mlux a 88,000 lux. El proveedor declara textualmente un rango de *0.1 a 40,000 Lux* y *3 direcciones I2C seleccionables (0x29/0x39/0x49)*. Estas características no corresponden al TSL2591 (que mide hasta 88,000 lux y tiene dirección I2C fija 0x29), sino al sensor inferior y desfasado TSL2561. Asimismo, el proveedor no adjuntó ficha técnica y declaró marca "nacional" para un semiconductor fabricado por ams-OSRAM.
4. **Incumplimiento de Interfaz en Sensor de Radiación (Ítem 5 - DFRobot SEN0463):** Se solicitó un sensor con interfaz USB Serial y alimentación 5V DC USB. El módulo ofertado es una placa didáctica con conector analógico/digital Gravity de 3 pines que entrega pulsos por cada evento de ionización (requiere interrupción por hardware en un microcontrolador) y carece de puerto USB Serial. Además, la entrega demora 30 días calendario (por importación) frente a los 10 días requeridos, y el fabricante advierte que es un equipo para enseñanza no apto para seguridad de personas.
5. **Carencia de Fuentes, Cables y Accesorios Críticos:** El microcontrolador Arduino Nano 33 IoT opera con lógica de 3.3V no tolerante a 5V. El sensor de calidad de aire SPS30 requiere 5V DC (hasta 80 mA en arranque) y conector propietario JST ZHR-5. El router RUT951 requiere 9-30V DC. La propuesta no incluye fuente regulada de 5V, adaptadores de nivel lógico (3.3V - 5V), cable de interfaz JST para SPS30, ni gabinete estanco de intemperie.
6. **Riesgo de Formato de Suministro en Sensor SHT45 (Ítem 7):** La ficha técnica adjuntada corresponde al circuito integrado desnudo SMD encapsulado DFN-4 de 1.5 x 1.5 mm en cinta y carrete industrial. Si no se entrega montado en una placa PCB con pines tipo cabecera (breakout board), no podrá ser soldado ni integrado en campo.

### Dictamen Técnico
**DICTAMEN: NO FAVORABLE (NO APTO PARA APROBACIÓN EN SU ESTADO ACTUAL).**  
La propuesta presenta incumplimientos directos de especificaciones obligatorias, omisión de un bien completo (Sensor Telúrico), contradicciones metrológicas y riesgos severos de incompatibilidad física y eléctrica que impedirían el funcionamiento integral del sistema sin desembolsos adicionales. Se establecen condiciones taxativas de subsanación técnica y aclaración formal previa antes de cualquier reevaluación.

---

## 3. Objetivo y Alcance

### 3.1 Objetivo
Realizar una auditoría técnica documental, imparcial y metrológicamente rigurosa a la cotización y especificaciones de bienes presentada por SERCIA E.I.R.L. frente a los requerimientos técnicos mínimos (RTM) fijados por la Universidad Nacional de San Agustín de Arequipa (UNSA), emitiendo un juicio fundado para proteger los recursos públicos y la viabilidad técnica del proyecto de investigación.

### 3.2 Alcance
El análisis abarca:
1. Inspección documental y verificación de autenticidad de los requerimientos contenidos en las imágenes oficiales.
2. Contraste parámetro por parámetro de cada equipo ofertado en la cotización y anexos de `PROPUESTA 1.pdf`.
3. Evaluación de compatibilidad eléctrica, electrónica, buses de comunicación, consumo de energía y montaje físico entre todos los componentes.
4. Determinación de faltantes (accesorios, conectores, fuentes, cables y licencias).
5. Evaluación de la idoneidad metrológica de los sensores para su explotación en un backend y dashboard web.

---

## 4. Documentación Examinada

La auditoría se basó exclusivamente en la evidencia documental disponible en la carpeta `fuentes/` del repositorio, complementada con las hojas de datos oficiales de los fabricantes de los semiconductores cuando fue técnicamente necesario para dirimir contradicciones:

| N° | Identificador / Nombre de Archivo | Formato | Páginas / Tamaño | Origen y Descripción |
|---|---|---|---|---|
| 1 | `WhatsApp Image 2026-10-19 at 8.09.18 AM.jpeg` | JPEG | 1 página (82.5 KB) | Documento original UNSA: Sección 6 "CARACTERÍSTICAS Y CONDICIONES DE LOS BIENES A CONTRATAR", Numeral 6.1, Ítems 1 al 5 (Controlador, Dispositivo de comunicación, Sensor Calidad de Aire, Sensor Luminancia, Sensor Radiación). |
| 2 | `WhatsApp Image 2026-10-19 at 8.09.18 AM (1).jpeg` | JPEG | 1 página (92.8 KB) | Documento original UNSA: Numeral 6.1, Ítems 6 al 9 (Sensor Ruido, Sensor Temperatura y Humedad, Sensor Pluviómetro, Sensor Telúrico). Incluye visados oficiales UGINY-UNSA de fecha 14/07/2026 y 15/07/2026. |
| 3 | `PROPUESTA 1.pdf` | PDF vectorial/escaneado | 66 páginas (3.22 MB) | Expediente presentado por SERCIA E.I.R.L.:<br>• Pág. 1-2: Declaración Jurada de Cotización formal (09/08/2026).<br>• Pág. 3-8: Teltonika RUT951 Quick Start Guide v1.0.<br>• Pág. 9-34: Sensirion SPS30 Datasheet v2.0 (Junio 2023).<br>• Pág. 35-37: Rika Sensors RK400-04 Rainfall Sensor Datasheet v3.0.<br>• Pág. 38-59: Sensirion SHT4x Datasheet v5 (Enero 2023).<br>• Pág. 60-64: AG Electrónica ABX00027 Arduino Nano 33 IoT Ficha Técnica.<br>• Pág. 65-66: AG Electrónica DFRobot SEN0463 Contador Geiger Ficha Técnica. |

---

## 5. Metodología y Criterios de Evaluación

### 5.1 Procedimiento de Auditoría
1. **Extracción y Trazabilidad:** Desagregación de cada línea descriptiva de las bases de contratación en parámetros medibles individuales con asignación de un código estable (`REQ-001` a `REQ-068`).
2. **Contraste Documental Objetivo:** Comparación directa entre la condición requerida y la evidencia explícita provista por el postor en su cotización o fichas técnicas. No se asumieron capacidades no respaldadas documentalmente.
3. **Análisis de Coherencia Cruzada:** Verificación de compatibilidad mutua (tensión de operación, niveles de señal lógica, protocolo físico de buses, consumo de corriente y direccionamiento I2C).
4. **Categorización de Cumplimiento:**
   - **CUMPLE:** Existe evidencia documental suficiente de que el parámetro ofrecido satisface o supera el requerimiento.
   - **NO CUMPLE:** La información documental demuestra discrepancia o incumplimiento con el requisito, o el bien fue omitido.
   - **CUMPLE PARCIALMENTE:** Satisface una parte del requisito, opera bajo condiciones restringidas, o presenta limitaciones metrológicas/operativas.
   - **NO VERIFICABLE:** La propuesta omite información técnica indispensable para confirmar o descartar el cumplimiento (p. ej. falta de fichas técnicas o números de parte incompletos).
   - **CONTRADICTORIO:** La propuesta contiene datos mutuamente excluyentes o incompatibles entre sus diferentes secciones.

---

## 6. Inventario de Bienes y Dispositivos Ofertados

En la siguiente tabla se consolida la oferta económica y técnica presentada por SERCIA E.I.R.L. (Página 1 de `PROPUESTA 1.pdf`):

| Ítem Solicitado | Descripción Solicitada | Cant. | Marca Ofertada | Modelo Ofertado | Garantía (Meses) | Plazo Entrega | P. Unitario (S/ inc. IGV) | P. Total (S/) | Ficha Técnica Adjunta en PDF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Controlador | 1 | Arduino | Nano 33 IoT (SKU ABX00027) | 12 | 10 días | 160.00 | 160.00 | Sí (AG Electrónica, Pág. 60-64) |
| 2 | Dispositivo de comunicación | 1 | Teltonika | RUT951 | 12 | 10 días | 1,360.00 | 1,360.00 | Sí (Quick Start Guide, Pág. 3-8) |
| 3 | Sensor de Calidad del Aire | 1 | Sensirion | SPS30 | 12 | 10 días | 165.00 | 165.00 | Sí (Datasheet oficial, Pág. 9-34) |
| 4 | Sensor de Luminancia | 1 | nacional | TSL2591 | 12 | 10 días | 55.00 | 55.00 | **NO ADJUNTA FICHA TÉCNICA** |
| 5 | Sensor de Radiación | 1 | DFRobot | SEN0463 | 12 | **30 días (importación)** | 420.00 | 420.00 | Sí (AG Electrónica, Pág. 65-66) |
| 6 | Sensor de Ruido Ambiental | 1 | nacional | INMP441 | 12 | 10 días | 51.00 | 51.00 | **NO ADJUNTA FICHA TÉCNICA** |
| 7 | Sensor Temp. y Humedad | 1 | nacional | SHT45 | 12 | 10 días | 179.00 | 179.00 | Sí (Sensirion SHT4x, Pág. 38-59) |
| 8 | Sensor Pluviómetro | 1 | Rika Sensors | RK400-04 | 12 | 10 días | 1,295.00 | 1,295.00 | Sí (Datasheet oficial, Pág. 35-37) |
| 9 | Sensor Telúrico | 1 | **NO OFERTADO** | **NO OFERTADO** | - | - | **0.00** | **0.00** | **OMITIDO POR COMPLETO** |
| **TOTAL** | | | | | | | | **S/. 3,685.00** | |

---

## 7. Transcripción y Clasificación de los Requisitos

A continuación se transcribe fielmente el contenido de las dos imágenes de requerimientos técnicos:

### 7.1 Requisitos de Imagen 1 (`WhatsApp Image 2026-10-19 at 8.09.18 AM.jpeg`)
- **Encabezado:** "6. CARACTERÍSTICAS Y CONDICIONES DE LOS BIENES A CONTRATAR" / "6.1. Descripción de los bienes a contratar"
- **Ítem 1 (1 Unidad): Controlador**
  - Procesador 16/32-bit
  - Frecuencia 48 MHz
  - Memoria Flash 256 KB
  - SRAM 32 KB
  - Alimentación 5V VIN / 3.3V
  - Pines Digital I/O 22
  - Pines PWM 12
  - Pines Analógicos 7 (ADC 12-bit)
  - Comunicación UART, I2C, SPI
  - WiFi ESP32 (U-blox NINA-W102)
  - BLE Bluetooth 4.2
  - Consumo 15-20 mA (activo)
- **Ítem 2 (1 Unidad): Dispositivo de comunicación**
  - Bandas LTE LTE-FDD: B1/B3/B5/B7/B8/B20
  - Velocidad descarga 150 Mbps
  - Velocidad subida 50 Mbps
  - Interface USB 2.0
  - Antena 2x SMA externas
  - Protocolos TCP/IP, UDP, HTTP, HTTPS
  - Alimentación 3.3V - 4.3V
- **Ítem 3 (1 Unidad): Sensor de Calidad de Aire**
  - Partículas medidas PM1.0, PM2.5, PM4.0, PM10
  - Rango de medición 0-1000 µg/m³
  - Resolución 1 µg/m³
  - Interface I2C/UART
  - Alimentación 5V DC ±10%
  - Precisión ±10% del valor medido
  - Tiempo respuesta 10 segundos
- **Ítem 4 (1 Unidad): Sensor de Luminancia**
  - Rango dinámico 188 mlux to 88,000 lux
  - Resolución ADC 16-bit
  - Interface I2C
  - Longitud onda 300-1000 nm
  - Alimentación 3.3V DC
- **Ítem 5 (1 Unidad): Sensor de Radiación**
  - Tipo radiación Gamma, Beta, X-Ray
  - Rango 0.08-1200 µSv/h
  - Sensor Tubo Geiger-Muller
  - Interface USB Serial
  - Alimentación 5V DC USB
  - Energía 0.5W

### 7.2 Requisitos de Imagen 2 (`WhatsApp Image 2026-10-19 at 8.09.18 AM (1).jpeg`)
- **Ítem 6 (1 Unidad): Sensor de Ruido Ambiental**
  - Rango frecuencia 60Hz - 15kHz
  - SNR 61 dBA
  - Sensibilidad -26 dBFS
  - Interface I2S
  - Patrón polar Omnidireccional
  - Alimentación 3.3V DC
- **Ítem 7 (1 Unidad): Sensor de Temperatura y Humedad Ambiental**
  - Rango temperatura -40°C a 125°C
  - Precisión temperatura ±0.1°C (0-65°C)
  - Rango humedad 0-100% RH
  - Precisión humedad ±1.5% RH (0-90% RH)
  - Interface I2C
  - Alimentación 3.3V DC
  - Consumo 1.7µA (típico)
  - *Visado registrado:* Monitor de Proyectos UGINY-UNSA (Maria Nelly Pezo Torres, 15/07/2026).
- **Ítem 8 (1 Unidad): Sensor Pluviómetro**
  - Resolución 0.2mm por pulso
  - Capacidad 200mm/hora
  - Material ABS + Acero inox
  - Contacto Reed switch
  - Alimentación 5-12V DC
  - *Visado registrado:* Gestor Administrativo UGINY-UNSA (Patricia Monjaras del Carpio, 14/07/2026).
- **Ítem 9 (1 Unidad): Sensor Telúrico**
  - Componente Especificación:
    - Acelerómetro ADXL345 3-axis
    - Rango ±16g
    - Resolución 13-bit
    - Interface SPI/I2C
    - Geófono 4.5Hz - 1kHz
    - Sensibilidad 80V/m/s
  - *Nota visual:* La fila del Ítem 9 inicia en la tabla superior y sus parámetros específicos están contenidos en el recuadro inferior situado tras la barra divisoria.

---

## 8. Matriz de Cumplimiento Completa

A continuación se presenta la matriz completa de trazabilidad técnica (disponible también en formato tabular estructurado en `informe/03_matriz_cumplimiento.csv`):

| ID | Bien / Parámetro | Valor Requerido | Especificación Ofertada | Evidencia Documental | Evaluación | Justificación Técnica y Riesgo |
|---|---|---|---|---|---|---|
| **REQ-001** | Controlador: Procesador | 16/32-bit | SAMD21G18A ARM Cortex-M0+ 32-bit | Pág. 1, 60-61 | **CUMPLE** | Procesador de 32 bits conforme. Sin riesgo. |
| **REQ-002** | Controlador: Frecuencia | 48 MHz | Hasta 48 MHz | Pág. 61 | **CUMPLE** | Reloj de 48 MHz nativo. Sin riesgo. |
| **REQ-003** | Controlador: Flash | 256 KB | 256 KB | Pág. 61 | **CUMPLE** | Memoria de programa suficiente para firmware IoT. |
| **REQ-004** | Controlador: SRAM | 32 KB | 32 KB | Pág. 61 | **CUMPLE** | Memoria de datos adecuada; vigilar buffers de audio I2S. |
| **REQ-005** | Controlador: Alimentación | 5V VIN / 3.3V | VIN (4.5V-21V), lógica 3.3V. Pines no toleran 5V. Pin 5V inactivo. | Pág. 61 | **CUMPLE PARCIALMENTE** | **Riesgo crítico:** no entrega 5V regulados por VIN y no tolera 5V en GPIO. Puede dañarse si se conecta señal de 5V. |
| **REQ-006** | Controlador: Pines GPIO | 22 | 14 digitales + 8 analógicos = 22 GPIO | Pág. 63 | **CUMPLE** | Pines reconfigurables en el SAMD21. |
| **REQ-007** | Controlador: Pines PWM | 12 | Ficha pág. 63 lista 5 pines (D3, D5, D6, D9, D10). Máximo hardware: 11. | Pág. 63 | **NO CUMPLE** | No alcanza 12 pines PWM nativos. |
| **REQ-008** | Controlador: Entradas ADC | 7 (ADC 12-bit) | 8 canales A0-A7 de 12 bits | Pág. 63 | **CUMPLE** | Supera la cantidad solicitada. A4 y A5 tienen pull-up para I2C. |
| **REQ-009** | Controlador: Buses serie | UART, I2C, SPI | Canales SERCOM nativos para UART, I2C, SPI | Pág. 63-64 | **CUMPLE** | Interfaces soportadas. Solo 1 UART hardware externo (Serial1). |
| **REQ-010** | Controlador: WiFi | ESP32 (U-blox NINA-W102) | Módulo u-blox NINA-W102 con ESP32 | Pág. 60, 62 | **CUMPLE** | Coincide exactamente con el componente exigido. |
| **REQ-011** | Controlador: BLE | Bluetooth 4.2 | Bluetooth 4.2 / BLE en módulo NINA | Pág. 60, 62 | **CUMPLE** | Estándar soportado por hardware. |
| **REQ-012** | Controlador: Consumo | 15-20 mA (activo) | CPU consume ~15 mA sin radio; con Wi-Fi asciende a >100 mA | Pág. 60-61 | **CUMPLE PARCIALMENTE** | Cumple en reposo; con radio activa el consumo es sustancialmente mayor. |
| **REQ-013** | Router: Bandas LTE | B1/B3/B5/B7/B8/B20 | LTE Cat 4: B1, B3, B5, B7, B8, B20 | Pág. 6 | **CUMPLE** | Bandas celulares soportadas en versión global. |
| **REQ-014** | Router: Bajada | 150 Mbps | Hasta 150 Mbps (LTE Cat 4) | Pág. 6 | **CUMPLE** | Velocidad estándar de categoría 4. |
| **REQ-015** | Router: Subida | 50 Mbps | Hasta 50 Mbps (LTE Cat 4) | Pág. 6 | **CUMPLE** | Velocidad estándar de categoría 4. |
| **REQ-016** | Router: Interfaz USB | USB 2.0 | **NO TIENE USB.** Posee 4 puertos RJ45 y Wi-Fi | Pág. 4, Teltonika | **NO CUMPLE** | **Incumplimiento grave:** no se puede conectar por USB al controlador ni a sensores. |
| **REQ-017** | Router: Antenas | 2x SMA externas | 2 conectores SMA hembra y 2 antenas móviles incluidas | Pág. 4, 6 | **CUMPLE** | Antenas externas omnidireccionales suministradas. |
| **REQ-018** | Router: Protocolos | TCP/IP, UDP, HTTP, HTTPS | RutOS soporta TCP/IP, UDP, HTTP, HTTPS, MQTT, VPN | Pág. 6-8 | **CUMPLE** | Pila completa y segura de red industrial. |
| **REQ-019** | Router: Alimentación | 3.3V - 4.3V | **Requiere 9 a 30 VDC.** Adaptador incluido entrega 9VDC / 1A | Pág. 5, 6 | **NO CUMPLE** | **Incompatibilidad eléctrica:** no opera a 3.3V-4.3V. Requiere 220VAC o fuente industrial de 12V. |
| **REQ-020** | Calidad Aire: Parámetros | PM1.0, PM2.5, PM4.0, PM10 | Medición de masa y número para PM1.0, PM2.5, PM4.0, PM10 | Pág. 10, 14 | **CUMPLE** | Cuatro fracciones soportadas por algoritmo de Sensirion. |
| **REQ-021** | Calidad Aire: Rango | 0-1000 µg/m³ | 0 a 1000 µg/m³ | Pág. 10 | **CUMPLE** | Rango certificado de concentración en masa. |
| **REQ-022** | Calidad Aire: Resolución | 1 µg/m³ | 1 µg/m³ (modo entero) / flotante IEEE754 | Pág. 14 | **CUMPLE** | Salida digital de alta resolución. |
| **REQ-023** | Calidad Aire: Interfaz | I2C/UART | UART (SHDLC) e I2C seleccionables | Pág. 12 | **CUMPLE** | Requiere arnés micro JST ZHR-5 no incluido en la oferta. |
| **REQ-024** | Calidad Aire: Alimentación | 5V DC ±10% | 4.5 V a 5.5 V DC | Pág. 11 | **CUMPLE** | Requiere fuente externa de 5V (Arduino no la provee por VIN). |
| **REQ-025** | Calidad Aire: Precisión | ±10% del valor medido | PM1/2.5 (>100): ±10%. Bajas conc.: ±5 µg/m³. PM4/10: ±25% | Pág. 10 | **CUMPLE PARCIALMENTE** | Cumple solo en concentraciones altas de PM1/2.5. En PM4/10 tolerancia es ±25%. |
| **REQ-026** | Calidad Aire: Respuesta | 10 segundos | Tasa muestreo 1 s; tiempo de inicio 8 a 30 s | Pág. 10 | **CUMPLE** | Actualización en tiempo real. |
| **REQ-027** | Luminancia: Rango | 188 mlux to 88,000 lux | Cotización declara: **"0.1 a 40,000 Lux"** | Pág. 1 | **NO CUMPLE** | **Discrepancia frontal:** 40,000 lux es el rango del TSL2561, no del TSL2591. Se saturará al sol. |
| **REQ-028** | Luminancia: Resolución | ADC 16-bit | ADC dual de 16 bits | Pág. 1 | **CUMPLE** | Conforme con la arquitectura de fotodiodos. |
| **REQ-029** | Luminancia: Interfaz | I2C | Comunicación I2C | Pág. 1 | **CUMPLE** | Protocolo serie I2C. |
| **REQ-030** | Luminancia: Espectro | 300-1000 nm | Fotodiodo dual visible e infrarrojo (300-1100 nm) | Pág. 1 | **CUMPLE** | Respuesta espectral del silicio. |
| **REQ-031** | Luminancia: Alimentación | 3.3V DC | Operación a 3.3V (15 µA standby) | Pág. 1 | **CUMPLE** | Compatible con bus de 3.3V. |
| **REQ-032** | Luminancia: Dirección I2C | Dirección no conflictiva | Cotización declara: **3 direcciones seleccionables (0x29/0x39/0x49)** | Pág. 1 | **CONTRADICTORIO** | El TSL2591 tiene dirección FIJA 0x29. Esas 3 direcciones corresponden al TSL2561. |
| **REQ-033** | Luminancia: Documentación | Ficha técnica oficial | Marca "nacional". **No adjunta ficha técnica.** | Pág. 1 | **NO VERIFICABLE** | Chip es de ams-OSRAM. Falta respaldo técnico del módulo físico. |
| **REQ-034** | Radiación: Tipo | Gamma, Beta, X-Ray | Detecta radiación gamma, beta dura y rayos X | Pág. 66 | **CUMPLE** | Sensibilidad física del tubo Geiger M4011. |
| **REQ-035** | Radiación: Rango | 0.08-1200 µSv/h | Máx. 1200 µSv/h teórico; fondo ~25 CPM | Pág. 65 | **CUMPLE PARCIALMENTE** | Límite inferior de 0.08 µSv/h sin calibrar. |
| **REQ-036** | Radiación: Sensor | Tubo Geiger-Muller | Tubo Geiger-Müller M4011 | Pág. 65 | **CUMPLE** | Elemento sensor conforme. |
| **REQ-037** | Radiación: Interfaz | USB Serial | **NO TIENE USB.** Salida de pulsos digitales Gravity (3 pines) | Pág. 65-66 | **NO CUMPLE** | **Incumplimiento técnico:** no se puede conectar a puerto USB; exige un GPIO de interrupción. |
| **REQ-038** | Radiación: Alimentación | 5V DC USB | Pines Gravity (3.3V ~ 5V DC). **Sin conector USB.** | Pág. 65-66 | **NO CUMPLE** | Requiere cableado directo a pines DC. |
| **REQ-039** | Radiación: Potencia | 0.5W | Consumo típico < 0.15 W | Pág. 65 | **CUMPLE** | Potencia inferior a 0.5W. |
| **REQ-040** | Radiación: Plazo entrega | 10 días calendario | Ofertado: **30 días calendario (importación)** | Pág. 1 | **CUMPLE PARCIALMENTE** | Triplica el plazo de entrega del proyecto. |
| **REQ-041** | Radiación: Grado equipo | Monitoreo confiable | Ficha advierte: **"no apto para seguridad personal; didáctico"** | Pág. 66 | **CUMPLE PARCIALMENTE** | Equipo educativo no profesional. |
| **REQ-042** | Ruido: Frecuencia | 60Hz - 15kHz | 60 Hz a 15 kHz | Pág. 1 | **CUMPLE** | Ancho de banda acústico conforme. |
| **REQ-043** | Ruido: SNR | 61 dBA | SNR: 61 dBA | Pág. 1 | **CUMPLE** | Relación señal/ruido nominal. |
| **REQ-044** | Ruido: Sensibilidad | -26 dBFS | -26 dBFS | Pág. 1 | **CUMPLE** | Sensibilidad acústica conforme. |
| **REQ-045** | Ruido: Interfaz | I2S | I2S digital de 24 bits | Pág. 1 | **CUMPLE** | Requiere manejo de reloj y datos I2S en SAMD21. |
| **REQ-046** | Ruido: Patrón polar | Omnidireccional | MEMS omnidireccional | Pág. 1 | **CUMPLE** | Puerto acústico inferior. |
| **REQ-047** | Ruido: Alimentación | 3.3V DC | 1.8V a 3.3V DC (1.4 mA) | Pág. 1 | **CUMPLE** | Bajo consumo a 3.3V. |
| **REQ-048** | Ruido: Documentación | Ficha técnica oficial | Marca "nacional". **No adjunta ficha técnica.** | Pág. 1 | **NO VERIFICABLE** | Chip es de TDK InvenSense. Falta ficha del módulo PCB. |
| **REQ-049** | Ruido: Medición dBA | Nivel sonoro (dBA) | Entrega audio PCM en bruto, no decibelios dBA | Pág. 1 | **CUMPLE PARCIALMENTE** | Requiere algoritmo DSP de ponderación A en software y calibración SPL. |
| **REQ-050** | Temp/Hum: Rango Temp | -40°C a 125°C | -40 °C a +125 °C | Pág. 38, 43 | **CUMPLE** | Rango térmico completo. |
| **REQ-051** | Temp/Hum: Precisión Temp| ±0.1°C (0-65°C) | Típica ±0.1 °C (NIST / ISO 17025) | Pág. 38, 43 | **CUMPLE** | Máxima precisión de la serie SHT4x. |
| **REQ-052** | Temp/Hum: Rango Hum | 0-100% RH | 0 a 100 %RH | Pág. 38, 41 | **CUMPLE** | Rango psicrométrico completo. |
| **REQ-053** | Temp/Hum: Precisión Hum | ±1.5% RH (0-90% RH) | Típica ±1.0 %RH | Pág. 38, 41 | **CUMPLE** | Supera la precisión solicitada. |
| **REQ-054** | Temp/Hum: Interfaz | I2C | I2C (dirección 0x44) | Pág. 38, 48 | **CUMPLE** | Protocolo I2C con CRC-8. No colisiona. |
| **REQ-055** | Temp/Hum: Alimentación | 3.3V DC | 1.08 V a 3.6 V DC | Pág. 38, 46 | **CUMPLE** | Operación nativa a 3.3V. |
| **REQ-056** | Temp/Hum: Consumo | 1.7µA (típico) | 0.4 a 2.2 µA según repetibilidad | Pág. 38, 46 | **CUMPLE** | Ultra bajo consumo. |
| **REQ-057** | Temp/Hum: Formato físico| Módulo integrable | Ficha muestra **chip suelto SMD DFN-4 de 1.5x1.5 mm en cinta** | Pág. 38, 51-57 | **NO VERIFICABLE** | Si se entrega chip suelto, es imposible soldarlo sin taller especializado. |
| **REQ-058** | Pluviómetro: Resolución | 0.2mm por pulso | 0.2 mm por balanceo de balancín | Pág. 35 | **CUMPLE** | Resolución hidrológica conforme. |
| **REQ-059** | Pluviómetro: Capacidad | 200mm/hora | Medida: 240 mm/h; admisible: 480 mm/h | Pág. 35 | **CUMPLE** | Supera la capacidad requerida. |
| **REQ-060** | Pluviómetro: Material | ABS + Acero inox | Embudo ABS, patas de acero 304SS | Pág. 35 | **CUMPLE** | Resistente a intemperie. |
| **REQ-061** | Pluviómetro: Contacto | Reed switch | Contacto magnético reed switch pasivo | Pág. 36 | **CUMPLE** | Conmutación por contacto seco. Requiere antirrebote. |
| **REQ-062** | Pluviómetro: Alimentación| 5-12V DC | Contacto seco pasivo (max 30V). Versión RS485 exige 12-24V | Pág. 35, 37 | **CUMPLE PARCIALMENTE** | Reed switch no consume voltaje; variante activa RS485 no opera a 5V. |
| **REQ-063** | Pluviómetro: Código exacto| Código y cable definidos| Solo indica 'RK400-04' sin sufijo ni cable | Pág. 1, 37 | **NO VERIFICABLE** | No se conoce la variante de salida ni longitud de cable incluida. |
| **REQ-064** | Telúrico: Acelerómetro | ADXL345 (±16g, 13b, SPI/I2C)| **NO COTIZADO / OMITIDO** | Pág. 1 | **NO CUMPLE** | **Omisión total:** no cotizado ni documentado. |
| **REQ-065** | Telúrico: Geófono | 4.5Hz - 1kHz, 80V/m/s | **NO COTIZADO / OMITIDO** | Pág. 1 | **NO CUMPLE** | **Omisión total:** no cotizado ni documentado. |
| **REQ-066** | Lote: Cantidad ítems | 9 bienes unitarios | Ofertados solo 8 bienes unitarios | Pág. 1 | **NO CUMPLE** | Propuesta económica y técnica incompleta. |
| **REQ-067** | Documentación técnica | Fichas técnicas completas | Faltan fichas de Ítems 4, 6 y 9 | Pág. 1-66 | **NO CUMPLE** | 33% de los ítems carecen de hoja de datos oficial. |
| **REQ-068** | Compatibilidad integral | Sistema funcional conjunto | Desajustes de voltaje, falta de fuentes de 5V y conversores | Evaluación cruzada | **NO CUMPLE** | Imposible hacer funcionar el lote sin compras adicionales de accesorios. |

---

## 9. Evaluación Técnica Individual de Cada Equipo

### 9.1 Ítem 1: Controlador - Arduino Nano 33 IoT (SKU ABX00027)
- **Fabricante:** Arduino (diseñado en Italia). Microcontrolador principal: Microchip ATSAMD21G18A (ARM Cortex-M0+ a 48 MHz, 256 KB Flash, 32 KB SRAM).
- **Módulo de Comunicaciones:** u-blox NINA-W102 (basado en Espressif ESP32) para conectividad Wi-Fi 802.11 b/g/n y Bluetooth 4.2 / BLE.
- **Seguridad Hardware:** Criptochip Microchip ATECC608A para almacenamiento seguro de certificados y claves TLS. Sensor inercial interno LSM6DS3 (IMU de 6 ejes).
- **Evaluación Metrológica y Funcional:** El microcontrolador dispone de potencia adecuada para adquisición de señales ambientales y formateo en JSON/MQTT. Sin embargo, su memoria RAM de 32 KB impone un techo restrictivo para el almacenamiento temporal durante cortes de conexión.
- **Riesgo Eléctrico Crítico:** La placa opera exclusivamente a 3.3V y sus entradas digitales **NO son tolerantes a 5V**. El pin rotulado como 5V viene desconectado de fábrica (requiere soldar un jumper en la parte posterior) y solo suministra 5V cuando se alimenta mediante el puerto micro-USB. Si el Arduino se energiza a través de VIN, el pin de 5V permanece inactivo y no puede energizar sensores externos como el SPS30.

### 9.2 Ítem 2: Dispositivo de Comunicación - Teltonika RUT951
- **Fabricante:** Teltonika Networks (Lituania). Enrutador industrial celular 4G LTE Cat 4 (hasta 150 Mbps DL / 50 Mbps UL).
- **Conectividad:** 4 puertos Ethernet Fast Ethernet 10/100 (1 WAN, 3 LAN), Wi-Fi 2.4 GHz (802.11 b/g/n, hasta 150 Mbps), 2 ranuras SIM con failover automático, 2 conectores SMA para antenas móviles y 2 conectores RP-SMA para antenas Wi-Fi.
- **Sistema Operativo:** RutOS basado en OpenWrt Linux, con cortafuegos avanzado, soporte para VPN (OpenVPN, WireGuard, IPsec), cliente/broker MQTT y Modbus TCP.
- **Incompatibilidades Directas:** 
  1. Carece de puerto USB 2.0 (el requerimiento exigía interfaz USB).
  2. Requiere tensión de alimentación de 9V a 30V DC (el requerimiento pedía 3.3V a 4.3V).
- **Evaluación Operativa:** Es un equipo industrial robusto y con certificaciones europeas (CE/RED), pero no es un módem embebido ni se puede conectar por cable USB al Arduino. La única vía de enlace entre el Arduino y el RUT951 es mediante la red inalámbrica Wi-Fi local.

### 9.3 Ítem 3: Sensor de Calidad de Aire - Sensirion SPS30
- **Fabricante:** Sensirion AG (Suiza). Principio de medición: Dispersión láser (Laser Scattering) con tecnología de resistencia a la contaminación y sistema de autolimpieza de ventilador.
- **Parámetros Medidos:** Masa (PM1.0, PM2.5, PM4.0, PM10 en rango 0 a 1000 µg/m³) y concentración numérica (PM0.5, PM1.0, PM2.5, PM4.0, PM10).
- **Interfaces:** Doble interfaz UART (protocolo SHDLC a 115200 bps) e I2C (dirección fija 0x69, hasta 100 kHz).
- **Aspectos Eléctricos y de Integración:** Requiere 5V DC ±10% y consume hasta 80 mA durante los primeros 200 ms de arranque del ventilador. Sus líneas de datos son compatibles con niveles TTL 5V y LVTTL 3.3V.
- **Observación Crítica:** Utiliza un conector miniatura propietario JST ZHR-5 de 5 pines. La cotización de SERCIA no incluye el cable conector hembra ni arnés de conexión.

### 9.4 Ítem 4: Sensor de Luminancia - TSL2591 (Declarado "nacional")
- **Fabricante Original del Chip:** ams-OSRAM (Austria).
- **Discrepancia Metrológica Grave:** Las bases solicitan un rango de hasta 88,000 lux. En la cotización económica formal (Pág. 1), el postor declara un rango de "0.1 a 40,000 Lux" y "3 direcciones I2C seleccionables (0x29 / 0x39 / 0x49)". Estas especificaciones corresponden al modelo inferior TSL2561. El chip TSL2591 tiene dirección fija 0x29 y rango de hasta 88,000 lux con 600 millones a 1 de rango dinámico.
- **Carencia Documental:** No se adjunta ficha técnica de la placa breakout ni se acredita la procedencia bajo la denominación de marca "nacional".

### 9.5 Ítem 5: Sensor de Radiación - DFRobot SEN0463
- **Fabricante:** DFRobot (China). Elemento sensor: Tubo Geiger-Müller M4011 de fabricación china (polarizado a ~400V DC internos).
- **Detección:** Rayos gamma (γ), rayos beta energéticos (β) y radiación X. Sensibilidad nominal de 153.8 CPM por µSv/h con fondo natural de ~25 CPM.
- **Incompatibilidad de Interfaz:** No cuenta con salida USB Serial. Dispone de un conector de 3 pines analógico/digital Gravity que emite un pulso descendente (active-low) por cada descarga en el gas del tubo.
- **Régimen de Operación:** La placa requiere un microcontrolador que cuente pulsos mediante interrupciones externas (ISR) y calcule CPM de forma temporalizada. La ficha técnica advierte expresamente que no es un equipo con calibración para dosimetría de seguridad humana.

### 9.6 Ítem 6: Sensor de Ruido Ambiental - INMP441 (Declarado "nacional")
- **Fabricante Original del Chip:** TDK InvenSense (Japón/EE.UU.). Micrófono MEMS con interfaz I2S digital de 24 bits.
- **Respuesta Acústica:** Omnidireccional, SNR de 61 dBA, sensibilidad de -26 dBFS y respuesta plana entre 60 Hz y 15 kHz.
- **Evaluación Funcional:** Físicamente cumple con los requerimientos electroacústicos, pero **no es un sensor de nivel sonoro integrado (sonómetro)**. El dispositivo entrega un flujo continuo de muestras de audio PCM digital. Para obtener el nivel de ruido ambiental en decibelios (dBA/Leq), el microcontrolador o servidor debe aplicar un filtro digital de ponderación A y una integración cuadrática media (RMS), requiriendo calibración previa frente a un sonómetro patrón.
- **Carencia Documental:** El proveedor omitió presentar la hoja de datos técnicos.

### 9.7 Ítem 7: Sensor de Temperatura y Humedad Ambiental - Sensirion SHT45 (Declarado "nacional")
- **Fabricante Original:** Sensirion AG (Suiza).
- **Metrología:** Sensor capacitivo de altísima precisión: ±0.1 °C (0 a 65 °C) y ±1.0 %RH (0 a 90 %RH). Incorpora microcalefactor integrado para descondensación y trazabilidad NIST / ISO 17025. Interfaz I2C estándar en dirección 0x44.
- **Riesgo Mecánico/Montaje:** La documentación adjunta corresponde al circuito integrado SMD encapsulado DFN-4 de 1.5 x 1.5 x 0.5 mm en formato industrial de cinta y carrete (tape and reel). No se especifica si se entrega premontado sobre placa PCB de inserción. Entregar el chip suelto inutilizaría el ítem.

### 9.8 Ítem 8: Sensor Pluviómetro - Rika Sensors RK400-04
- **Fabricante:** Hunan Rika Electronic Technology Co., Ltd. (China).
- **Mecánica:** Embudo colector de 200 mm de diámetro, balancín basculante calibrado a 0.2 mm de precipitación y burbuja de nivelación integrada. Capacidad de hasta 240 mm/h.
- **Transducción:** Conmutación magnética de láminas (reed switch) libre de tensión.
- **Deficiencia Documental:** La cotización no consigna el número de parte completo ni precisa la longitud de cable suministrada (1.5 m, 3 m, etc.) ni si incluye la electrónica con salida RS485 o pulsos directos.

### 9.9 Ítem 9: Sensor Telúrico - ADXL345 y Geófono 4.5 Hz (NO OFERTADO)
- **Requerimiento:** Acelerómetro ADXL345 de 3 ejes (±16g, 13 bits, SPI/I2C) y Geófono de 4.5 Hz a 1 kHz con sensibilidad de 80 V/m/s.
- **Estado de la Propuesta:** **OMISIÓN TOTAL.** No fue cotizado, no tiene precio ni ficha técnica en la propuesta de SERCIA E.I.R.L. Constituye una causal insubsanable de descalificación técnica.

---

## 10. Compatibilidad e Integración entre Componentes

Para verificar la viabilidad técnica del sistema integral, se construyó la siguiente matriz de compatibilidad e interoperabilidad entre los equipos ofertados:

| Componente A | Componente B | Interfaz Necesaria | Compatibilidad Documentada | Evidencia | Componentes Adicionales Indispensables (No Incluidos) | Estado | Riesgo |
|---|---|---|---|---|---|---|---|
| Arduino Nano 33 IoT | Teltonika RUT951 | Datos de telemetría | **INCOMPATIBLE POR CABLE.** Compatible solo por Wi-Fi | RUT951 no tiene USB ni el Arduino tiene RJ45 | Ninguno por Wi-Fi; exige antena y configuración SSID | **CUMPLE PARCIALMENTE** | Saturación del canal inalámbrico local o pérdida de conexión por blindaje metálico. |
| Arduino Nano 33 IoT | Sensirion SPS30 | Datos (I2C o UART) | **COMPATIBLE A NIVEL LÓGICO.** Incompatible en alimentación directa | Pág. 12 (SPS30) y Pág. 61 (Arduino) | Arnés micro JST ZHR-5 a Dupont y Fuente externa de 5V regulada | **CUMPLE PARCIALMENTE** | Daño por sub-tensión en arranque del ventilador o imposibilidad de conexión por falta de arnés. |
| Arduino Nano 33 IoT | TSL2591 (Luminancia) | I2C (SDA/SCL) | **COMPATIBLE EN BUS.** TSL2591 en 0x29 y 3.3V | Pág. 1 y Pág. 63 | Resistencia pull-up en SDA/SCL si el breakout no las incluye | **CUMPLE** | Confusión con TSL2561 y saturación en exteriores. |
| Arduino Nano 33 IoT | DFRobot SEN0463 (Radiación) | Salida digital de pulsos a GPIO | **COMPATIBLE POR GPIO.** Incompatible con USB Serial | Pág. 65-66 (Salida D a pin con ISR) | Cable de conexión Gravity a Dupont (3 hilos) | **CUMPLE PARCIALMENTE** | Carga de CPU por atención de interrupciones externas continuas en el SAMD21. |
| Arduino Nano 33 IoT | INMP441 (Ruido) | Interfaz I2S (SCK, WS, SD) | **COMPATIBLE POR HARDWARE.** | SAMD21 soporta I2S nativo en SERCOM | Cableado directo a pines dedicados (D2, A1, A2, A3) | **CUMPLE PARCIALMENTE** | Complejidad de drivers I2S en SAMD21 y consumo elevado de memoria RAM. |
| Arduino Nano 33 IoT | Sensirion SHT45 (Temp/Hum) | I2C (dirección 0x44) | **COMPATIBLE EN BUS.** Dirección 0x44 no colisiona | Pág. 38 (I2C 0x44) | Placa breakout con pines para inserción (si entregan chip suelto DFN-4) | **CUMPLE PARCIALMENTE** | Imposibilidad de soldar el microchip DFN-4 de 1.5 mm manualmente. |
| Arduino Nano 33 IoT | Rika RK400-04 (Pluviómetro)| Entrada digital (pulsos de reed switch) | **COMPATIBLE ELÉCTRICAMENTE.** | Pág. 36 (reed switch pasivo) | Resistencia pull-up externa (10 kΩ) y condensador antirrebote (0.01 µF) | **CUMPLE** | Conteo espurio de lluvia por rebotes mecánicos del contacto si no se filtra. |
| Red Eléctrica / Fuente | Router RUT951 | Alimentación eléctrica | **COMPATIBLE.** Adaptador 220VAC a 9VDC incluido | Pág. 6 (Power adapter) | Toma de corriente 220VAC en el punto de monitoreo | **CUMPLE** | Dependencia obligatoria de red eléctrica comercial o banco de baterías externo. |
| Red Eléctrica / Fuente | Conjunto Sensores y Arduino | Alimentación eléctrica | **INCOMPATIBLE SIN FUENTE.** | RUT951 entrega 9V y Arduino opera a 3.3V/5V | Fuente de poder reductora regulada de 220VAC a 5VDC (2A) o convertidor DC-DC 9V->5V | **NO CUMPLE** | **Faltante crítico:** no hay forma de energizar el Arduino y los sensores con lo cotizado. |

---

## 11. Requisitos Incumplidos

A continuación se fundamentan técnicamente los **11 requisitos en estado NO CUMPLE**:

1. **REQ-007 (Pines PWM 12 en Controlador):**  
   *Discrepancia:* Se exigieron 12 salidas PWM. La ficha técnica adjunta en la propuesta (Pág. 63) identifica únicamente 5 pines PWM (D3, D5, D6, D9, D10). En la arquitectura de microcontrolador SAMD21 de esta placa se alcanzan hasta 11 salidas PWM mediante configuración avanzada de temporizadores, pero en ningún caso llega a los 12 canales solicitados.
2. **REQ-016 (Interface USB 2.0 en Dispositivo de Comunicación):**  
   *Discrepancia:* Se solicitó interfaz USB 2.0. El router ofertado Teltonika RUT951 **no dispone de puerto USB**. Dispone únicamente de puertos Ethernet RJ45 y Wi-Fi. Esto impide conectar el módem como periférico directo de datos o alimentar dispositivos USB a través de él.
3. **REQ-019 (Alimentación 3.3V - 4.3V en Dispositivo de Comunicación):**  
   *Discrepancia:* Las bases especificaban alimentación de 3.3V a 4.3V (rango característico de baterías Li-ion o módulos módems celulares integrados). El RUT951 requiere obligatoriamente una tensión industrial de **9V a 30V DC**. No puede funcionar bajo el riel de baja tensión de los sensores.
4. **REQ-027 (Rango Dinámico 188 mlux to 88,000 lux en Sensor de Luminancia):**  
   *Discrepancia:* La cotización formal (Pág. 1) declara: *"Rango 0.1 a 40,000 Lux con cambio automático"*. Esta especificación incumple el rango requerido de hasta 88,000 lux y corresponde al sensor desfasado TSL2561, el cual saturará ante radiación solar directa.
5. **REQ-037 (Interface USB Serial en Sensor de Radiación):**  
   *Discrepancia:* Se exigió interfaz USB Serial. El módulo DFRobot SEN0463 no cuenta con puerto USB ni chip conversor serie USB (FTDI/CH340). Posee una interfaz física de 3 pines analógicos/digitales tipo Gravity que emite pulsos digitales que deben ser muestreados por un microcontrolador.
6. **REQ-038 (Alimentación 5V DC USB en Sensor de Radiación):**  
   *Discrepancia:* El módulo se alimenta mediante pines de cabecera estándar de 3.3V a 5V DC, no mediante conector USB ni cable USB.
7. **REQ-064 (Acelerómetro ADXL345 del Sensor Telúrico - Ítem 9):**  
   *Discrepancia:* **Omisión absoluta.** El acelerómetro triaxial de ±16g con resolución de 13 bits e interfaz SPI/I2C no fue cotizado ni descrito en ninguna sección de la propuesta.
8. **REQ-065 (Geófono 4.5Hz - 1kHz del Sensor Telúrico - Ítem 9):**  
   *Discrepancia:* **Omisión absoluta.** El transductor velocimétrico sísmico de 4.5 Hz y sensibilidad de 80 V/m/s fue omitido totalmente en la oferta técnica y económica.
9. **REQ-066 (Completitud Cuantitativa del Lote de 9 Bienes):**  
   *Discrepancia:* Las bases exigen contratar 9 ítems de equipamiento unitario. La cotización de SERCIA E.I.R.L. contiene únicamente 8 ítems, dejando desamparada la línea de monitoreo sísmico.
10. **REQ-067 (Documentación Técnica Oficial Completa):**  
    *Discrepancia:* La propuesta carece de hojas de datos oficiales para el Ítem 4 (Luminancia), Ítem 6 (Ruido) e Ítem 9 (Telúrico), vulnerando el principio de comprobabilidad técnica y veracidad documental.
11. **REQ-068 (Compatibilidad Eléctrica y Fuentes de Alimentación Integral):**  
    *Discrepancia:* El sistema propuesto carece de fuentes de poder intermedias para conciliar los 9-30V del router con los 5V del sensor SPS30 y los 3.3V del Arduino Nano 33 IoT, careciendo también de adaptadores de nivel lógico bidireccionales.

---

## 12. Requisitos Parcialmente Cumplidos

Se identificaron **8 requisitos en estado CUMPLE PARCIALMENTE**:
1. **REQ-005 (Alimentación 5V VIN / 3.3V en Controlador):** Admite 5V en VIN, pero no provee 5V regulados de salida para alimentar periféricos si no está enchufado por USB y con el puente VUSB soldado. Sus pines lógicos son de 3.3V no tolerantes a 5V.
2. **REQ-012 (Consumo 15-20 mA en Controlador):** El SAMD21 en modo activo básico cumple con 15-20 mA, pero al transmitir por Wi-Fi mediante el u-blox NINA-W102 el consumo asciende a picos de 150-200 mA.
3. **REQ-025 (Precisión ±10% en Calidad de Aire SPS30):** La precisión de ±10% se garantiza documentalmente solo para PM1.0 y PM2.5 en concentraciones superiores a 100 µg/m³. En concentraciones bajas la incertidumbre es de ±5 µg/m³, y para PM4.0 y PM10 la tolerancia de fábrica es de ±25%.
4. **REQ-035 (Rango 0.08-1200 µSv/h en Radiación):** El rango superior alcanza 1200 µSv/h de forma teórica, pero el límite inferior de 0.08 µSv/h no cuenta con calibración certificada.
5. **REQ-040 (Plazo de Entrega en Radiación):** La propuesta establece 30 días calendario por condición de importación, desfasando el plazo general del proyecto que es de 10 días.
6. **REQ-041 (Uso Previsto del Sensor de Radiación):** El fabricante explicita que es un dispositivo para experimentación didáctica y no un instrumento calibrado de seguridad radiológica.
7. **REQ-049 (Funcionalidad de Ruido Ambiental en INMP441):** Cumple con la adquisición de audio acústico en bruto por I2S, pero no es un sonómetro; requiere desarrollo de software de filtrado ponderado A y calibración SPL en sitio.
8. **REQ-062 (Alimentación 5-12V DC en Pluviómetro):** El sensor es un reed switch de contacto seco libre de potencial. Si se deseara salida activa industrial RS485, exige 12-24V DC.

---

## 13. Requisitos No Verificables

Se identificaron **4 requisitos en estado NO VERIFICABLE**:
1. **REQ-033 (Procedencia y Ficha Técnica de Luminancia):** Se declara marca "nacional" para un componente cuyo chip es ams-OSRAM y no se suministra ficha técnica de la placa breakout.
2. **REQ-048 (Procedencia y Ficha Técnica de Ruido Ambiental):** Se declara marca "nacional" para el micrófono MEMS de TDK InvenSense sin adjuntar hoja de datos del módulo PCB integrado.
3. **REQ-057 (Presentación Física de SHT45):** La ficha técnica adjunta corresponde al microchip desnudo SMD DFN-4 de 1.5 x 1.5 mm. No es posible verificar si el postor entregará un módulo breakout soldable o el componente suelto no integrable.
4. **REQ-063 (Nomenclatura y Cable del Pluviómetro RK400-04):** No se especificó el sufijo de pedido en la cotización, impidiendo verificar la variante de interfaz ni la longitud de cable suministrada.

---

## 14. Contradicciones y Ambigüedades Documentales

### 14.1 Contradicción Crítica en el Sensor de Luminancia (REQ-032)
En la Página 1 de la cotización formal, el proveedor cotiza el modelo **TSL2591**, pero en la columna de observaciones describe:
- *"Rango 0.1 a 40,000 Lux con cambio automático"*
- *"3 direcciones I2C seleccionables (0x29 / 0x39 / 0x49)"*
- *"Permite múltiples sensores en el mismo bus I2C"*

**Demostración Técnica de la Contradicción:**
- El sensor **TSL2591** auténtico de ams-OSRAM tiene una dirección I2C estricta y cableada internamente a **0x29** (sin pines de configuración de dirección externa) y un rango de **188 µlux a 88,000 lux**.
- El sensor **TSL2561** posee exactamente 3 direcciones I2C seleccionables por pin (0x29, 0x39, 0x49) y un rango máximo de **40,000 Lux**.
- **Conclusión:** El proveedor ha transcrito las características del chip inferior TSL2561 bajo el nombre del TSL2591, lo que constituye un indicio fundado de que entregará un sensor que saturará a 40,000 lux y no cumplirá con las bases técnicas.

---

## 15. Componentes, Accesorios o Licencias Faltantes

Para garantizar que el sistema opere integralmente, se identifican los siguientes elementos indispensables no incluidos en la propuesta económica evaluada:

1. **Arnés de Conexión Especial para Sensirion SPS30:** El sensor dispone de una clavija micro JST ZHR-5 de 5 pines (pitch 1.5 mm). Se requiere obligatoriamente el cable conector original JST a cables Dupont macho/hembra.
2. **Fuente de Alimentación Regulada de 5V DC (mínimo 2A):** Indispensable para energizar el sensor SPS30 (5V), el sensor de radiación (5V) y el controlador Arduino (vía pin 5V tras puente o vía USB).
3. **Desplazador de Nivel Lógico Bidireccional (Logic Level Shifter 3.3V <-> 5V):** Necesario para interconectar líneas de comunicación entre dispositivos de 5V y el Arduino Nano 33 IoT sin dañar los pines del microcontrolador SAMD21.
4. **Placas de Adaptación (Breakout Boards) con Cabecera de Pines:** Para los sensores SHT45 e INMP441 si no vienen provistos en módulos montados.
5. **Gabinete y Protección Ambiental (Caja Estanca IP65 / IP66):** Requerido para albergar el controlador, el router RUT951, los bloques de terminales y las fuentes en condiciones de intemperie.
6. **Módulo Acondicionador de Señal para Geófono Sísmico (Ítem 9):** Los geófonos de 4.5 Hz entregan tensiones en el rango de microvoltios/milivoltios; se requiere un amplificador de instrumentación de bajo ruido (INA) y filtro pasa-banda activo para que el ADC del microcontrolador pueda registrar vibraciones sísmicas.
7. **Tarjeta SIM de Datos Celulares 4G:** Con plan activo M2M/IoT y APN configurado para el router Teltonika RUT951.

---

## 16. Riesgos Técnicos y Operativos

Se ha elaborado la siguiente matriz de riesgos técnicos derivados de las discrepancias documentales:

| Riesgo Identificado | Causa Raíz | Probabilidad | Impacto | Severidad | Medida de Mitigación Requerida |
|---|---|---|---|---|---|
| **Omisión del subsistema sísmico** | Ítem 9 no cotizado en la propuesta | Alta (100%) | Crítico | **CRÍTICA** | No adjudicar la compra sin la inclusión y cotización formal del Ítem 9 completo. |
| **Destrucción de pines del microcontrolador** | Incompatibilidad de niveles lógicos 5V en Arduino Nano 33 IoT | Alta (80%) | Grave | **ALTA** | Incorporar obligatoriamente convertidores de nivel lógico 3.3V/5V. |
| **Inoperatividad del sensor SPS30** | Falta de arnés JST ZHR-5 y falta de riel de 5V regulado | Alta (90%) | Grave | **ALTA** | Exigir al postor la entrega del cable de fábrica y proveer fuente externa de 5V. |
| **Saturación en lecturas de luminancia** | Suministro de sensor con tope en 40,000 lux (TSL2561) | Alta (85%) | Moderado | **MEDIA** | Rechazar el componente y exigir TSL2591 auténtico de 88,000 lux. |
| **Falsas mediciones de radiación** | Uso de placa didáctica SEN0463 expuesta a luz solar o sin calibrar | Alta (70%) | Moderado | **MEDIA** | Proteger el tubo Geiger de la luz solar y registrar lecturas como referenciales. |
| **Incapacidad de soldar el sensor SHT45** | Entrega de circuito integrado SMD DFN-4 suelto | Media (50%) | Grave | **ALTA** | Condicionar la recepción a que el sensor venga montado en PCB breakout. |
| **Corte de energía e incompatibilidad de tensión** | Router RUT951 requiere 9-30V y no puede operar con 3.3V/5V | Alta (100%) | Grave | **ALTA** | Habilitar toma de 220VAC en sitio o instalar bus común de 12V con conversor DC-DC. |

---

## 17. Consultas que Deben Formularse al Proveedor

Previo a cualquier decisión contractual, la entidad debe cursar al proveedor SERCIA E.I.R.L. el siguiente pliego de consultas técnicas perentorias:

1. **Sobre el Ítem 9 (Sensor Telúrico):** Sírvase aclarar por qué fue omitido de la cotización económica y técnica el Ítem 9 (Acelerómetro ADXL345 y Geófono 4.5 Hz). Indique si mantiene la capacidad de suministrarlo dentro del presupuesto o precise la cotización complementaria correspondiente con su respectiva ficha técnica.
2. **Sobre el Ítem 4 (Sensor de Luminancia):** Sírvase aclarar la contradicción documental entre el modelo declarado (TSL2591) y las especificaciones descritas (0.1 a 40,000 Lux y 3 direcciones I2C seleccionables, propias del TSL2561). Confirme si el producto suministrado alcanza los 88,000 Lux y adjunte la ficha técnica del fabricante original.
3. **Sobre el Ítem 2 (Dispositivo de Comunicación):** Considerando que el router Teltonika RUT951 ofertado carece de interfaz USB 2.0 y requiere alimentación de 9V a 30V DC (a diferencia de los 3.3V-4.3V solicitados), precise cómo garantizará la interconexión con el controlador y aclare si suministra los accesorios necesarios para su integración en gabinete.
4. **Sobre el Ítem 5 (Sensor de Radiación):** Confirme cómo se integrará el módulo SEN0463 ante la ausencia de puerto USB Serial y justifique el plazo de entrega de 30 días calendario frente a los 10 días exigidos en las bases.
5. **Sobre el Ítem 7 (Sensor SHT45):** Confirme formalmente si el sensor SHT45 se entregará montado sobre una placa de circuito impreso (breakout board) con terminales macho/hembra estándar de 2.54 mm aptos para conexión directa, o en formato de componente suelto SMD DFN-4.
6. **Sobre el Ítem 3 (Sensor SPS30):** Confirme si la oferta incluye el cable de interfaz con conector propietario JST ZHR-5 de 5 pines para su enlace al microcontrolador.
7. **Sobre el Ítem 8 (Pluviómetro RK400-04):** Especifique el part number exacto ofertado, indicando si la salida corresponde a pulso pasivo (Código A) o transmisión industrial RS485 (Código B), así como la longitud del cable suministrado.

---

## 18. Acciones Correctivas Necesarias

Para viabilizar la ejecución del proyecto de monitoreo, se deben adoptar las siguientes medidas correctivas:

1. **Requerir Subsanación Formal o Re-cotización:** Exigir al postor la subsanación de la omisión del Ítem 9 y la rectificación de las fichas técnicas y modelos de los Ítems 2, 4 y 5.
2. **Aprobación de Arquitectura de Potencia:** Aprobar un esquema de alimentación basado en una fuente de poder industrial conmutada de 12V DC (para el router RUT951) y un regulador reductor conmutado (Step-Down / Buck) de 12V a 5V DC (3A) para energizar el Arduino Nano 33 IoT y el sensor SPS30, evitando sobrecargar el regulador interno del microcontrolador.
3. **Inclusión de Accesorios de Interconexión en la Adquisición:** Condicionar la adjudicación a la entrega obligatoria del arnés JST para SPS30, cables Gravity para SEN0463, módulos breakout para SHT45 e INMP441, y un módulo conversor de nivel lógico 3.3V-5V de 4 u 8 canales.

---

## 19. Conclusión Técnica sobre la Documentación Presentada

Tras una rigurosa evaluación multidimensional realizada por especialistas en hardware embebido, telemetría IoT, software y aseguramiento metrológico:

1. **La propuesta presentada por SERCIA E.I.R.L. es técnica y documentalmente DEFICIENTE e INCOMPLETA.**
2. Existe un **incumplimiento sustancial insoslayable: la omisión del Ítem 9 (Sensor Telúrico)**, lo que priva al proyecto de la instrumentación sísmica estructural programada.
3. Existen **incumplimientos severos de especificación e incompatibilidades de hardware** en el dispositivo de comunicación (RUT951 sin USB y con voltaje de 9-30V), sensor de luminancia (cotización de características del TSL2561 en vez de TSL2591) y sensor de radiación (módulo sin puerto USB Serial y con plazo desfasado de 30 días).
4. El lote ofertado **no puede ensamblarse como un sistema operativo autosuficiente** debido a la omisión de cables especiales, fuentes de poder compatibles y adaptación de niveles de voltaje.

---

## 20. Recomendación de Decisión y Condiciones Previas

### 20.1 Recomendación
**SE RECOMIENDA NO APROBAR LA PROPUESTA DE ADQUISICIÓN DE SERCIA E.I.R.L. EN SU ESTADO ACTUAL.**  
Aprobar la propuesta en estas condiciones vulneraría la directriz crítica de no realizar gastos complementarios posteriores y condenaría al proyecto a contar con equipos incompatibles, incompletos e incapaces de cumplir los fines de investigación trazados por la UNSA.

### 20.2 Condiciones Previas Indispensables para una Eventual Reevaluación
Únicamente si la normativa de contratación de la entidad permite la subsanación de ofertas antes de la adjudicación, se podrá reconsiderar la propuesta si el proveedor cumple acumulativamente con:
1. Cotizar e incorporar formalmente el **Ítem 9 completo** (Acelerómetro ADXL345 + Geófono de 4.5 Hz con circuito acondicionador).
2. Rectificar la oferta del **Ítem 4**, garantizando el modelo TSL2591 auténtico con rango de 88,000 lux y adjuntando la ficha técnica del fabricante.
3. Acreditar documentalmente que el sensor **SHT45 (Ítem 7)** y el micrófono **INMP441 (Ítem 6)** se entregan montados en placas breakout con pines accesibles.
4. Incluir formalmente sin costo adicional el **arnés conector JST ZHR-5** para el sensor SPS30, los cables de interfaz y un convertidor de niveles lógicos 3.3V/5V.
5. Presentar una solución técnica validada para la alimentación coordinada del router RUT951 (9-30V) y los sensores (5V/3.3V), garantizando el funcionamiento conjunto del sistema.
""")

    report_content = "\n".join(report_lines)
    dest_path = r"d:\Proyectos\Arquitectura\informe\01_informe_auditoria_cumplimiento.md"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Report generated successfully: {dest_path} ({len(report_content)} characters)")

if __name__ == "__main__":
    generate_report()
