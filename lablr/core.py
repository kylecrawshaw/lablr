from __future__ import print_function

from collections import namedtuple

from PIL import ImageFont, ImageDraw, Image, PngImagePlugin


class BaseRegion(object):

    def __init__(self, name, type='region', bg_color=(255, 255, 255), size=(200, 200), position=(0, 0)):
        self.bg_color = bg_color
        self.image = None
        self.size = size
        self.name = name
        self.type = type
        self.size = size
        self.position = position
        self.is_rendered = False

    @property
    def position(self):
        if None in (self.__x, self.__y):
            return None

        return namedtuple('position', ('x', 'y'))(self.__x, self.__y)

    @position.setter
    def position(self, coords):
        self.__x = int(coords[0])
        self.__y = int(coords[1])

    @property
    def size(self):
        if None in (self.__width, self.__height):
            return None

        return namedtuple('size', ('width', 'height'))(self.__width, self.__height)

    @size.setter
    def size(self, size):
        self.__width = size[0]
        self.__height = size[1]

    @property
    def position_below(self):
        position_x = self.position.x
        position_y = self.size.height + self.position.y

        return position_x, position_y

    @property
    def position_right(self):
        position_x = self.size.width + self.position.x
        position_y = self.position.y

        return position_x, position_y

    def resize(self, resize_ratio):
        new_width = int(self.size.width * resize_ratio)
        new_height = int(self.size.height * resize_ratio)
        self.size = (new_width, new_height)

    def fit_within_bounds(self, size):
        width = size[0]
        height = size[1]
        min_bounds = min(width, height)
        min_image = min(self.size.width, self.size.height)
        if min_image > min_bounds:
            resize_ratio = float(min_bounds) / float(min_image)
        elif min_image < min_bounds:
            resize_ratio = float(min_image) / float(min_bounds)
        else:
            resize_ratio = 1
        self.resize(resize_ratio)

    def save(self, path):
        self.render()
        self.image.save(path)

    def render(self):
        if isinstance(self.image, (Image.Image, PngImagePlugin.PngImageFile)):
            self.image = self.image.resize(self.size)
        else:
            self.image = Image.new('RGB', self.size, self.bg_color)


class ImageItem(BaseRegion):

    def __init__(self, image, name=None, **kwargs):

        BaseRegion.__init__(self, name=name, **kwargs)

        if isinstance(image, str):
            self.image = Image.open(image)
        elif isinstance(image, (Image.Image, PngImagePlugin.PngImageFile)):
            self.image = image

        self.size = self.image.size


class TextItem(BaseRegion):

    def __init__(self, text, name, font_name='Arial.ttf', font_size=18,
                 font_color=(0, 0, 0), bg_color=(255, 255, 255), padding=10):
        BaseRegion.__init__(self, name=name, bg_color=bg_color, type='text')
        self.text = text
        self.font_name = font_name
        self.font_size = font_size
        self.font_color = font_color
        self.padding = padding
        self.size = self.font.getsize(text)

    @property
    def font(self):
        return ImageFont.truetype(self.font_name, self.font_size)

    def getsize(self, text):
        width, height = self.font.getsize(self.text)
        return namedtuple('size', ('width', 'height'))(width, height)

    def render(self):
        self.size = (self.size.width+(self.padding*2), self.size.height+(self.padding*2))
        BaseRegion.render(self)
        draw = ImageDraw.Draw(self.image)
        draw.text((self.padding, self.padding), self.text, self.font_color, font=self.font)

    def fit_within_bounds(self, size):
        width = size[0]
        height = size[1]
        BaseRegion.fit_within_bounds(self, (width, height))
        new_font_size = self.font_size

        if self.getsize(self.text).width >= self.size.width:
            while self.getsize(self.text).width >= self.size.width:
                self.font_size -= 1
        else:
            while self.getsize(self.text).width < self.size.width:
                self.font_size += 1
        self.font_size = new_font_size


class Region(BaseRegion):

    def __init__(self, name, **kwargs):
        BaseRegion.__init__(self, name, type='region', **kwargs)
        self.label_items = list()

    def add_item(self, label_item, position=None):
        if position:
            label_item.position = position
        self.label_items.append(label_item)

    def render(self):
        BaseRegion.render(self)
        for component in self.label_items:
            component.render()
            self.image.paste(component.image, component.position)


class SingleItemRegion(BaseRegion):

    def __init__(self, name, label_item, align='left', vertical_align='top',
                 x_offset=0, y_offset=0, fit=False, **kwargs):
        BaseRegion.__init__(self, name, **kwargs)
        self.label_item = label_item
        self.align = align
        self.vertical_align = vertical_align
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.fit = fit

    def _update_item_position(self):
        if self.align == 'left':
            x = 0 + self.x_offset
        elif self.align == 'center':
            x = ((self.size.width - self.label_item.size.width) / 2) + self.x_offset
        elif self.align == 'right':
            x = (self.size.width - self.label_item.size.width) + self.x_offset
        else:
            raise ValueError('"align" must be one of {}'.format(('left', 'center', 'right')))

        if self.vertical_align == 'top':
            y = 0 + self.y_offset
        elif self.vertical_align == 'middle':
            y = ((self.size.height- self.label_item.size.height) / 2) + self.y_offset
        elif self.vertical_align == 'bottom':
            y = (self.size.height - self.label_item.size.height) + self.y_offset
        else:
            raise ValueError('"vertical_align" must be one of {}'.format(('top', 'middle', 'bottom')))
        self.label_item.position = (x, y)

    def render(self):
        BaseRegion.render(self)
        if self.fit:
            self.label_item.fit_within_bounds(self.size)
        self.label_item.render()
        self._update_item_position()
        self.image.paste(self.label_item.image, self.label_item.position)

