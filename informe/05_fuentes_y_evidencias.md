# INVENTARIO DOCUMENTAL DE FUENTES Y REGISTRO DE EVIDENCIAS TÉCNICAS

**Proyecto:** Sistema de Monitoreo Ambiental y Estructural con Telemetría IoT  
**Entidad Contratante:** Universidad Nacional de San Agustín de Arequipa (UNSA)  
**Propósito:** Respaldar con trazabilidad documental, referencias bibliográficas, normas metrológicas y enlaces web oficiales todas las afirmaciones, juicios técnicos y evaluaciones emitidas en la auditoría.  
**Fecha:** 19 de Octubre de 2026  

---

## 1. Fuentes Documentales Internas del Proyecto

Las fuentes internas corresponden a los archivos originales provistos en el repositorio de trabajo, los cuales fueron inspeccionados sin alteración física ni modificación de metadatos:

### 1.1 Documento de Requerimientos - Imagen 1
- **Nombre de Archivo:** `Fuentes/Requerimientos_1`
- **Formato y Tamaño:** Imagen JPEG, 82,524 bytes (80.5 KB).
- **Resolución:** 899 x 923 píxeles.
- **Sección Identificada:** Sección 6 "CARACTERÍSTICAS Y CONDICIONES DE LOS BIENES A CONTRATAR", Subsección 6.1 "Descripción de los bienes a contratar".
- **Contenido Verificado:**
  - Encabezado de tabla: `ITEM` | `CANTIDAD` | `UNIDAD DE MEDIDA` | `DESCRIPCIÓN DEL BIEN`.
  - Ítems 1 al 5 completos (Controlador, Dispositivo de comunicación, Sensor de Calidad de Aire, Sensor de Luminancia, Sensor de Radiación).
  - Corte inferior: La imagen corta al final de la celda de descripción del Ítem 5 e inicio del texto "Sensor de Ruido Ambiental".
- **Estado de Conservación:** Íntegramente legible.

### 1.2 Documento de Requerimientos - Imagen 2
- **Nombre de Archivo:** `Fuentes/Requerimientos_2`
- **Formato y Tamaño:** Imagen JPEG, 92,839 bytes (90.6 KB).
- **Resolución:** 899 x 681 píxeles.
- **Sección Identificada:** Continuación del Numeral 6.1 de las bases de contratación.
- **Contenido Verificado:**
  - Línea superior: Texto residual "• Energía 0.5W" correspondiente al cierre del Ítem 5.
  - Ítems 6 al 8 completos (Sensor de Ruido Ambiental, Sensor de Temperatura y Humedad Ambiental, Sensor Pluviómetro).
  - Ítem 9 (Sensor Telúrico): Título e inicio de celda en la tabla principal y recuadro inferior desprendido con las especificaciones del acelerómetro ADXL345 y geófono de 4.5 Hz.
  - Sellos y Visados Institucionales Oficiales:
    - Sello 1: "MONITOR DE PROYECTOS / V° B° / UNIDAD DE GESTION DE LA INVESTIGACION / UGINY - UNSA / Maria Nelly Pezo Torres / 15/07/2026".
    - Sello 2: "GESTOR ADMINISTRATIVO / V° B° / UGINY - UNSA / UNIDAD DE GESTION DE LA INVESTIGACION / PATRICIA MONJARAS DEL CARPIO / 14/07/2026".
- **Estado de Conservación:** Íntegramente legible.

### 1.3 Expediente de Cotización del Proveedor
- **Nombre de Archivo:** `Fuentes/PROPUESTA 1.pdf`
- **Formato y Tamaño:** Documento PDF (versión 1.4 / multipágina), 3,228,942 bytes (3.07 MB).
- **Número Total de Páginas:** 66 páginas.
- **Desglose Estructural del Contenido:**
  1. **Páginas 1 y 2:** Declaración Jurada de Cotización (Bienes) de SERCIA E.I.R.L. (RUC 2060469242), emitida el 09/08/2026, firmada y sellada por Emerson Valdivia Cartagena. Contiene cuadro de oferta económica con 8 ítems, total S/. 3,685.00.
  2. **Páginas 3 a 8:** Teltonika Networks - *RUT951 Quick Start Guide v1.0* (Guía rápida de instalación, hardware, luces LED, pinout del conector de poder y declaración CE).
  3. **Páginas 9 a 34:** Sensirion AG - *Datasheet SPS30: Particulate Matter Sensor for Air Quality Monitoring and Control* (Versión 2.0 - D1 - Junio 2023, 26 páginas completas).
  4. **Páginas 35 a 37:** Hunan Rika Electronic Technology Co., Ltd. - *RK400-04 Economical Tipping Bucket Rainfall Sensor Datasheet* (Versión 3.0, 3 páginas completas).
  5. **Páginas 38 a 59:** Sensirion AG - *Datasheet SHT4x: 4th Generation High-Accuracy Ultra-Low-Power 16-bit Relative Humidity and Temperature Sensor* (Versión 5 - Enero 2023, 22 páginas completas).
  6. **Páginas 60 a 64:** AG Electrónica S.A.P.I. de C.V. - Ficha técnica comercial para *ABX00027: Placa de Desarrollo Arduino Nano 33 IoT* (Fecha: 18/06/2019, 5 páginas).
  7. **Páginas 65 a 66:** AG Electrónica S.A.P.I. de C.V. - Ficha técnica comercial para *SEN0463: Detector de Radiación Ionizante (Contador Geiger)* de DFRobot (Fecha: 17/11/2022, 2 páginas).
