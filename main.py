from config import g_API
import pathlib
import textwrap
import pyttsx3 as p3
import speech_recognition as sr
import datetime as ds
# from VoiceMaker.custom_voice import speak
import time
import webbrowser as web
import config
import google.generativeai as genai
import config
import pygame
import os
import random
formal_responses = [
    "I appreciate your request. Please allow me a moment to gather my thoughts, and I'll get back to you shortly.",
    "Thank you for reaching out. I need a brief moment to consider your request. I'll respond promptly.",
    "I'm glad you brought this up. Let me take a moment to review the details, and I'll provide a response as soon as possible.",
    "Your inquiry is important. Allow me a moment to assess the situation, and I'll address it promptly.",
    "I understand your need, and I'm happy to assist. Please give me a moment to gather the necessary information, and I'll respond promptly."
]

# Used to securely store your API key
# from google.colab import userdata

def to_markdown(text):
    text = text.replace('•', '  *')
    indented_text = textwrap.indent(text, ' ',predicate=lambda _: True)
    return indented_text
def text_response(prompt):
  res=model.generate_content(prompt)
  return to_markdown(res.text)
def wishMe():
    hour=int(ds.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good After Noon!")
    else:
        speak("Good Evening!")
    #speak("I am your friend! How can I Help You")
    speak('How Can i help you?')
#takes the command using speech_recognition👌
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language= 'en-in')
        print(f"tarun said: {query}\n")
    except Exception as e:
        speak("sorry tarun i can't get that.")
        print("sorry tarun i can't get that.")
        query=takeCommand().lower()
        return None
    return query
def speak(data):
    voice1 = "kn-IN-SapnaNeural"

    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 100
    chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]

    # Convert and play each chunk
    for chunk in chunks:
        text = ' '.join(chunk)
        command1 = f'edge-tts --voice "{voice1}" --text "{text}" --write-media "data.mp3"'
        os.system(command1)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    return True
if __name__=="__main__":
    genai.configure(api_key=config.g_API)
    model = genai.GenerativeModel('gemini-pro')
    # print(text_response('What is GPT?'))
    print('testing..')
    wishMe()
    while True:
        query = takeCommand().lower()
        # query = input('Question: ')
        if 'hi sapna' in query:
            speak('hii tarun')
        elif 'stop ' in query:
            speak('miss you')
            exit()
        else:
            data=text_response(query)
            print(query)
            with open('response.txt','w') as file:
                file.writelines(data)
            print(data)
            speak('complete information is provided in response file')
            speak(random.choice(formal_responses))
            speak(f'sumnmary of {data} with 400 maximum charecters')