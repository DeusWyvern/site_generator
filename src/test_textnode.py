import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Url Node", TextType.LINK, 'http://www.youtube.com')
        node2 = TextNode("Url Node", TextType.LINK, 'http://www.youtube.com')
        self.assertEqual(node, node2)

    def url_image_eq(self):
        node = TextNode("Link node", TextType.IMAGE)
        node2 = TextNode("Link node", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Text node", TextType.PLAIN)
        node2 = TextNode("Bold Node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("Text node", TextType.PLAIN)
        node2 = TextNode("Other Node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Text node", TextType.ITALIC)
        node2 = TextNode("Text node", TextType.CODE)
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    unittest.main()
