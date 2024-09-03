from os.path import splitext
import sys
from msvcrt import getch
from PIL import Image


#####################
##   이곳만 수정    ##
#####################
IMAGE_QUALITY = 70
HEIGHT_LIMIT = 1000
#####################
#####################


def get_result_image_size(x, y):
    result_x = x
    result_y = y
    if (x == y):
        # 1:1 비율일 때
        result_x = min(x, HEIGHT_LIMIT)
        result_y = min(y, HEIGHT_LIMIT)
    else:
        # 1:1이 아닐 땐
        # 최대 ? x 1000 해상도로 맞추고 싶음.
        if (y > HEIGHT_LIMIT):
            result_x = int(x * HEIGHT_LIMIT / y)
            result_y = int(y * HEIGHT_LIMIT / y)
    return (result_x, result_y)


def get_result_file_path(file_path):
    result = f"{splitext(file_path)[0]}_pressed.jpg"
    return result


def main():
    if (len(sys.argv) <= 1):
        print("drag image files into this program. :)")
        getch()
        return

    for i in range(1, len(sys.argv)):
        try:
            image = Image.open(sys.argv[i]).convert("RGB")
            result_image = image.resize(get_result_image_size(*image.size))
            result_image.save(get_result_file_path(
                sys.argv[i]), quality=IMAGE_QUALITY)
            image.close()
            result_image.close()
        except:
            print('failed to open image file.')
            continue


if __name__ == "__main__":
    main()
