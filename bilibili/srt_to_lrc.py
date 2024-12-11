'''
Run it in srt file folder.
python 3.x
'''
import re
import click
import os


SRT_BLOCK_REGEX = re.compile(
        r'(\d+)[^\S\r\n]*[\r\n]+'
        r'(\d{2}:\d{2}:\d{2},\d{3,4})[^\S\r\n]*-->[^\S\r\n]*(\d{2}:\d{2}:\d{2},\d{3,4})[^\S\r\n]*[\r\n]+'
        r'([\s\S]*)')

err_info = []

def srt_block_to_irc(block):
    match = SRT_BLOCK_REGEX.search(block)
    if not match:
        return None
    num, ts, te, content = match.groups()

    ts = ts[3:-1].replace(',', '.')
    te = te[3:-1].replace(',', '.')
    co = content.replace('\n', ' ')
    return '[%s]%s\n[%s]\n' % (ts, co, te)


def srt_file_to_irc(file):
    with open(file, 'r') as file_in:
        str_in = file_in.read()
        blocks_in = str_in.replace('\r\n', '\n').split('\n\n')

        blocks_out = [srt_block_to_irc(block) for block in blocks_in]
        if not all(blocks_out):
            err_info.append((file, blocks_out.index(None), blocks_in[blocks_out.index(None)]))
        blocks_out = filter(None, blocks_out)
        str_out = ''.join(blocks_out)

        lrc_file_name=os.path.basename(file).split('.')[0]+".lrc"
        with open(lrc_file_name, 'w') as file_out:
            file_out.write(str_out)

@click.command()
@click.argument("file")
def main(file):
    """tool to convert srt subtitle file to lrc format."""

    srt_file_to_irc(file)
    if err_info:
        print('success, but some exceptions are ignored:')
        for file_name, blocks_num, context in err_info:
            print('\tfile: %s, block num: %s, context: %s' % (file_name, blocks_num, context))
    else:
        print('success')

if __name__ == '__main__':
    main()