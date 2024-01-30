import pygame
import os
import openai
import config
def speak(audio):
    #bn-IN-TanishaaNeural
    #'hr-HR-SreckoNeural'
    #zh-CN-XiaoyiNeural
    #zh-CN-YunjianNeural
    #zh-CN-YunxiaNeural
    ##en-HK-YanNeural
    #en-IN-PrabhatNeural😂
    #gu-IN-DhwaniNeural
    # kn-IN-SapnaNeural
    voice='kn-IN-SapnaNeural'
    # voice=vi
    openai.api_key = config.API
    chunks=audio.split()
    chunk_size=100
    chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]
    for chunk in chunks:
        text = ' '.join(chunk)
        command1 = f'edge-tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
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