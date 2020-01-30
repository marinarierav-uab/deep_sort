import os
import argparse
from shutil import copyfile


def rename_images(src, dst):
    images = os.listdir(src)

    for image in images:
        renamed = "".join(image.split('-'))
        copyfile(src+image, dst+renamed)


def parse_args():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="Re-ID feature extractor")
    parser.add_argument('src', type=str,
                        help='directory to rename')
    parser.add_argument('dst', type=str,
                        help='renamed directory')
    return parser.parse_args()


def main():
    args = parse_args()
    rename_images(args.src, args.dst)


if __name__ == "__main__":
    main()
