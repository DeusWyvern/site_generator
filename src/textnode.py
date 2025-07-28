from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            node = LeafNode(tag=None, value=text_node.text)

        case TextType.BOLD:
            node = LeafNode(tag='b', value=text_node.text)

        case TextType.ITALIC:
            node = LeafNode(tag='i', value=text_node.text)

        case TextType.CODE:
            node = LeafNode(tag='code', value=text_node.text)

        case TextType.LINK:
            url = text_node.url
            prop = {'href': url}
            node = LeafNode(tag='a', value=text_node.text, props=prop)

        case TextType.IMAGE:
            src = text_node.url
            alt = text_node.text
            prop = {'src': src, 'alt': alt}
            node = LeafNode(tag='img', value="", props=prop)

        case _:
            raise Exception("Text Type in text node not a TextType")

    return node

