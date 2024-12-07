#!/usr/bin/env python3

import whisper
import time
from whisper.utils import get_writer
import click

@click.command()
@click.argument("file")
def main(file):

    t1_start=time.time()
    model = whisper.load_model("turbo")
    result = model.transcribe(file)
    t1_end=time.time()

    #可以选择 txt, vtt, srt, tsv, json, all
    # writer=get_writer("srt",'.')
    # writer(result,file)

    writer=get_writer("vtt",'.')
    writer(result,file)
    print("saved in vtt format")

    writer=get_writer("txt",'.')
    writer(result,file)
    print("saved in txt format")

    # with open('1.txt', 'w') as f:
    #     f.write(result['text'])

    print("time take: ",t1_end-t1_start)

if __name__ == "__main__":
    main()