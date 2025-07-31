import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_functions import split_nodes_delimiter

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
        node = TextNode("Text node", TextType.TEXT)
        node2 = TextNode("Bold Node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("Text node", TextType.TEXT)
        node2 = TextNode("Other Node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Text node", TextType.ITALIC)
        node2 = TextNode("Text node", TextType.CODE)
        self.assertNotEqual(node, node2)

class TestTextToNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an italic node")

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, 'imgur.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {'src': 'imgur.com', 'alt': 'This is an image node'})

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, 'youtube.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'This is a link node')
        self.assertEqual(html_node.props, {'href': 'youtube.com'})

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, 'This is a code node')

    def test_unhandled(self):
        node = TextNode("This is an unhandled node", None)
        with self.assertRaises(Exception) as e:
            text_node_to_html_node(node)
        self.assertIn("Text Type in text node not a TextType", str(e.exception))

class TestMarkdownSplit(unittest.TestCase):
    def test_code_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_exception(self):
        node = TextNode("This is an **invalid node", TextType.TEXT)
        with self.assertRaises(Exception) as e:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertIn("Invalid markdown syntax", str(e.exception))

    def test_multi_node(self):
        node_one = TextNode("This is a **bold** word", TextType.TEXT)
        node_two = TextNode("This is an __italic__ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_one, node_two], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is an __italic__ word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_node_defined(self):
        node = TextNode("This is an __italic__ word", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "__", TextType.ITALIC)

        expected_nodes = [TextNode("This is an __italic__ word", TextType.ITALIC)]

        self.assertEqual(new_nodes, expected_nodes)

    def test_at_end(self):
        node = TextNode("This word is `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [TextNode("This word is ", TextType.TEXT),
                          TextNode("code", TextType.CODE)]

        self.assertEqual(new_nodes, expected_nodes)

if __name__ == '__main__':
    unittest.main()
