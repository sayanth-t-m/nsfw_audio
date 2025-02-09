from pydub import AudioSegment

def convert_m4a_to_mp3(input_file, output_file):
    """
    Converts an .m4a audio file to .mp3 format.

    Parameters:
    - input_file: str : Path to the .m4a file.
    - output_file: str : Path to save the converted .mp3 file.
    """
    try:
        # Load the .m4a file
        audio = AudioSegment.from_file(input_file, format="m4a")
        
        # Export as .mp3 with 192 kbps bitrate
        audio.export(output_file, format="mp3", bitrate="192k")

        print(f"✅ Successfully converted '{input_file}' to '{output_file}'")

    except Exception as e:
        print(f"❌ Error: {e}")

# Input and output file paths
input_file = r"C:\Users\sayan\Downloads\Test1.m4a"  # Use raw string (r"") to avoid path issues
output_file = r"C:\Users\sayan\Downloads\Test1.mp3"  # Save in the same location

# Convert the file
convert_m4a_to_mp3(input_file, output_file)
