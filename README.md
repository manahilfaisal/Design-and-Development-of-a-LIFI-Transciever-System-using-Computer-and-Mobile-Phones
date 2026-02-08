# Li-Fi Transceiver System

This repository contains a prototype implementation of a **Li-Fi (Light-Fidelity)** transceiver system. The project demonstrates the transmission of text data using visible light, leveraging personal computers for transmission and smartphones for reception.

## Overview
Li-Fi is an emerging wireless communication technology that uses the visible light spectrum to transmit data. This project implements a full communication cycle: encoding text into binary, modulating light pulses via a screen, and decoding the signal using a smartphone's ambient light sensor.



---

## System Architecture
The system operates in three distinct stages:

### **Stage 1: Transmission (Data Encoding)**
* **ASCII Conversion:** Text is converted to ASCII codes using Python’s `ord()` function.
* **Binary Translation:** ASCII values are formatted into 8-bit binary strings using the `format()` function.
* **Light Modulation:** A GUI built with `Tkinter` flashes the screen to represent data:
    * **Binary 1:** White screen (Light On).
    * **Binary 0:** Gray screen (Light Off).
    * **Separator:** A "separator bit" (value 2) was introduced to distinguish between individual data bits and prevent signal merging.

### **Stage 2: Reception & Data Acquisition (ADC Simulation)**
* **The phyphox Interface:** The **phyphox** mobile app is used to access the smartphone's ambient light sensor. It records variations in light intensity (lux) as the screen flashes.
* **Data Export:** The recorded lux levels are exported from the app as a **CSV file**, which serves as the raw input for the decoding script.
* **Signal Processing:** Raw lux data is imported via `pandas` and visualized with `matplotlib` to identify patterns.
* **Peak Detection:** The system identifies local maxima (peaks for binary 1) and minima (valleys for binary 0) using `scipy.signal`.
* **Filtering:** Improper values caused by noise or ambient interference are filtered out using predefined thresholds to ensure data integrity.



### **Stage 3: Decoding (Data Reconstruction)**
* **Cleaning:** The filtered signal is used to reconstruct a clean binary sequence.
* **String Reconstruction:** The binary chunks are grouped into 8-bit bytes, converted back to integers using `int()`, and finally restored to human-readable text using the `chr()` function.

---

## Requirements
* **Hardware:**
    * PC or Laptop (with screen for transmission).
    * Smartphone with an ambient light sensor.
* **Software:**
    * **Python 3.x**.
    * **phyphox app** (Mobile).
    * **Libraries:** `pandas`, `numpy`, `matplotlib`, `scipy`, `tkinter`.

---

## Troubleshooting & Lessons Learned
Initially, data transmission faced issues where individual bits were indistinguishable, leading to "garbage values". The team resolved this by:
1.  Introducing a **black separator bit** (value 2) between data pulses to add structure to the transmission.
2.  Assigning specific **RGB values** to improve bit distinguishability.
3.  **Sensor Note:** On some devices, the light sensor only updates during coarse changes in illuminance, which must be accounted for during data capture.

---

## Authors
* **Department of Electrical Engineering**, Ghulam Ishaq Khan Institute of Engineering Sciences and Technology (GIKI).
* **Contributors:** Palwasha Binte Inam, Manahil Faisal, Sara bint Bilal, and Rafay Saeed.

## Acknowledgements
Special thanks to **Dr. Nisar Ahmed** and **Sir Asad Malik** for their continuous guidance and support.
