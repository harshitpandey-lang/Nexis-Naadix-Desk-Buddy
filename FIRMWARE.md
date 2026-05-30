# Firmware Documentation

## Overview

The Nexis firmware runs on the ESP32-S3 and is responsible for converting approved actions into USB Human Interface Device (HID) events.

Unlike the Raspberry Pi, the ESP32-S3 does not perform AI processing or task planning. Its primary role is to act as a reliable keyboard and mouse controller for the connected computer.

---

# Firmware Objectives

The firmware is designed to:

* Receive commands from Raspberry Pi
* Execute keyboard actions
* Execute mouse actions
* Report execution status
* Maintain a stable connection
* Operate with low latency

---

# Firmware Architecture

```text
Raspberry Pi
      │
      ▼
Communication Layer
      │
      ▼
ESP32 Firmware
      │
 ┌────┴────┐
 ▼         ▼
Keyboard  Mouse
 HID       HID
      │
      ▼
 Connected PC
```

---

# Core Responsibilities

## USB HID

The ESP32-S3 acts as:

### Keyboard

Supported actions:

* Key presses
* Key combinations
* Text entry
* Hotkeys

Examples:

```text
CTRL + C
CTRL + V
ALT + TAB
WIN + R
```

---

### Mouse

Supported actions:

* Cursor movement
* Left click
* Right click
* Double click
* Scroll wheel

Examples:

```text
Move Cursor
Left Click
Scroll Down
Right Click
```

---

# Command Flow

```text
User Command
      │
      ▼
OAI
      │
      ▼
Raspberry Pi
      │
      ▼
ESP32-S3
      │
      ▼
USB HID Event
      │
      ▼
Computer
```

---

# Communication

The ESP32 receives commands from the Raspberry Pi.

Each command contains:

```json
{
  "action": "type",
  "value": "Hello World"
}
```

Example:

```json
{
  "action": "hotkey",
  "keys": ["CTRL","S"]
}
```

---

# WiFi

Purpose:

* Device connectivity
* Communication with Raspberry Pi
* Status reporting

Features:

* Auto reconnect
* Connection monitoring
* Error recovery

---

# Device States

## Boot

```text
Starting Firmware
```

---

## Connected

```text
Connected To Nexis
```

---

## Waiting

```text
Awaiting Commands
```

---

## Executing

```text
Executing Action
```

---

## Error

```text
Execution Failed
```

---

# HID Action Types

## Type Text

Example:

```text
Hello World
```

Firmware Behavior:

```text
Type characters one by one
```

---

## Press Key

Example:

```text
ENTER
ESC
TAB
```

---

## Hotkey

Example:

```text
CTRL + S
CTRL + SHIFT + T
ALT + TAB
```

---

## Mouse Click

Example:

```text
Left Click
Right Click
Double Click
```

---

## Mouse Move

Example:

```text
Move to X,Y
```

---

## Scroll

Example:

```text
Scroll Up
Scroll Down
```

---

# Safety Features

The firmware does not independently decide actions.

Every action must originate from:

```text
User
 ↓
OAI
 ↓
Approval Screen
 ↓
Firmware
```

This prevents unintended execution.

---

# Error Handling

The firmware detects:

* Lost WiFi connection
* Invalid commands
* HID failures
* Communication timeouts

Recovery Actions:

```text
Reconnect
Retry
Report Status
```

---

# Future Improvements

Planned additions:

* OTA updates
* USB status detection
* Device pairing
* Advanced diagnostics
* Local command buffering

---

# Design Philosophy

The ESP32 should remain simple.

Responsibilities should stay limited to:

* Communication
* HID execution
* Status reporting

All complex processing should remain on the Raspberry Pi and OAI systems.

---

Firmware Version: 1.0

Target Hardware:

* ESP32-S3

Status:

* In Development
* MVP Firmware Architecture Defined
