import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_props(self):
        prop = {'href': 'https://boot.dev'}
        node = HTMLNode('a', 'Boot.dev', children=None, props=prop)
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'Boot.dev')
        self.assertEqual(node.props, {'href': 'https://boot.dev'})
        self.assertEqual(node.children, None)

    def test_html_tag_value(self):
        node = HTMLNode('p', 'Paragraph')
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'Paragraph')
        self.assertEqual(node.props, None)
        self.assertEqual(node.children, None)

    def test_html_child(self):
        child = HTMLNode('p', 'Paragraph')
        child_list = [child]
        node = HTMLNode(children=child_list)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.props, None)
        self.assertEqual(node.children, [child])

    def test_props_to_html(self):
        prop = {'href': 'https://boot.dev', 'target': '_blank'}
        node = HTMLNode('a', 'Boot.dev', children=None, props=prop)
        html = node.props_to_html()
        self.assertEqual(node.props, prop)
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'Boot.dev')
        self.assertEqual(html, " href=\"https://boot.dev\" target=\"_blank\"")

if __name__ == '__main__':
    unittest.main()
