## 官网地址
url address:  https://github.com/ggerganov/whisper.cpp

## 安装

whisper.cpp 无需安装 ffmpeg，但只能识别 wav 格式的文件.

所以，一般也需要先安装 ffmpeg，用来把音频文件转成 wav 格式的文件。

然后安装whisper.cpp，需要下载源码并编译。

## 语言转文字使用:

whisper.cpp 只能接受 wav 格式的音频文件。
需要先将音频转成wav格式，然后再运行whisper.cpp。
这儿使用run.py脚本来自动化这些步骤。

直接把run.py放到whisper.cpp目录下，执行 `./run.py ./1.mp3`

会把同名的 txt,srt 文件放到result目录下。

## 播放音频并显示字幕
* linux/mac 使用 mpv 播放器，
* windows 下使用 potplayer 播放器

## 说明
* whisper.cpp 在mac上能调用gpu
