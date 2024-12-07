## 官网地址
url address:  https://github.com/openai/whisper

## 安装

whisper 需要先安装 ffmpeg , 用来把音频文件转成 wav 格式的文件。

然后安装whisper

`pip install -U openai-whisper`

## 语言转文字使用:

`whisper input.mp3`

或者 

`python -m whisper input.mp3`

## 播放音频并显示字幕
* linux/mac 使用 mpv 播放器，
* windows 下使用 potplayer 播放器

## 说明
* whisper在mac上不能调用gpu, 速度慢
* whisper在linux上可以使用gpu.
