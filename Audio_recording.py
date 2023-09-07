import pyaudio
import wave
def record_audio(filename, duration=5, sample_rate=44100, channels=1, chunk_size=1024):
    audio = pyaudio.PyAudio()
    # Configure the audio stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)
    print("Recording...")
    frames = []
    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("Finished recording.")
    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
    # Save the recorded audio to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
if __name__ == "__main__":
    output_filename = "recorded_audio.wav"
    record_duration = 10  # You can change this to the desired recording duration in seconds
    record_audio(output_filename, duration=record_duration)