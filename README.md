# Li-Fi Transceiver System

This repository contains a software-based prototype implementation of a **Li-Fi (Light-Fidelity)** transceiver system. The project demonstrates the transmission of text data using visible light without any external hardware, leveraging a computer display for transmission and a smartphone’s built-in ambient light sensor for reception.



## Overview
Li-Fi is an emerging wireless communication technology that utilizes the visible light spectrum for data transmission. This project implements a complete Li-Fi communication cycle entirely using off-the-shelf consumer devices and software tools, including data encoding, optical modulation, sensor-based reception, signal processing, and decoding.

**Note:** No dedicated transmitters, receivers, or custom hardware components are used.

---

## System Architecture
The system operates in three distinct stages:

### **Stage 1: Transmission (Data Encoding)**
* **ASCII Conversion:** Text is converted into ASCII codes using Python’s `ord()` function.
* **Binary Translation:** ASCII values are formatted into 8-bit binary strings using the `format()` function.
* **Light Modulation:** A GUI built with `Tkinter` modulates data by flashing the computer screen:
    * **Binary 1:** White screen (Light ON)
    * **Binary 0:** Gray screen (Light OFF)
    * **Separator Bit:** A dedicated separator (value = 2, represented by black) is inserted between bits to prevent pulse merging and improve decoding reliability.

### **Stage 2: Reception & Data Acquisition (ADC Simulation)**
* **Sensor Interface:** The **phyphox** mobile application is used to access the smartphone’s built-in ambient light sensor.
* **Data Capture:** Variations in light intensity (lux values) are recorded as the screen transmits data.
* **Data Export:** Recorded lux values are exported as a **CSV file**, which serves as the raw input for the decoding process.
* **Signal Processing:** * Lux data is imported using `pandas`.
    * Lux vs. Time is visualized using `matplotlib`.
    * Local maxima and minima are identified using `scipy.signal` (Peaks → **Binary 1**, Valleys → **Binary 0**).
    * Noise and ambient interference are reduced using predefined threshold values.
* *This stage emulates the behavior of an Analog-to-Digital Converter (ADC) using software-based signal processing.*



### **Stage 3: Decoding (Data Reconstruction)**
* The filtered signal is converted into a clean binary sequence.
* Binary data is grouped into 8-bit bytes.
* Each byte is converted back into an integer using `int()`.
* Human-readable text is reconstructed using the `chr()` function.

---

## Results & Experimental Validation
The Li-Fi transceiver system was experimentally validated using real sensor data obtained from a smartphone ambient light sensor. Under controlled lighting conditions, the system successfully transmitted and reconstructed ASCII-encoded text.

Detailed experimental results—including lux-versus-time plots, data cleaning stages, decoding steps, and system observations—are documented in the full project report:

📄 **[View Full Project Report (PDF)](./document%20(1).pdf)**
*Design and Development of Li-Fi Transceiver System Using Computer and Mobile Phones*

---

## Requirements

### **Hardware**
* Computer or laptop with a display
* Smartphone with a built-in ambient light sensor

### **Software**
* **Python 3.x**
* **phyphox** mobile application
* **Python Libraries:** `pandas`, `numpy`, `matplotlib`, `scipy`, `tkinter`

---

## Troubleshooting & Lessons Learned
Initial experiments resulted in indistinguishable bit transitions, leading to unreliable decoded output. These issues were resolved by:
1. **Introducing a separator bit** to impose structure on the transmitted signal.
2. **Using distinct screen intensity levels** to improve bit separation.
3. **Accounting for smartphone sensor limitations**, as some sensors update only during coarse changes in illuminance.

---


