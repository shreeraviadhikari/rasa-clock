import datetime
import pyaudio
import wave


class RasaSpeaker:
    def __init__(self) -> None:
        self.chunk = 1024
        self.p = pyaudio.PyAudio()

        self.times = self._load_files()

    def _load_files(self):
        audio_files = ["prefix", "suffix", *map(str, range(1, 13))]
        return {af: f"times/{af}.wav" for af in audio_files}

    def speak(self):

        this_hour = datetime.datetime.now().hour % 12

        selected = ["prefix", str(this_hour), "suffix"]

        for file in selected:
            self.process(file)
        self.p.terminate()

    def process(self, filename):
        print("<Processing---", filename)
        wf = wave.open(self.times[filename])

        # Open a .Stream object to write the WAV file to
        stream = self.p.open(
            format = self.p.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
        )

        data = wf.readframes(self.chunk)

        # Play the sound by writing the audio data to the stream
        while data != b'':
            stream.write(data)
            data = wf.readframes(self.chunk)

        # Close and terminate the stream
        stream.close()
        print(filename, "------Completed>")


def main():
    RasaSpeaker().speak()


if __name__ == "__main__":
    main()
