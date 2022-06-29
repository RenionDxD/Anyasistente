import os
from dotenv import load_dotenv
import pyttsx3

load_dotenv()


def info():
    for k, v in os.environ.items():
        print(k + ':', v)
    print('\n')
    [print(item) for item in os.environ['PATH'].split(';')]

    print("----------------------------")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for v in voices:
        print(v.id+" | "+v.name)


if __name__ == '__main__':
    info()