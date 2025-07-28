import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_prop(self):
        prop = {'href': 'https://boot.dev'}
        node = LeafNode(tag="a", value='Boot.dev', props=prop)
        html_string = node.to_html()
        self.assertEqual(html_string, "<a href=\"https://boot.dev\">Boot.dev</a>")

    def test_leaf_none_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode('p', None)
            node.to_html()

if __name__ == '__main__':
    unittest.main()
