import whisper

# Load the model (turbo model in this case)
model = whisper.load_model("turbo")

# Transcribe the audio file (adjust the path as needed)
result = model.transcribe(r"C:\Users\sayan\Downloads\Test1.mp3")
print("Transcribed Text:", result["text"])
