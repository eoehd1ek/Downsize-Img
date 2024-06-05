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


def is_image_file(file_path):
    file_ext = splitext(sys.argv[1])[-1]
    return file_ext in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]


def main():
    if len(sys.argv) != 2:
        print('drag single image file into this program.')
        getch()
        return

    if (not is_image_file(sys.argv[1])):
        print('file extension is not supported.')
        print('supported extensions: .jpg, .jpeg, .png, .bmp, .webp')
        getch()
        return

    try:
        image = Image.open(sys.argv[1]).convert("RGB")
        [x, y] = image.size
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
        result_image = image.resize((result_x, result_y))
        result_image.save(splitext(sys.argv[1])[
                          0] + "_pressed.jpg", quality=IMAGE_QUALITY)
        image.close()
        result_image.close()
    except:
        print('failed to open image file.')
        getch()
        return


if __name__ == "__main__":
    main()