- **Omisiones Documentales Detectadas en el PDF:**
  - Ausencia absoluta de ficha técnica del Ítem 4 (TSL2591).
  - Ausencia absoluta de ficha técnica del Ítem 6 (INMP441).
  - Ausencia absoluta de cotización y ficha técnica del Ítem 9 (Sensor Telúrico).

---

## 2. Fuentes Técnicas Externas y Fichas Oficiales de Fabricantes

Para dirimir contradicciones metrológicas y contrastar las especificaciones físicas reales de los componentes, el equipo auditor consultó la documentación oficial de los fabricantes originales de los semiconductores:

### 2.1 Microcontrolador y Plataforma de Desarrollo (Arduino Nano 33 IoT)
- **Fabricante:** Arduino S.r.l. / Microchip Technology Inc.
- **Documento 1:** *Arduino Nano 33 IoT Datasheet & Schematic Reference*, Documentación oficial de hardware Arduino.  
  URL: `https://docs.arduino.cc/hardware/nano-33-iot` (Consultado: 19/10/2026).
- **Documento 2:** Microchip Technology Inc., *SAM D21/DA1 Family Complete Datasheet (DS40001882G)*. Microcontrolador ARM Cortex-M0+ de 32 bits y 48 MHz.  
  URL: `https://www.microchip.com/en-us/product/ATSAMD21G18` (Consultado: 19/10/2026).
- **Documento 3:** u-blox AG, *NINA-W10 series Stand-alone Wi-Fi and Bluetooth modules System Integration Manual*.  
  URL: `https://content.u-blox.com/sites/default/files/NINA-W10_SIM_UBX-17005730.pdf` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** Comprobación de que la placa opera exclusivamente con niveles lógicos de 3.3V (no tolerante a 5V) y que el pin de 5V no entrega energía a menos que se suelde el jumper VUSB.

### 2.2 Router Celular Industrial (Teltonika RUT951)
- **Fabricante:** Teltonika Networks UAB (Vilna, Lituania).
- **Documento:** *RUT951 Technical Specifications and Hardware Interfaces Wiki*.  
  URL: `https://wiki.teltonika-networks.com/view/RUT951` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** Verificación física de interfaces: RUT951 carece absolutamente de puerto USB 2.0 (posee 4 puertos RJ45 y Wi-Fi) y su tensión de alimentación permitida es de 9V a 30V DC (no 3.3V a 4.3V).

### 2.3 Sensor de Calidad de Aire (Sensirion SPS30)
- **Fabricante:** Sensirion AG (Stäfa, Suiza).
- **Documento:** *Datasheet SPS30: Particulate Matter Sensor for Air Quality Monitoring and Control*, Versión 2.0 (Junio 2023).  
  URL: `https://sensirion.com/products/catalog/SPS30` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** Requerimiento estricto de conector hembra JST ZHR-5, tolerancia de alimentación de 4.5V a 5.5V (5V ±10%), consumo de 80 mA en arranque de turbina y precisión metrológica por fracciones PM.

### 2.4 Sensor de Luminancia (ams-OSRAM TSL2591 vs TSL2561)
- **Fabricante:** ams-OSRAM AG (Premstaetten, Austria).
- **Documento 1:** *TSL2591 High Sensitivity Light-to-Digital Converter Datasheet (DS000338)*.  
  URL: `https://ams-osram.com/products/sensor-solutions/ambient-light-sensors/ams-tsl2591-ambient-light-sensor` (Consultado: 19/10/2026).
