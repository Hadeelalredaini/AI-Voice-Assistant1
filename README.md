# AI-Voice-Assistant1

A voice-based AI assistant that takes spoken input, processes it through a large language model, and responds back with generated speech.

## Overview

This project implements a simple **Voice-to-Voice AI Assistant** pipeline made up of three core stages:

1. **Speech-to-Text (STT)** — captures audio from the microphone and converts it into written text using Google's speech recognition service (`speech_recognition` library).
2. **LLM Processing** — sends the transcribed text to Cohere's language model (`command-a-03-2025` via `ClientV2`) to generate a relevant response.
3. **Text-to-Speech (TTS)** — converts the model's text response into an audio file using `gTTS` (Google Text-to-Speech) and plays it back to the user.

## Pipeline Architecture

```
🎙️ Microphone Input
        ↓
Speech-to-Text (Google Speech Recognition)
        ↓
Text Query
        ↓
LLM Processing (Cohere command-a-03-2025)
        ↓
Text Response
        ↓
Text-to-Speech (gTTS)
        ↓
🔊 Audio Output
```

## Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Configure your API key
Create a `.env` file in the project root:
COHERE_API_KEY=your_api_key_here

### 3. Run the assistant
python app.py


## Sample Output
<img width="960" height="492" alt="vsccode" src="https://github.com/user-attachments/assets/bb742a0b-f679-4ce2-99c9-b9a7f3192fc2" />

--- بدء تشغيل المساعد الذكي ---
🎙️ جاري الاستماع عبر الميكروفون...
✅ تم التعرف على النص صوتياً: ما هي عملة السعودية؟
🤖 جاري توليد الرد...

🤖 الرد:
عملة المملكة العربية السعودية هي الريال السعودي...
🔊 جاري تحويل الرد إلى صوت...
✅ تم تشغيل الرد الصوتي بنجاح.


## Known Limitation: Arabic Text Rendering

The assistant correctly understands and answers Arabic questions — for example, when asked *"What is the currency of Saudi Arabia?"*, the model correctly identifies it as the **Saudi Riyal**. However, the terminal used for testing does not fully support right-to-left (RTL) Arabic rendering, which can cause the displayed text to appear **garbled, reversed, or mixed up** even though the underlying answer is accurate.


## Microphone Fallback

Since not all environments have a working/available microphone, the assistant includes a built-in fallback: if the microphone cannot be accessed (no device found, permission denied, no sound detected, etc.), the program automatically switches to **text input mode**, allowing the user to type their question instead. This ensures the assistant keeps working end-to-end even without a functioning microphone.
