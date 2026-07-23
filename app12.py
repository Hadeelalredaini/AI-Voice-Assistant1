import os
import sys
import cohere
from dotenv import load_dotenv
import speech_recognition as sr
from gtts import gTTS
import playsound
import tempfile

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    print(" لم يتم العثور على مفتاح API في ملف .env")
    sys.exit()

co = cohere.ClientV2(api_key)

MODEL_NAME = "command-a-03-2025"


def get_question():
    r = sr.Recognizer()
    try:
        print("🎙️ جاري الاستماع عبر الميكروفون...")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=3, phrase_time_limit=6)

        question = r.recognize_google(audio, language="ar-SA")
        print(f" تم التعرف على النص صوتياً: {question}")
        return question

    except Exception as e:
        print(f"\n تنبيه: تعذر استخدام المايك ({type(e).__name__}: {e}). تم التحويل لوضع الكتابة النصية.")
        question = input(" اكتب سؤالك هنا: ")
        return question


def get_ai_response(question):
    response = co.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": question}],
    )
    return response.message.content[0].text


def speak_response(text):
    try:
        print(" جاري تحويل الرد إلى صوت...")
        tts = gTTS(text=text, lang="ar")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_path = tmp_file.name

        tts.save(tmp_path)
        playsound.playsound(tmp_path)
        os.remove(tmp_path)
        print(" تم تشغيل الرد الصوتي بنجاح.")

    except Exception as e:
        print(f" ({e}). تم عرض الرد نصياً فقط.")


if __name__ == "__main__":
    print("--- بدء تشغيل المساعد الذكي ---")

    question = get_question()

    if question.strip() == "":
        print(" لم يتم إدخال  سؤال.")
        sys.exit()

    try:
        print("🤖 جاري توليد الرد...")
        answer_text = get_ai_response(question)

        print("\n🤖 الرد:")
        print(answer_text)

        speak_response(answer_text)

    except Exception as e:
        print("حدث خطأ:", e)