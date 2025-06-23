# Death Countdown Timer ⏳

A minimalistic and motivational desktop app that shows how much time you have left to live — based on your birthdate and expected lifespan.

This app runs as a floating transparent widget on your desktop and updates every second. You can customize your birthdate and life expectancy through the settings menu.

![App Screenshot](screenshots/screenshot.png)

## 🔍 Features

- Live countdown (years, days, hours, minutes, seconds)
- Customizable birthdate & death age via Settings
- Draggable window
- Auto-start at login (Ubuntu)
- Clean dark theme with hover effects
- Transparency on idle, full controls on hover
- Lightweight and easy to install

## 🧠 Built With

- Python 3
- Tkinter GUI
- Debian packaging (`.deb`) for Ubuntu

## 🚀 Requirements

Before running or installing the app, make sure you have:

- Python 3 (`sudo apt install python3`)
- Tkinter (`sudo apt install python3-tk`)
- Pillow (for icon support):  
  ```bash
  pip3 install pillow

## 📦 Installation (Ubuntu .deb)
Option 1: Install from Release
Go to Releases
Download the .deb file
Install it : sudo dpkg -i death-countdown.deb

Option 2: Build Your Own .deb
Make sure you have packaging tools : sudo apt install python3 python3-tk devscripts debhelper build-essential

Create folder structure and DEBIAN/control file
Run : dpkg-deb --build death-countdown
Install: sudo dpkg -i death-countdown.deb