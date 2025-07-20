**Jarvis AI Voice Assistant (LLM + Voice + OpenRouter)** :

---

````markdown
# 🧠 Jarvis AI Voice Assistant

Jarvis is a smart voice-activated personal assistant built using Python. It can answer questions using a local or cloud-based LLM (via OpenRouter), control system functions, respond in spoken language using TTS, and stop listening instantly via voice commands.

---

## 🚀 Features

- 🎤 Voice input via microphone (Speech Recognition)
- 🗣️ Voice output with gTTS
- 🤖 Answers your questions using **DeepSeek R1 LLM** from OpenRouter
- 💻 Controls PC actions: open apps, take screenshots, volume, lock screen, etc.
- 🕒 Tells time, date, and system info
- 🌍 Multilingual support with translation
- 🛑 Voice-controlled STOP (say "stop", "exit", or "goodbye" anytime)
- 🧠 Ignores casual phrases like “hi”, “hello”, etc.
- 🧵 Works fully offline except for the LLM API

---

## 🛠️ Tech Stack

- Python 3.13
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [Playsound](https://pypi.org/project/playsound/)
- [OpenRouter API](https://openrouter.ai/)
- [DeepSeek R1 model](https://openrouter.ai/models/deepseek/deepseek-r1)

---

## 🔧 Setup Instructions

### 1. Clone the repo


````

### 2. Install dependencies

Make sure you have Python 3.13 installed.

```bash
pip install -r requirements.txt
```

If `pyaudio` fails, install with:

```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Add your OpenRouter API Key

In `ai_agent.py`, replace this line:

```python
self.api_key = "your_openrouter_api_key"
```

with your actual API key from [OpenRouter](https://openrouter.ai/).

---

## ▶️ Run the Assistant

```bash
python ai_agent.py
```

Jarvis will greet you and start listening for your voice commands.

---

## 🗣️ Example Commands

* “Take a screenshot”
* “Open Notepad”
* “What is the time?”
* “Stop” — will stop Jarvis immediately
* “Switch to Hindi” — will change response language

---

## 📂 Project Structure

```
jarvis-voice-assistant/
├── ai_agent.py         # Main assistant script
├── README.md           # This file
└── requirements.txt    # Python dependencies
```


---


## 🙏 Acknowledgements

* [OpenRouter](https://openrouter.ai/)
* [DeepSeek LLM](https://deepseek.com/)
* [Google TTS](https://cloud.google.com/text-to-speech)
* [PyAudio & SpeechRecognition](https://pypi.org/)

---

✅ requirements.txt
txt
Copy
Edit
speechrecognition
gtts
playsound
requests
pyautogui
psutil
translatepy
pyaudio
✅ Tip: If 

---

> Created with ❤️ by [Mohammad Naqi](https://github.com/naqi51)



