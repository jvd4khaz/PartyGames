# Mafia Game Role Distributor (Takavar Scenario)

This is a Python application built with Kivy that distributes Mafia game roles for the "Takavar" (Commando) scenario for 10 players. It is designed to be passed between players on a single phone.

## Features
- Supports 10 players: 3 Mafia, 7 Citizens.
- Roles: Godfather, Dr. Lecter, Simple Mafia, Doctor, Detective, Takavar (Sniper), Die-hard, Psychologist, 2 Simple Citizens.
- Hidden role reveal system.
- Persian text support (requires font).

## Prerequisites

### 1. Font File
You **MUST** provide a Persian/Arabic supporting font file named `vazir.ttf` (or rename your font to this) in this folder.
- You can download Vazir font from: https://github.com/rastikerdar/vazir-font
- Without this file, the Persian text will likely show as squares.

### 2. Local Testing (Windows)
1. Install Python.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python main.py
   ```

## How to Build APK (Android)

Since you are on Windows, the easiest way to build the APK is using **Google Colab**.

1. **Zip your project**: Compress the `MafiaApp` folder (containing `main.py`, `game_logic.py`, `buildozer.spec`, and `vazir.ttf`) into a zip file.
2. **Open Google Colab**: Go to [colab.research.google.com](https://colab.research.google.com).
3. **Upload your Zip**: Upload your zip file to the Colab environment.
4. **Run the following commands in Colab cells**:

   ```python
   # Install buildozer
   !pip install buildozer cython==0.29.21
   !sudo apt-get install -y \
       python3-pip \
       build-essential \
       git \
       python3 \
       python3-dev \
       ffmpeg \
       libsdl2-dev \
       libsdl2-image-dev \
       libsdl2-mixer-dev \
       libsdl2-ttf-dev \
       libportmidi-dev \
       libswscale-dev \
       libavformat-dev \
       libavcodec-dev \
       zlib1g-dev

   # Unzip your project
   !unzip MafiaApp.zip -d MafiaApp
   
   # Navigate to folder
   %cd MafiaApp
   
   # Initialize buildozer (if you didn't include buildozer.spec)
   # !buildozer init
   
   # Build the APK
   !buildozer android debug
   ```

5. **Download APK**: Once finished, the APK will be in `bin/` folder inside `MafiaApp`. Download it and transfer to your phone.

## Role Configuration
You can modify the roles in `game_logic.py`.

