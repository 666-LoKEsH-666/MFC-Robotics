import pyaudio
import json
from vosk import Model, KaldiRecognizer
from pydobot import Dobot
import serial.tools.list_ports
import time
from letter_strokes import letter_draw_functions

class SpeechToWriter:
    def __init__(self, model_path, port='COM15'):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=16000,
                                      input=True,
                                      frames_per_buffer=8000)
        self.stream.start_stream()
        self.dobot = Dobot(port=port, verbose=True)

    def listen_and_draw(self):
        print("🎤 Speak now...")
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "").upper().strip()
                if text:
                    print(f"🗣️ '{text}' recognized")
                    self.draw_text(text)

    def draw_text(self, text):
        offset_x = 0
        for char in text:
            if char == " ":
                offset_x += 10
                continue

            if char not in letter_draw_functions:
                print(f"⚠️ Unsupported character: '{char}'")
                continue 

            draw_func = letter_draw_functions[char]
            draw_func(self.dobot, offset_x)
            offset_x += 8

if __name__ == "__main__":
    ports = [port.device for port in serial.tools.list_ports.comports()]
    print("Available COM ports:", ports)
    port = 'COM15'  # Use COM15 as you specified
    model_path = r"C:\Users\LENOVO\Desktop\python\SpeechToHandwritingBot\assets\model"

    writer = SpeechToWriter(model_path=model_path, port=port)
    writer.listen_and_draw()
