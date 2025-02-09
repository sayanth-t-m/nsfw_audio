from pydub import AudioSegment

def convert_m4a_to_mp3(input_file, output_file):
    # Load the .m4a file
    audio = AudioSegment.from_file(input_file, format="m4a")
    # Export as .mp3
    audio.export(output_file, format="mp3", bitrate="192k")
    print(f"Converted {input_file} to {output_file}")

# Example usage
convert_m4a_to_mp3("input.m4a", "output.mp3")
