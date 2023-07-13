import exifread
import os
import shutil
import logging


# create logger
logger = logging.getLogger()

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add fromatter to ch
ch.setFormatter(formatter)

logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

'''
{'MI 5s', 'HUAWEI G730-U00', 'ARS-AL00'}

'''


def mymovefile(srcfile, dstfile):
    """
    移动文件
    @param srcfile:
    @param dstfile:
    @return:
    """
    if not os.path.isfile(srcfile):
        print("{0} is not exits!".format(srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.mkdir(fpath)
        shutil.move(srcfile, dstfile)
        print("move {0} -> {1}".format(srcfile, dstfile))


def mycopyfile(srcfile, dstfile):
    """
    拷贝源文件到目标目录中
    @param srcfile:  源文件
    @param dstfile:     目的文件
    @return:
    """
    if not os.path.isfile(srcfile) or os.path.isfile(dstfile):
        print("{0} is not exits!".format(srcfile),end='')
        print(f"目标文件{dstfile}已经存在！")
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.mkdir(fpath)
        shutil.copy(srcfile, dstfile)
        print("copy {0} -> {1}".format(srcfile, dstfile))


def exif_Image_Model(file_name):
    """
    返回 jpg文件中exif的 设备型号(Image Model)
    :param file_name: jpg文件
    :return:
    """
    with open(file_name,'rb') as fp:
        try:
            tag = exifread.process_file(fp)
            logger.debug(tag)
        except Exception as e:
            logger.error(f"读取jpg文件获取Image Model中出错,{e}")
        else:
            tag = {}

    if tag.get("Image Model") is not None:
        image_camera = str(tag.get("Image Model")).strip()
    else:
        image_camera = None

    return image_camera


def get_img_model(img_dir):
    """
    给定目录，返回文件路径名和相机型号的字典。
    @param img_dir: 要查询的目录
    :return:键位
    {
    "file_path":"Image Model",
    ...
    }

    """

    img_model_dict = {}

    for root, dirs, files in os.walk(img_dir, topdown=False):
        for file_name in files:

            logger.debug(f"开始遍历目录：{root}:{file_name}")

            if os.path.splitext(file_name)[-1][1:] == "jpg":
                file_path_name = os.path.join(root, file_name)
                logger.debug(file_path_name)
                file_image_model = exif_Image_Model(file_path_name)

                if file_image_model is not None:
                    img_model_dict[file_path_name] = file_image_model

    return img_model_dict


if __name__ == "__main__":
    img_camera_dict = get_img_model(r'F:\My Pictures\2008-08-22泰山')
    print(f'img_camera_dict:{img_camera_dict}')
    print(set(img_camera_dict.values()))
    print(len(img_camera_dict))

    for file_path, camera in img_camera_dict.items():
        print(file_path, camera)
        file_name = os.path.split(file_path)[-1]
        if camera != "HUAWEI G730-U00":
            print(file_path, camera)
