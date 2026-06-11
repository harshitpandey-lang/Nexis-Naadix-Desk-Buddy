
# Nexis
<img width="1366" height="410" alt="model_nexis_2026-Jun-03_01-21-36AM-000_CustomizedView11682904690_png" src="https://github.com/user-attachments/assets/e82a30d5-a7dc-404a-8ee1-78e78ddcec3c" />

Nexis is a dual AI powered desk automation bot which uses raspberry pi to run a local llm and also uses a cloud deployed ai agent to do the tasks given to it in small chunks. We can give instructions through the interactive touch screen and also through the micophone. 
It uses esp32 to give commands to the device connected through the USB. 

## Overview

Nexis is a desk buddy which can do all sort of works upon good training and customisation. It uses a raspberry pi and open source AI model to break works into smaller steps. It uses the the local llm to generte the HID code respective to every step given uses python to asses if the work is performed then goes ahed with next step till all are completed. 
It uses esp32 to give HID code to the PC connected to make it do or perform a particular task. It can communicate or given instructionthrough the Touchscreen and Microphone.

---

## System Architecture
User

 │
 
 ├── Voice Input
 
 ├── Touchscreen Input
 
 │
 
 ▼
 
Raspberry Pi 4

 │
 
 ├── Local LLM
 
 ├── Task Planner
 
 ├── Verification Engine
 
 └── Cloud AI Agent
 
 │
 
 ▼
 
ESP32-S3 HID Controller

 │
 
 ▼
 
Connected Computer

 │
 
 ├── Keyboard Events
 
 ├── Mouse Events
 
 └── Workflow Execution
 

 
## Specifications

| Parameters | Value |
| Code | Python|
| Hardware | Raspberry pi model B |
| Design | 3d printed and rubber keys|

### Hardware

| Component | Purpose |
|-----------|---------|
| Raspberry Pi 4 Model B | Main computing unit |
| Official Raspberry Pi Display | User interface |
| ESP32-S3 | HID controller |
| INMP441 Microphone | Voice input |
| MAX98357A Amplifier | Audio output |
| Speaker | Voice feedback |
| Rotary Encoder | Navigation control |
| Push Buttons | User interaction |
| LiPo Battery | Portable power |

<img width="211" height="176" alt="{549CDC2C-EC70-4538-B992-6CFFC3E95AC3}" src="https://github.com/user-attachments/assets/bd43ffa1-3f87-47c6-be5f-c1ea334ff9be" />
<img width="1068" height="572" alt="nexus deskbuddy" src="https://github.com/user-attachments/assets/49230096-0863-433c-9016-1df34559e010" />


See BOM.md for the complete bill of materials.

---

## Software

- Backend Language
  - Python
- Framework
  - FastAPI
- AI
  - OpenAI API
  - Claude API
  - Gemini API
- Data Models
  - Pydantic
- Hosting
  - Render

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

### How It Works
- User gives an instruction.
- Nexis interprets the request.
- AI breaks the task into smaller steps.
- Local verification checks progress.
- ESP32 receives generated HID commands.
- Commands are executed on the connected computer.
- Nexis confirms completion and proceeds to the next step.

This process continues until the entire workflow is completed.

---

## Gallery

<p align="center">
  <img src="https://github.com/user-attachments/assets/b77763a1-a549-44a0-bfa6-dd492a8bac73" width="32%">
  <img src="https://github.com/user-attachments/assets/5c248b59-53d9-4192-b686-e38ccb909070" width="32%">
  <img src="https://github.com/user-attachments/assets/6164724f-40d4-4d7c-93f2-3191f8126337" width="32%">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/7bfca1ae-367c-4b8e-880c-0d4b1b8a9a82" width="32%">
  <img src="https://github.com/user-attachments/assets/36904d80-f7c2-493c-b4ef-9acd55fdf369" width="32%">
  <img src="https://github.com/user-attachments/assets/0bbf32c7-7a68-4bed-ad2c-3b902730f3d9" width="32%">
</p>

## Future Improvements

- It can work as full work automation
- It can also control the other tech stacks of your rooms
- If developed correctly it can do the job of any person

## Acknowledgement

- The raspberrry pi model 4 was alloted by my college (Jaypee Institute of Information Technology), which I am grateful.
- I am grateful for the oppurtunity presented by the Hack Club called fallout, Which I am a part of and am proud of making this project under their guidance for more reference realted to the fallout event (https://fallout.hackclub.com/path).
- I am also grateful for the help given by my seniors.


---
# Zine page
<img width="874" height="1240" alt="WhatsApp Image 2026-06-04 at 8 46 59 AM" src="https://github.com/user-attachments/assets/b5e7b2c2-8e9a-4f77-adbe-37a7350d4056" />

---
