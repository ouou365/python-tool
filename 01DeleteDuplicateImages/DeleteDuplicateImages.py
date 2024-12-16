import os
from PIL import Image
import imagehash


def get_image_hashes(folder_path):
    """
    获取指定文件夹下所有图片的哈希值以及对应的文件路径
    """
    image_hashes = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                img = Image.open(file_path)
                hash_value = imagehash.average_hash(img)
                if hash_value in image_hashes:
                    image_hashes[hash_value].append(file_path)
                else:
                    image_hashes[hash_value] = [file_path]
            except:
                continue
    return image_hashes


def delete_duplicate_images(image_hashes):
    """
    根据图片哈希值删除重复的图片，只保留一份
    """
    for hash_value, file_paths in image_hashes.items():
        if len(file_paths) > 1:
            # 保留一份，删除其余重复的图片
            for file_path in file_paths[1:]:
                os.remove(file_path)


if __name__ == "__main__":
    folder_path = input("请输入要检测的Windows文件夹路径: ")
    if os.path.exists(folder_path):
        image_hashes = get_image_hashes(folder_path)
        delete_duplicate_images(image_hashes)
        print("重复图片删除完成。")
    else:
        print("输入的文件夹路径不存在，请重新输入。")