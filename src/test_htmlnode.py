import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_one(self):
        prop = {'href': 'https://boot.dev'}
        node = HTMLNode('a', 'Boot.dev', children=None, props=prop)
        print("Link Test")
        print(node)
        print()

    def test_two(self):
        node = HTMLNode('p', 'Paragraph')
        print("Paragraph Test")
        print(node)
        print()

    def test_three(self):
        child = HTMLNode('p', 'Paragraph')
        child_list = [child]
        node = HTMLNode(children=child_list)
        print("Child Test")
        print(node)
        print()

    def test_four(self):
        prop = {'href': 'https://boot.dev', 'target': '_blank'}
        node = HTMLNode('a', 'Boot.dev', children=None, props=prop)
        html = node.props_to_html()
        print("Props Test")
        print(html)
        print()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print("Leaf Test")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        print()

    def test_leaf_to_html_prop(self):
        prop = {'href': 'https://boot.dev'}
        node = LeafNode(tag="a", value='Boot.dev', props=prop)
        html_string = node.to_html()
        print("Leaf Prop Test")
        print(html_string)
        print()

    def test_leaf_none_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode('p', None)
            node.to_html()




if __name__ == '__main__':
    unittest.main()
