# Hardware Documentation

## Overview

Nexis is a desktop companion designed around a Raspberry Pi and an ESP32-S3. The Raspberry Pi acts as the primary controller while the ESP32-S3 provides USB HID functionality for interacting with a computer.

The hardware was designed to provide:

* Voice input
* Audio output
* Touchscreen interaction
* Physical controls
* USB HID automation
* Portable power support

---

# System Architecture

```text
                 User
                   │
                   ▼
         Official Pi Display
                   │
                   ▼
             Raspberry Pi
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
    Microphone  Speaker    ESP32-S3
        │                     │
        ▼                     ▼
    Voice Input         USB HID Output
                              │
                              ▼
                           Computer
```

---

# Main Controller

## Raspberry Pi

Role:

* System controller
* User interface
* Voice processing
* OAI communication
* Feedback monitoring

Connected Components:

* Display
* Microphone
* Amplifier
* ESP32 Interface
* Buttons
* Rotary Encoder

---

# HID Controller

## ESP32-S3

Role:

* Keyboard emulation
* Mouse emulation
* Command execution
* Secondary communication controller

Benefits:

* Native USB support
* WiFi support
* Low power consumption
* Reliable HID operation

---

# Display

## Official Raspberry Pi Touchscreen

Purpose:

* Device status
* User interaction
* Task approval
* Settings menu

Displayed Information:

* Network status
* Voice status
* Current task
* Approval prompts
* Error messages

---

# Audio Input

## INMP441 I2S Microphone

Purpose:

* Voice command capture

Interface:

* I2S

Connections:

```text
3V3
GND
WS
SCK
SD
```

Connected To:

* Raspberry Pi

---

# Audio Output

## MAX98357A Amplifier

Purpose:

* Audio playback
* Voice feedback

Interface:

* I2S

Connected To:

* Raspberry Pi

Output:

* 3W Speaker

---

# Rotary Encoder

Purpose:

* Navigation
* Volume control
* Menu selection

Signals:

```text
CLK
DT
SW
```

Connected To:

* Raspberry Pi GPIO

---

# Front Panel Buttons

Purpose:

* Manual control
* Emergency stop
* Menu navigation

Functions:

* Confirm
* Cancel
* Back
* Wake Device

---

# Power System

## USB-C Input

Primary power source.

Provides:

* Raspberry Pi power
* Peripheral power
* Charging input

---

## Battery Support

Optional portable operation.

Supports:

* Single-cell LiPo battery

Functions:

* Backup power
* Portable usage

---

# Speaker

Purpose:

* Audio feedback
* Notifications
* Voice responses

Connected Through:

```text
MAX98357A
        ↓
      Speaker
```

---

# Internal Communication

## Raspberry Pi ↔ ESP32-S3

Purpose:

* Command transfer
* Status reporting

Possible Interfaces:

* UART
* MQTT over WiFi
* USB Serial

Current Design:

* MQTT communication

---

# Hardware Features

### Input

* Touchscreen
* Microphone
* Buttons
* Rotary Encoder

### Output

* Speaker
* Display
* HID Keyboard
* HID Mouse

### Connectivity

* WiFi
* USB

### Power

* USB-C
* Battery Backup

---

# Design Goals

1. Simple architecture

2. Reliable HID operation

3. Easy assembly

4. Expandable design

5. Portable operation

6. Educational value

7. Hack Club Fallout compatibility

---

# Revision

Current Revision: V1

Status:

* Schematic Complete
* PCB In Development
* Firmware In Development
* Assembly Pending
