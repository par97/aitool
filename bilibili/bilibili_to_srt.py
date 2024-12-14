#!/usr/bin/env python3

import json
import click
import os

def float2hhmmss(num):
    int_ = int(num)
    frac = int((num - int_) * 1000)
    hr, min_, sec = int_ // 3600, int_ % 3600 // 60, int_ % 60
    return f'{hr:02d}:{min_:02d}:{sec:02d},{frac:03d}'

def bili_sub_to_srt(file):
    with open(file, 'r') as f:
        data = json.load(f)

        if 'body' not in data or len(data['body']) == 0:
            print("No body data found.")
            return

        subs = data['body']

        srts = []
        for i, sub in enumerate(subs, start=1):
            st = float2hhmmss(sub['from'])
            ed = float2hhmmss(sub['to'])
            txt = sub['content']
            srtpt = f'{i}\n{st} --> {ed}\n{txt}'
            srts.append(srtpt)

        srt = '\n\n'.join(srts)

        basename=os.path.basename(file)
        stem, suffix=os.path.splitext(basename)
        srt_file_name = f'{stem}.srt'

        # Write the SRT file
        with open(srt_file_name, 'w') as srt_file:
            srt_file.write(srt)

@click.command()
@click.argument("file")
def main(file):
    """tool to convert bilibili json subtitle file to srt format."""

    bili_sub_to_srt(file)

if __name__ == "__main__":
    main()