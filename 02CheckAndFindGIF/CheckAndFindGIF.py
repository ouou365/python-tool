from PIL import Image
import os


def check_and_rename_images(folder_path):
    """
    检测指定文件夹下后缀名为png但实际为gif的图片并改名
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[-1].lower()
            if file_extension == '.png':
                try:
                    img = Image.open(file_path)
                    if img.format == 'GIF':
                        new_file_path = os.path.splitext(file_path)[0] + '.gif'
                        os.rename(file_path, new_file_path)
                        print(f"已将 {file_path} 重命名为 {new_file_path}")
                except:
                    continue


if __name__ == "__main__":
    folder_path = input("请输入要检测的文件夹路径: ")
    if os.path.exists(folder_path):
        check_and_rename_images(folder_path)
    else:
        print("输入的文件夹路径不存在，请重新输入。")