import os
 
# 处理时间格式
def deal_time(timeStamp=''):
    if len(timeStamp) < 1:
        return None
 
    startTime = timeStamp.split("-->")[0].strip()
    times = startTime.split(":")
    times[-1] = times[-1][0: 5]
    # print(startTime)
    # print(times)
    ans = "[{}:{}]".format(times[1], times[2])
    # print(ans)
    return ans
 
# 进行转换
def convert_vtt_to_lrc(vtt_file_path):
    lines = []
    # 打开vtt文件进行读取
    with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
        # 读取所有行
        lines = vtt_file.readlines()
 
    # 创建对应的lrc文件名
    lrc_file_path = os.path.splitext(vtt_file_path)[0].strip('.mp3') + '.lrc'
    print(lrc_file_path)
    # lrc_file_path = "{}{}".format(lrc_file_path.split(".")[0], ".lrc")
    # print(lrc_file_path)
    # return
    timeStamp = ''
    # 打开lrc文件进行写入
    with open(lrc_file_path, 'w', encoding='utf-8') as lrc_file:
        for line in lines:
            if line.strip().isnumeric():
                continue
 
            # 如果行以时间戳格式开始，则跳过（vtt文件中的时间戳行不需要复制到lrc文件）
            if line.strip().startswith(('00:', '01:', '02:', '03:', '04:', '05:', '06:', '07:', '08:', '09:')):
                timeStamp = deal_time(line.strip())
                # print(timeStamp)
                continue
 
            # 将其他行写入lrc文件
            lrc_file.write(timeStamp + line)
            # print(timeStamp + line)
            timeStamp = ""
 
    # remove_blank_lines(vtt_file_path)
 
def convert_vtt_files_to_lrc(directory):
    # 获取目录下的所有文件和文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 拼接文件的完整路径
            file_path = os.path.join(root, file)
            # 如果文件是vtt文件，则进行转换
            if file.endswith('.vtt'):
                print(f"Converting {file} to LRC...")
                convert_vtt_to_lrc(file_path)
            # elif file.endswith('.lrc'):
            #     cut(file_path)
  
# 测试程序
if __name__ == "__main__":
    # 输入要处理的目录路径
    directory_path = input("请输入要处理的目录路径：")
    # 调用函数将vtt文件转换为lrc文件
    convert_vtt_files_to_lrc(directory_path)
    print("Conversion completed!")
