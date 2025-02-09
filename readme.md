You can use the `pydub` library to convert `.m4a` files to `.mp3` in Python. Here's how:

### Steps:
1. Install `pydub` and `ffmpeg`:
   ```bash
   pip install pydub
   ```
   - You also need `ffmpeg`, which you can install via:
     - **Windows**: [Download ffmpeg](https://ffmpeg.org/download.html), extract it, and add it to your system `PATH`.
     - **Linux (Debian-based)**:
       ```bash
       sudo apt install ffmpeg
       ```
     - **Mac**:
       ```bash
       brew install ffmpeg
       ```

2. Use this Python script to convert `.m4a` to `.mp3`:
   ```python
   from pydub import AudioSegment

   def convert_m4a_to_mp3(input_file, output_file):
       # Load the .m4a file
       audio = AudioSegment.from_file(input_file, format="m4a")
       # Export as .mp3
       audio.export(output_file, format="mp3", bitrate="192k")
       print(f"Converted {input_file} to {output_file}")

   # Example usage
   convert_m4a_to_mp3("input.m4a", "output.mp3")
   ```

### Notes:
- Adjust the `bitrate="192k"` for quality (higher = better quality, but larger file size).
- If `pydub` throws an error, make sure `ffmpeg` is installed and accessible via the command line.

Let me know if you need further help! 🚀