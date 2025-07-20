# Jarvis AI Assistant (OpenRouter Edition with translatepy)

import speech_recognition as sr
import pyttsx3
import requests
import pyautogui
import psutil
import subprocess
import os
import webbrowser
import json
import threading
import time
from datetime import datetime
from translatepy import Translator
import sys

class JarvisAI:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()
        self.translator = Translator()
        self.is_listening = True

        # OpenRouter API configuration
        self.api_key = "My_api_key"  # Replace with your real API key
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

        self.setup_tts()

        self.language_codes = {
            'english': 'english',
            'hindi': 'hindi',
            'chinese': 'chinese',
            'russian': 'russian',
            'japanese': 'japanese',
            'spanish': 'spanish'
        }

        self.current_language = 'english'

        print("🤖 Jarvis AI Assistant Initialized!")

    def setup_tts(self):
        voices = self.tts_engine.getProperty('voices')
        if voices:
            self.tts_engine.setProperty('voice', voices[0].id)
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 0.8)

    def speak(self, text, language='english'):
        try:
            if language != 'english':
                translated = self.translator.translate(text, destination_language=language)
                text = translated.result
            print(f"🗣️ Jarvis: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")

    def listen(self):
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = self.recognizer.recognize_google(audio).lower()
            print(f"👤 You said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected. Try again.")
            return None
        except Exception as e:
            print(f"🎙️ Listening error: {e}")
            return None

    def get_ai_response(self, prompt, language='english'):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            messages = [
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant capable of controlling computers and providing information. Be concise and helpful."},
                {"role": "user", "content": prompt}
            ]

            payload = {
                "model": "mistralai/mixtral-8x7b",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500
            }

            response = requests.post(self.api_url, headers=headers, json=payload)
            data = response.json()

            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
            else:
                return "I couldn't generate a response."
        except requests.exceptions.RequestException as e:
            return f"Network error: {e}"
        except json.JSONDecodeError:
            return "Invalid response from server."

    def execute_pc_command(self, command):
        command = command.lower()
        if "screenshot" in command:
            screenshot = pyautogui.screenshot()
            screenshot.save("jarvis_screenshot.png")
            return "Screenshot saved as jarvis_screenshot.png"
        elif "open" in command:
            if "notepad" in command:
                subprocess.Popen(['notepad.exe'])
                return "Opening Notepad"
            elif "calculator" in command:
                subprocess.Popen(['calc.exe'])
                return "Opening Calculator"
            elif "chrome" in command:
                webbrowser.open('https://www.google.com')
                return "Opening Chrome browser"
            elif "explorer" in command:
                subprocess.Popen(['explorer.exe'])
                return "Opening File Explorer"
        elif "close" in command:
            if "notepad" in command:
                os.system("taskkill /f /im notepad.exe")
                return "Closing Notepad"
        elif "volume up" in command:
            for _ in range(5): pyautogui.press('volumeup')
            return "Volume increased"
        elif "volume down" in command:
            for _ in range(5): pyautogui.press('volumedown')
            return "Volume decreased"
        elif "mute" in command:
            pyautogui.press('volumemute')
            return "Audio muted"
        elif "lock screen" in command:
            pyautogui.hotkey('win', 'l')
            return "Screen locked"
        return None

    def get_system_info(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return f"CPU: {cpu_percent}% | RAM: {memory.percent}% | Disk: {disk.percent}%"

    def change_language(self, language):
        lang = language.lower()
        if lang in self.language_codes:
            self.current_language = self.language_codes[lang]
            return f"Language changed to {language}"
        return "Language not supported"

    def process_command(self, command):
        if not command:
            return

        command = command.lower()

        if any(word in command for word in ["exit", "quit", "goodbye"]):
            self.speak("Goodbye! Jarvis signing off.", self.current_language)
            self.is_listening = False
            return

        if "switch to" in command:
            for lang in self.language_codes:
                if lang in command:
                    res = self.change_language(lang)
                    self.speak(res, self.current_language)
                    return

        pc_res = self.execute_pc_command(command)
        if pc_res:
            self.speak(pc_res, self.current_language)
            return

        if "time" in command:
            self.speak(datetime.now().strftime("%H:%M:%S"), self.current_language)
            return

        if "date" in command:
            self.speak(datetime.now().strftime("%Y-%m-%d"), self.current_language)
            return

        if "system info" in command:
            self.speak(self.get_system_info(), self.current_language)
            return

        self.speak(self.get_ai_response(command, self.current_language), self.current_language)

    def run(self):
        self.speak("Hello Mohammad Naqi, I'm Jarvis. How can I assist you today?", self.current_language)
        while self.is_listening:
            command = self.listen()
            if command:
                self.process_command(command)
            time.sleep(0.5)

if __name__ == "__main__":
    JarvisAI().run()
