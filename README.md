# Recreating Nexis

This section documents the process required to recreate the project from scratch.

## Requirements

### Hardware

* Raspberry Pi 4 Model B
* Official Raspberry Pi Display
* ESP32-S3
* INMP441 Microphone
* MAX98357A Amplifier
* Speaker
* Rotary Encoder
* Push Buttons
* LiPo Battery (Optional)

See BOM.md for the complete list.

---

## Software

### Raspberry Pi

Install:

* Raspberry Pi OS
* Python
* Git
* Required libraries

### ESP32

Install:

* Arduino IDE or PlatformIO
* ESP32 Board Package

---

# Step 1 — Clone Repositories

Clone:

```bash
git clone <oai-repository>
```

Clone:

```bash
git clone <nexis-repository>
```

---

# Step 2 — Prepare Raspberry Pi

Flash Raspberry Pi OS.

Connect:

* Display
* Keyboard
* Mouse

Perform:

```bash
sudo apt update
sudo apt upgrade
```

Install project dependencies.

---

# Step 3 — Configure OAI

Create environment file.

Add:

```text
API_KEY=
MQTT_SERVER=
```

Run test commands.

Verify OAI returns valid plans.

---

# Step 4 — Flash ESP32

Open:

```text
firmware/
```

Compile firmware.

Upload to ESP32-S3.

Verify:

* WiFi connection
* HID connection

---

# Step 5 — Manufacture PCB

Open:

```text
pcb/
```

Generate:

* Gerbers
* Drill Files
* BOM

Submit to PCB manufacturer.

---

# Step 6 — Assemble Hardware

Install:

* Raspberry Pi
* Display
* PCB
* Speaker
* Buttons
* Encoder

Complete wiring.

Verify power rails.

---

# Step 7 — System Test

Test:

### Audio

* Microphone
* Speaker

### Input

* Touchscreen
* Buttons
* Encoder

### Communication

* Pi ↔ ESP32

### HID

* Keyboard
* Mouse

---

# Step 8 — Final Validation

Test example commands:

```text
Open YouTube

Open Calculator

Search Google

Upload File
```

Verify:

* OAI response
* Approval screen
* HID execution

---

# Manufacturing Notes

The PCB included in this repository is an early revision.

Future revisions may change:

* Component placement
* Routing
* Connector locations

Always verify the latest schematic before ordering boards.

---

# Current Project State

Completed:

* OAI
* CAD Design
* PCB Design
* Documentation

In Progress:

* Firmware
* PCB Validation
* Physical Assembly

Planned:

* Manufacturing
* Testing
* Final Enclosure Revision

The repository represents the current development state and will continue evolving as physical prototypes are produced and tested.
