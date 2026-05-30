# Nexis-Naadix-Desk-Buddy
Nexis is and AI-powered desktop companion desiged to simplify interaction with a computer through natural langage commands.

The project combines a Raspberry Pi, ESP 32-S3, Touhscreen display, microphone, Spekaer, and cloud-based AI services to create a physical desk assistant capable of understanding instructions and controlling a computer through standard USB Human Interface device (HID) protocols.
---
## Project Goal
The goal of nexis is to creat a hardware device that allows users to perform computer tasks through simple spoken commands.

Instead of manully interacting with a keyboard and mouse, users communicate with nexis whixh converts commands into structured actions and executes them on a connected computer.

Examples :

Upload a video
Open applications
Launch websites
Manage files
Perform repetitive workflows
System Overview
User
 ↓
Touchscreen Interface
 ↓
Voice Command
 ↓
Raspberry Pi
 ↓
OAI Cloud Agent
 ↓
Task Plan
 ↓
User Approval
 ↓
ESP32-S3 HID Controller
 ↓
Computer
Main Components
Raspberry Pi

Acts as the primary controller.

Responsibilities:

Touchscreen interface
Voice processing
Communication with OAI
Task monitoring
Feedback validation
ESP32-S3

Acts as the HID controller.

Responsibilities:

USB keyboard emulation
USB mouse emulation
Command execution
Display

Official Raspberry Pi touchscreen used for:

Status display
Task approval
Device settings
Audio System

INMP441 microphone

Voice input

MAX98357A amplifier + speaker

Audio feedback
Features
Voice Commands

Users can issue commands naturally.

AI Task Planning

Tasks are interpreted by the OAI cloud agent.

Touchscreen Approval

Actions are displayed before execution.

HID Automation

Commands are executed through keyboard and mouse emulation.

Feedback Verification

Task progress is monitored and validated.

Hardware
Raspberry Pi
Official Raspberry Pi Display
ESP32-S3
INMP441 Microphone
MAX98357A Amplifier
Speaker
USB-C Power
LiPo Battery Support
Rotary Encoder
Repository Structure
pcb/
        KiCad design files

enclosure/
        CAD models and enclosure files

firmware/
        ESP32-S3 firmware

README.md
        Project overview

BOM.csv
        Bill of materials

HARDWARE.md
        Hardware documentation

FIRMWARE.md
        Firmware documentation

JOURNAL.md
        Development log

IMAGES.md
        Image references and renders

Steps_to_self_create.md
        Manufacturing and assembly notes
Current Status

Current development stage:

Hardware architecture completed
Schematic design completed
PCB design in progress
Firmware development in progress
Future Improvements
Local AI support
Offline operation
Enhanced feedback system
Improved touchscreen interface
Expanded automation capabilities
Hack Club Fallout

Nexis is being developed as a Hack Club Fallout project with a focus on hardware design, embedded systems, and practical AI-assisted computer interaction.

All PCB files, firmware, documentation, CAD files, and build logs are maintained within this repository.

Version 1.0

Author: Harshit Pandey
