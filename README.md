# gTTs Voice Assistant

A bootstrapped voice assistant in Python utilizing various APIs for speech synthesis and recognition.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This project is a simple voice assistant built using Python. It leverages several APIs and libraries to enable speech recognition and text-to-speech functionalities. The main components include Google Text-to-Speech (gTTS), Speech Recognition, and more.

## Features

- **Greeting and User Identification:**
  - The assistant greets the user and asks for their name.

- **General Conversation:**
  - Responds to queries like "how are you" and provides the current time.

- **Location Information:**
  - Provides location information using Google Maps.

- **Weather Updates:**
  - Retrieves and speaks the current weather for a specified location using OpenWeatherMap.

- **YouTube Search:**
  - Searches for videos on YouTube based on user input.

- **Mathematical Queries:**
  - Searches for mathematical or equation-related questions on Google.

- **Internet Search:**
  - Performs a web search on Google based on user queries.

- **News Headlines:**
  - Retrieves and displays the latest news headlines.

- **Application Opening:**
  - Opens specified applications using voice commands.

## Requirements

The following Python packages are required for this project:

- PyAudio
- PySpeech
- SpeechRecognition
- Playsound
- Requests
- PyAppOpener
- gTTS

## Installation

1. Clone the Repository 
   ```bash
   git clone https://github.com/your-username/gtts-voice-assistant.git
   cd gtts-voice-assistant
   
2. Install the APIs and Libraries required.

    ```bash 
     pip install pyaudio
     pip install SpeechRecognition
     pip install requests
     pip install AppOpener
     pip install gTTS
     pip install playsound@git+https://github.com/taconi/playsound

## Usage

After installing the necessary dependencies, you can run the voice assistant script:

```bash
python gtts.py
