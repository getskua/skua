import enum
from typing import List


class PageType(enum.Enum):
    MARKDOWN = 1
    HTML = 2


class OutputFormats(enum.Enum):
    HTML = 1
    EBOOK = 2
    PDF = 3


class Page(object):
    def __init__(self, *args, **kwargs):
        setattr(self, 'page_type', self.page_type)
        setattr(self, 'output_formats', self.output_formats)

    def render(self):
        """
        :return:
        """
        pass


class Collection(object):
    def __init__(self, pages: List[Page], page_types: PageType = PageType.MARKDOWN):
        self.pages = pages

    def output_name_generator(self, page: Page) -> str:
        """
        This method should be subclassed and give the output path of the document.
        :return:
        """
        pass
