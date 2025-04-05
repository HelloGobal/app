import os

def rename_video_files(folder_path):
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in video_extensions:
                    old_file_path = os.path.join(root, file)
                    new_file_name = file[53:] if len(file) > 50 else file
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(old_file_path, new_file_path)
                    print(f"已将 {old_file_path} 重命名为 {new_file_path}")
    except FileNotFoundError:
        print(f"错误: 指定的文件夹路径 {folder_path} 未找到。")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")


if __name__ == "__main__":
    folder_path = 'your_folder_path'
    rename_video_files(folder_path)
    
