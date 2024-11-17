# importing the module
import os
import io
from PIL import Image
from PIL.ImageFile import ImageFile


class ImageConverter:
    def __init__(self, img):
        self.img = img
        self.new_image = None
        self.base_location = os.path.dirname(os.path.abspath(__file__))
        self.converted_png_images = os.path.join(self.base_location, "converted_png_images/")
        self.converted_jpg_images = os.path.join(self.base_location, "converted_jpg_images/")
        self.image_width = None
        self.image_height = None
        self.new_image_name = None

    def open_image(self) -> ImageFile:
        self.new_image = Image.open(self.img)
        return self.new_image

    def initialize_image_conversion_jpg(self) -> None:
        self.new_image = self.new_image.convert("RGB")

    def initialize_image_conversion_png(self) -> None:
        self.new_image = self.new_image.convert("RGBA")

    def get_image_width(self) -> int:
        return self.new_image.width

    def get_image_height(self) -> int:
        return self.new_image.height

    def get_image_width_and_height(self) -> tuple:
        self.get_image_height()
        self.get_image_width()
        return self.get_image_width(), self.get_image_height()

    def get_possible_image_formats(self) -> dict[str, str]:
        return Image.registered_extensions()

    def get_possible_image_sizes(self) -> object:
        # and object with posible image sizes
        all_possible_box = {
            "icon": (16, 16),
            "thumbnail": (128, 128),
            "small": (256, 256),
            "medium": (512, 512),
            "large": (1024, 1024),
            "large2": (1280, 1280),
            "xlarge": (1920, 1920),
            "2xlarge": (2048, 2048),
            "3xlarge": (2560, 2560),
            "4xlarge": (3840, 3840),
            "5xlarge": (4096, 4096),
        }

        all_possible_landscapes = {
            "landscape": (1024, 768),
            "landscape2": (1280, 720),
            "landscape3": (1366, 768),
            "landscape4": (1600, 900),
            "landscape5": (1920, 1080),
            "landscape6": (2560, 1440),
            "landscape7": (3840, 2160),
            "landscape8": (4096, 2160),
        }

        all_possible_portraits = {
            "portrait": (768, 1024),
            "portrait2": (720, 1280),
            "portrait3": (768, 1366),
            "portrait4": (900, 1600),
            "portrait5": (1080, 1920),
            "portrait6": (1440, 2560),
            "portrait7": (2160, 3840),
            "portrait8": (2160, 4096),
        }

        return {
            "all_possible_box": all_possible_box,
            "all_possible_landscapes": all_possible_landscapes,
            "all_possible_portraits": all_possible_portraits
        }

    def resize_image(self, image, width=None, height=None):
        self.image_width, self.image_height = self.get_image_width_and_height()
        if width is None and height is None:
            width = self.image_width
            height = self.image_height
        elif width is None:
            width = self.image_width
        elif height is None:
            height = self.image_height

        return image.resize([width, height])

    def rename_image_with_underscore(self, new_image_name) -> str:
        return self.new_image_name.replace(" ", "_")

    def rename_image_with_hyphen(self, new_image_name) -> str:
        return self.new_image_name.replace(" ", "-")

    # def save_image_as_jpg(self, new_image_name, width=None, height=None):
    #     self.open_image()
    #     self.initialize_image_conversion_jpg()
    #     # FolderHandler(self.converted_jpg_images).create_dirs_if_not_exists()
    #     self.resize_image(width, height)
    #     # self.new_image.save(f"{self.converted_jpg_images}{new_image_name}.jpg")
    #     return self.new_image, new_image_name

    def get_image_format(self, img) -> str:
        return img.format

    def get_converted_image(self, new_image_name, width=None, height=None, _format=None):

        with self.open_image() as img:
            if _format is None:
                _format = self.get_image_format(img)
            img_byte_array = io.BytesIO()
            resized_image = self.resize_image(img,width, height)
            resized_image.save(img_byte_array, format=_format)
            img_byte_array.seek(0)
            return img_byte_array.read(), new_image_name