- **Documento 2:** *TSL2561 Light-to-Digital Converter Datasheet*.  
  URL: `https://ams-osram.com/products/sensor-solutions/ambient-light-sensors/ams-tsl2561-ambient-light-sensor` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** 
  - El sensor TSL2591 alcanza **88,000 lux** con dirección I2C estricta y fija en **0x29**.
  - El sensor TSL2561 alcanza un máximo de **40,000 lux** y dispone de **3 direcciones seleccionables (0x29 / 0x39 / 0x49)**.
  - Esto evidencia que el proveedor copió la descripción del TSL2561 para el Ítem 4.

### 2.5 Sensor de Radiación Ionizante (DFRobot SEN0463)
- **Fabricante:** DFRobot (Shanghái, China).
- **Documento:** *DFRobot Gravity: Geiger Counter Module User Manual and Technical Guide (SKU: SEN0463)*.  
  URL: `https://wiki.dfrobot.com/SKU_SEN0463_Gravity_Geiger_Counter_Module` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** El módulo emite pulsos digitales activos en bajo (Active-Low) en el pin digital `D` mediante conector Gravity de 3 pines. Carece totalmente de bus o controlador USB Serial.

### 2.6 Micrófono MEMS Acústico (TDK InvenSense INMP441)
- **Fabricante:** InvenSense Inc. / TDK Corporation (San José, California, EE.UU.).
- **Documento:** *INMP441: Omnidirectional Microphone with I2S Digital Output Datasheet*.  
  URL: `https://invensense.tdk.com/products/digital/inmp441/` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** Transductor con salida digital I2S de 24 bits. Entrega audio en bruto (PCM), requiriendo procesamiento DSP (filtro A y RMS) en microcontrolador para calcular decibelios ambientales.

### 2.7 Sensor de Temperatura y Humedad (Sensirion SHT45)
- **Fabricante:** Sensirion AG (Stäfa, Suiza).
- **Documento:** *Datasheet SHT4x: 4th Generation High-Accuracy Relative Humidity and Temperature Sensor*, Versión 5 (Enero 2023).  
  URL: `https://sensirion.com/products/catalog/SHT45` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** Precisión metrológica de $\pm 0.1^\circ C$ y $\pm 1.0\% RH$ con certificación ISO 17025 y trazabilidad NIST. Factor de forma DFN-4 de montaje superficial de 1.5 x 1.5 mm.

### 2.8 Sensor Pluviómetro (Rika Sensors RK400-04)
- **Fabricante:** Hunan Rika Electronic Technology Co., Ltd. (Changsha, China).
- **Documento:** *RK400-04 Economical Tipping Bucket Rainfall Sensor User Manual*, Versión 3.0.  
  URL: `http://www.rikasensor.com.cn` (Consultado: 19/10/2026).
- **Evidencias Contrastadas:** Resolución de balancín de 0.2 mm por vaciado, capacidad máxima admisible de 480 mm/h (8 mm/min), contacto magnético reed switch pasivo.

### 2.9 Sensor Telúrico (ADXL345 y Geófono 4.5 Hz)
- **Fabricante ADXL345:** Analog Devices Inc. (Wilmington, Massachusetts, EE.UU.).  
  *Documento:* ADXL345 3-Axis, ±2g/±4g/±8g/±16g Digital Accelerometer Datasheet (Rev. G).  
  URL: `https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf` (Consultado: 19/10/2026).
- **Geófono Sísmico 4.5 Hz:** Instrumentación estándar geofísica (bobina móvil suspendida en campo magnético con frecuencia de resonancia de 4.5 Hz y sensibilidad nominal de 80 V/m/s).

---

## 3. Normativa y Estándares Metrológicos Aplicados en la Evaluación

1. **IEC 61672-1:2013:** *Electroacoustics - Sound level meters - Part 1: Specifications.* Estándar internacional para ponderación frecuencial A ($dBA$) y medición de nivel sonoro equivalente ($L_{Aeq}$).
2. **ISO/IEC 17025:2017:** *Requisitos generales para la competencia de los laboratorios de ensayo y calibración.* Aplicado para valorar la trazabilidad metrológica de los sensores de temperatura y calidad de aire.
3. **Directiva RED 2014/53/EU:** *Radio Equipment Directive.* Directiva de la Unión Europea sobre compatibilidad electromagnética y seguridad de equipos con radiofrecuencia (aplicada a Teltonika RUT951 y Arduino Nano 33 IoT).
4. **D.S. N° 003-2017-MINAM (Perú):** *Estándares de Calidad Ambiental (ECA) para Aire.* Marco normativo peruano de referencia para concentraciones máximas permisibles de PM2.5 y PM10 en el dashboard de monitoreo.
5. **D.S. N° 085-2003-PCM (Perú):** *Reglamento de Estándares Nacionales de Calidad Ambiental para Ruido.* Valores de referencia para zonificación acústica urbana en horarios diurnos y nocturnos.
