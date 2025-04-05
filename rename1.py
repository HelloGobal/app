import os
import re


def rename_video_files(folder_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 {folder_path} 不存在。")
        return
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # 检查是否为文件
        if os.path.isfile(file_path):
            # 检查文件名中是否包含括号
            if '(' in filename and ')' in filename:
                # 使用正则表达式删除括号及其内部内容
                new_filename = re.sub(r'\([^)]*\)', '', filename)
                # 去除多余的空格
                new_filename = new_filename.strip()
                new_file_path = os.path.join(folder_path, new_filename)
                try:
                    # 重命名文件
                    os.rename(file_path, new_file_path)
                    print(f"已将 {filename} 重命名为 {new_filename}")
                except Exception as e:
                    print(f"重命名 {filename} 时出错：{e}")


if __name__ == "__main__":
    # 请替换为你实际的文件夹路径
    folder_path = 'your_folder_path'
    rename_video_files(folder_path)
