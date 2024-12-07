#!/usr/bin/env python3

import os
import subprocess
import click

@click.command()
@click.argument("file")
def main(file):
    result_dir="result"
    os.makedirs(result_dir, exist_ok=True)
    temp_audio_path = os.path.join(result_dir, "temp.wav")

    filename=os.path.basename(file)

    if not filename:
        raise click.BadParameter("No filename provided")
    
    file_basename, _ = os.path.splitext(filename)
    result_file=os.path.join(result_dir, file_basename)

    # Run ffmpeg command to convert audio to WAV format
    cmd = [
        "ffmpeg",
        "-nostdin",
        "-threads", "0",
        "-i", file,
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        "-f", "wav",
        "-y",
        temp_audio_path
    ]

    # print("Running ffmpeg command:")
    print("step 1: "," ".join(cmd)) 

    subprocess.run(cmd, stderr=subprocess.DEVNULL, check=True)

    # Use the converted file for inference
    command = f"./main -m model/ggml-large-v3-turbo.bin -otxt -ovtt -of {result_file} -f {temp_audio_path} -pp -np"
    print("step 2: ",command)

    subprocess.run(command, shell=True)
    # result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True, text=True)
    # prediction = result.stdout.strip()
    # print(prediction)

    # Remove the temporary file
    print("step 3: ","remove temp audio file:", temp_audio_path)
    os.remove(temp_audio_path)

    print(f"Done!")

if __name__ == "__main__":
    main()
