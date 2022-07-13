import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import tempfile

fs = 16000  # sample rate
duration = 5  # seconds
sd.default.samplerate = fs
sd.default.channels = 2

tempdir = tempfile.gettempdir()


def listen():  # Returns speech_recognition.AudioData type
    recording = sd.rec(int(duration * fs))
    sd.wait()
    sf.write(tempdir+'/speech_recording.wav', recording, fs)
    r = sr.Recognizer()
    audiofile = sr.AudioFile(tempdir+'/speech_recording.wav')
    with audiofile as source:
        return r.record(source)



