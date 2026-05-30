# Nexis Development Journal

## Introduction

Nexis started as an idea rather than a hardware design.

The original vision was inspired by the concept of a personal desk companion capable of interacting with a computer through natural language. Instead of controlling software through APIs, the device would interact with a computer exactly like a human using a keyboard and mouse.

The project eventually evolved into two major components:

### OAI

Online AI responsible for:

* Understanding commands
* Planning actions
* Validating actions
* Generating execution instructions

### Nexis

Physical desk companion responsible for:

* Voice interaction
* User interface
* Task approval
* HID execution

The development journey is documented below.

---

# Phase 1 — Project Ideation

## April 2026

The project began with research into Human Interface Devices.

Main topics studied:

* USB HID specifications
* Keyboard architecture
* Mouse architecture
* Scan codes
* Input automation

The initial question was:

> Can a device behave like a human user and control a computer entirely through USB HID?

This phase focused on understanding how keyboards and mice communicate with computers and whether AI-generated actions could be translated into HID events.

### Outcome

A high-level architecture for the entire system was created.

---

# Phase 2 — Defining OAI

## April 2026

After understanding HID systems, attention shifted toward the intelligence layer.

The concept of OAI was introduced.

OAI stands for:

**Online AI**

Its purpose is to convert natural language into structured computer actions.

Example:

User Command:

```text
Upload my video to YouTube
```

Expected Output:

```text
Open Browser
Navigate To YouTube
Click Upload
Select File
Publish
```

The challenge was no longer controlling a computer.

The challenge became:

> How do we convert human intent into machine actions?

This phase produced the first architecture for OAI.

---

# Phase 3 — Building OAI

## April–May 2026

The software portion of the project was developed before hardware acquisition.

Several layers were implemented:

### Normalizer

Responsible for:

* Cleaning commands
* Extracting intent
* Identifying keywords

### Planner

Responsible for:

* Breaking tasks into steps

### Validator

Responsible for:

* Safety checks
* Structural verification

### Executor

Responsible for:

* Converting plans into executable actions

This was the first fully functional version of OAI.

---

# Phase 4 — Debugging and Deployment

## May 2026

Once the core software was functional, deployment work began.

Major tasks:

* GitHub setup
* API migration
* Testing
* Bug fixing
* Cloud deployment

OAI was successfully deployed and became accessible through the internet.

## This milestone transformed OAI from a local experiment into a usable service.

# Phase 5 — Hardware Planning

## May 2026

With the software foundation completed, focus shifted toward hardware.

Key hardware selected:

* Raspberry Pi 4 Model B
* ESP32-S3
* INMP441 Microphone
* MAX98357A Amplifier
* Speaker
* Touchscreen Display

The Raspberry Pi was chosen as the primary controller while the ESP32-S3 was retained for USB HID functionality.

---

# Phase 6 — CAD Design

## May 2026

Fusion 360 was used to design the enclosure.

Design objectives:

* Compact footprint
* Touchscreen integration
* Front control panel
* Internal speaker mount
* PCB mounting system

Challenges:

* Limited laptop performance
* Large assemblies
* Mechanical constraints

## Despite these limitations, the enclosure design progressed steadily and eventually reached a near-complete state.

# Phase 7 — Learning KiCad

## Late May 2026

This was the first PCB ever designed for the project.

Learning resources included:

* Community tutorials
* Philip's Lab
* Official documentation
* Practical experimentation

Initial tasks:

* Understanding footprints
* Symbol selection
* Net connections
* PCB workflow

The learning curve was significant but resulted in a complete schematic.

---

# Phase 8 — PCB Development

## May 2026

The schematic gradually evolved into a complete PCB design.

Integrated systems:

* Raspberry Pi
* Audio subsystem
* ESP32 interface
* Buttons
* Rotary encoder
* Power subsystem
* Expansion headers

## The PCB was repeatedly revised as understanding of KiCad improved.

# Current Status

Completed:

* OAI Architecture
* OAI Implementation
* Cloud Deployment
* Hardware Selection
* CAD Design
* PCB Schematic
* Initial PCB Layout

In Progress:

* PCB Validation
* Firmware
* Physical Assembly
* Manufacturing Preparation

Remaining:

* PCB Fabrication
* Component Assembly
* System Testing
* Final Enclosure Iteration

---

# Lessons Learned

The most important lesson from this project was that building a hardware product is not only about electronics or software.

It requires:

* Research
* Documentation
* Iteration
* Debugging
* Patience

Several parts of the project were redesigned multiple times, and many tools had to be learned from scratch. However, each redesign improved the final system.

---

# Final Vision

Nexis is intended to become the first component of a larger productivity ecosystem.

The long-term goal is to create a physical AI companion capable of helping users interact with computers naturally while maintaining the reliability and compatibility of standard HID devices.
