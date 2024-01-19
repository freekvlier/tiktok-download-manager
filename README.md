# TikTok Video Downloader

## Overview
This Python script serves as a TikTok video downloader, specifically designed for creating video compilations. The tool features a graphical user interface (GUI) for a user-friendly experience and ensures that the same video is not downloaded twice.

## Features
- Download TikTok videos by entering the video URL.
- GUI for a user-friendly experience.
- Check if a video has already been downloaded using a Firebase database.

## Prerequisites
- Python 3.x
- Dependencies (specified in requirements.txt)
- Firebase credentials JSON file for database functionality

## Installation
### 1. Clone the repository:
```bash
git clone https://github.com/freekvlier/tiktok-downloader.git
cd tiktok-downloader
```

### 2. Activate the Virtual Environment

Activate the virtual environment to work with isolated package dependencies.

- **Windows:**
```bash
.\env\Scripts\activate
```

- **Mac/Linux:**
```bash
source env/bin/activate
```

### 3. Install Required Packages

Install the required packages within the virtual environment.

```bash
pip install -r requirements.txt
```

### 4. Set up Firebase:
1. Create a Firebase project.
2. Download the Firebase credentials JSON file.
3. Save the JSON file in the project root or in a location of your choice.

### 5. Create .env file
Create a .env file in the project root and add the following line, replacing 'your_credentials.json' with the actual name of your credentials file:

```bash
FIREBASE_CREDENTIALS_PATH=your_credentials.json
```

## Usage
Run the GUI using:

```bash
python3 main.py
```
