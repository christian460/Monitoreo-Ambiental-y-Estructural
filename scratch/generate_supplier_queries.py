# -*- coding: utf-8 -*-
"""
Script to generate informe/04_consultas_al_proveedor.md
"""
import os

def generate_supplier_queries():
    lines = []
    lines.append("""# PLIEGO DE CONSULTAS Y REQUERIMIENTO DE ACLARACIÓN TÉCNICA AL PROVEEDOR

**Destinatario:** SERCIA E.I.R.L. (RUC: 2060469242)  
**Representante Legal / Comercial:** Emerson Valdivia Cartagena  
**Referencia del Proceso:** Declaración Jurada de Cotización de Bienes - Sistema de Monitoreo Ambiental IoT (09/08/2026)  
**Entidad Solicitante:** Universidad Nacional de San Agustín de Arequipa (UNSA) - Unidad de Gestión de la Investigación (UGINY)  
**Fecha de Emisión:** 19 de Octubre de 2026  
**Carácter del Documento:** Requerimiento Técnico Previo y Vinculante  

---

## 1. Contexto y Advertencia Previa

En el marco de la auditoría técnica documental efectuada a la propuesta presentada por su representada para la provisión de equipos de monitoreo, telemetría y sensores, se han identificado **omisiones sustanciales, discrepancias metrológicas, contradicciones técnicas e incompatibilidades de hardware** que comprometen la viabilidad operativa del sistema.

> [!CRITICAL]
> **Condición Contractual Determinante:** Por directriz presupuestaria y normativa del proyecto, **una vez aprobada la oferta y emitidas las órdenes de compra, NO se autorizarán compras complementarias ni adiciones para subsanar omisiones, incompatibilidades o carencias de accesorios.** Todos los bienes y elementos indispensables para el funcionamiento armónico e integral deben estar comprendidos y aclarados antes de la adjudicación.

Por consiguiente, se solicita a **SERCIA E.I.R.L.** absolver de manera formal, detallada y documentada el siguiente pliego de consultas en un plazo perentorio.

---

## 2. Pliego de Consultas Técnicas Priorizadas

### Bloque A: Omisiones Críticas e Incompletitud de la Oferta (Prioridad Máxima - Bloqueante)

#### Consulta 1: Omisión Total del Ítem 9 (Sensor Telúrico)
- **Requerimiento en Bases (Imagen 2):** Se exige contratar 1 unidad del *Sensor Telúrico*, compuesto por:
  - Acelerómetro triaxial ADXL345 (rango $\pm 16g$, resolución 13 bits, interfaz SPI/I2C).
  - Geófono de baja frecuencia (rango 4.5 Hz - 1 kHz, sensibilidad 80 V/m/s).
- **Situación en su Propuesta:** En la Declaración Jurada de Cotización (Página 1 de `PROPUESTA 1.pdf`), su oferta económica concluye en el Ítem 8 por un monto de S/. 3,685.00, omitiendo por completo el Ítem 9. Tampoco se adjuntó ficha técnica ni descripción alguna de este componente en el expediente.
- **Requerimiento:**
  1. Aclare si su representada mantendrá el suministro del Ítem 9 dentro del proceso de contratación.
  2. En caso afirmativo, remita formalmente la cotización complementaria desglosada y las fichas técnicas oficiales del acelerómetro ADXL345 y del geófono de 4.5 Hz ofertados.
  3. Precise si el geófono incluirá circuito preamplificador y acondicionador de señal para su conexión al convertidor analógico del microcontrolador.

---

### Bloque B: Contradicciones Metrológicas y Sustitución de Modelos (Prioridad Alta)

#### Consulta 2: Discrepancia Técnica en el Sensor de Luminancia (Ítem 4)
- **Requerimiento en Bases (Imagen 1):** Rango dinámico de **188 mlux a 88,000 lux**, resolución ADC 16 bits, interfaz I2C, longitud de onda 300-1000 nm, alimentación 3.3V DC.
- **Situación en su Propuesta:** En el cuadro de cotización consigna modelo *TSL2591* y marca *nacional*, pero en la columna de observaciones describe textualmente:
  - *"Rango 0.1 a 40,000 Lux con cambio automático"*
  - *"3 direcciones I2C seleccionables (0x29 / 0x39 / 0x49)"*
- **Sustento de la Contradicción:** El chip ams-OSRAM TSL2591 alcanza 88,000 lux y posee una única dirección fija (0x29). Las características descritas por usted (0.1 a 40,000 lux y 3 direcciones) corresponden al modelo inferior y desfasado TSL2561, el cual saturará ante luz solar intensa.
- **Requerimiento:**
  1. Confirme categóricamente cuál es el modelo exacto que suministrará: ¿TSL2591 (hasta 88,000 lux) o TSL2561 (hasta 40,000 lux)?
  2. Adjunte la hoja de datos (datasheet) oficial del fabricante del módulo que se entregará físicamente.
  3. Rectifique la marca declarada ("nacional") indicando el fabricante real del módulo de circuito impreso.

---

### Bloque C: Incompatibilidades Físicas, de Interfaz y Alimentación (Prioridad Alta)

#### Consulta 3: Interfaz y Rango de Alimentación del Router Celular (Ítem 2 - Teltonika RUT951)
- **Requerimiento en Bases (Imagen 1):** Interfaz **USB 2.0**, alimentación **3.3V - 4.3V**, bandas LTE B1/B3/B5/B7/B8/B20, 2 antenas SMA externas.
- **Situación en su Propuesta:** Oferta el router industrial Teltonika RUT951. La documentación oficial del equipo acredita que:
  - **NO cuenta con puerto USB 2.0 ni interfaz USB.** Dispone únicamente de puertos Ethernet RJ45 y Wi-Fi.
  - Su tensión de alimentación nominal es de **9V a 30V DC** (incompatible con 3.3V - 4.3V).
- **Requerimiento:**
  1. Aclare cómo se conectará este dispositivo con el controlador Arduino Nano 33 IoT al no existir bus USB entre ambos. ¿La conexión prevista será exclusivamente inalámbrica vía Wi-Fi local?
  2. Indique si su oferta incluye una fuente de poder o convertidor de voltaje común capaz de suministrar simultáneamente 9-30V para el router y 5V/3.3V para el microcontrolador y sensores, o si la entidad deberá alimentarlos por separado con tomas independientes de 220VAC.

#### Consulta 4: Interfaz de Comunicación y Salida del Sensor de Radiación (Ítem 5 - DFRobot SEN0463)
- **Requerimiento en Bases (Imagen 1):** Interfaz **USB Serial** y alimentación **5V DC USB**.
- **Situación en su Propuesta:** Oferta el módulo DFRobot SEN0463 con tubo Geiger M4011. Dicho módulo carece de conector USB y de conversor serie USB (FTDI/CH340), presentando únicamente un conector Gravity de 3 pines que emite pulsos digitales para ser leídos por interrupciones GPIO.
- **Requerimiento:**
  1. Aclare si el sensor se suministrará con un módulo conversor externo USB-Serial (USB a TTL) para cumplir con la interfaz requerida en bases, o si la entrega consistirá en la placa didáctica Gravity sin puerto USB.
  2. Confirme si se incluye el cable de interfaz para conectar la salida de pulsos a los pines de cabecera del microcontrolador.

---

### Bloque D: Formato Físico, Módulos Breakout y Montaje en Campo (Prioridad Media-Alta)

#### Consulta 5: Presentación Física del Sensor SHT45 (Ítem 7)
- **Situación en su Propuesta:** Adjuntó la ficha técnica de Sensirion correspondiente al circuito integrado de montaje superficial (SMD) encapsulado DFN-4 de 1.5 x 1.5 x 0.5 mm en empaque industrial de cinta y carrete (*tape and reel*).
- **Requerimiento:**
  1. Confirme formalmente si el sensor SHT45 se entregará **montado sobre una placa de circuito impreso (breakout board) con terminales estándar tipo cabecera (pitch 2.54 mm)**, o si pretende entregar el chip suelto SMD.
  2. *Nota de Advertencia:* La entrega del chip suelto en cinta será causal de rechazo en recepción de almacén por imposibilidad física de integración en campo.

#### Consulta 6: Ficha Técnica y Fabricante del Sensor de Ruido Ambiental (Ítem 6 - INMP441)
- **Situación en su Propuesta:** Declaró marca "nacional" y omitió adjuntar la hoja de datos técnicos en el expediente.
- **Requerimiento:**
  1. Remita la ficha técnica oficial del módulo ofertado.
  2. Confirme si el micrófono se entrega en una placa breakout con pines soldados y orificio acústico protegido.

#### Consulta 7: Configuración de Fábrica del Pluviómetro (Ítem 8 - Rika Sensors RK400-04)
- **Situación en su Propuesta:** En el catálogo del fabricante (Pág. 37 de su PDF) se indican múltiples opciones: Salida A (Pulsos de reed switch), Salida B (Transmisión RS485), y longitudes de cable de 1.5 m o 3.0 m. En la cotización solo consigna "RK400-04".
- **Requerimiento:**
  1. Precise el código de producto exacto ofertado.
  2. Confirme si la salida es contacto seco por pulsos (Código A) o interfaz serie RS485 (Código B).
  3. Indique la longitud exacta de cable resistente a intemperie incluido en el suministro.

---

### Bloque E: Accesorios Críticos Indispensables (Prioridad Alta)

#### Consulta 8: Conectores y Cables Propietarios de Sensores
- **Situación:** El sensor de calidad de aire Sensirion SPS30 utiliza una clavija miniatura propietaria **JST ZHR-5**. La cotización no detalla si se incluye el cable de fábrica.
- **Requerimiento:**
  1. Confirme expresamente si el ítem 3 incluye el cable de conexión oficial JST ZHR-5 a terminales Dupont hembra/macho.

---

### Bloque F: Plazos de Entrega y Condiciones Comerciales (Prioridad Administrativa)

#### Consulta 9: Desfase en el Plazo de Entrega del Sensor de Radiación
- **Situación:** Las bases y todos los demás ítems de su oferta establecen un plazo de entrega de **10 días calendario**. Para el Ítem 5 (Sensor de Radiación), su cotización consigna **30 días calendario** con la anotación *"importacion"*.
- **Requerimiento:**
  1. Confirme si dispone de stock local o si puede reducir el plazo a 10 días para alinearse al cronograma integral del proyecto.
  2. En caso de requerir indefectiblemente 30 días, aclare si su empresa asumirá las entregas parciales formales sin costo adicional para la universidad.

---

## 3. Instrucciones para la Respuesta del Proveedor

Las respuestas a este pliego deben cumplir con los siguientes requisitos formales:
1. Ser remitidas mediante carta formal firmada digitalmente por el Representante Legal de **SERCIA E.I.R.L.**
2. Acompañar las **hojas de datos técnicos completas (datasheets)** emitidas por los fabricantes originales de los ítems observados (ams-OSRAM, TDK InvenSense, DFRobot, Rika Sensors, y del fabricante del Ítem 9).
3. Presentar una declaración jurada complementaria donde se garantice que todos los sensores se entregarán en placas listas para interconexión y montaje, con sus respectivos cables y conectores.
""")

    content = "\n".join(lines)
    dest_path = r"d:\Proyectos\Arquitectura\informe\04_consultas_al_proveedor.md"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Supplier queries generated: {dest_path} ({len(content)} characters)")

if __name__ == "__main__":
    generate_supplier_queries()
