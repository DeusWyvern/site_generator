import unittest

from htmlnode import HTMLNode

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

if __name__ == '__main__':
    unittest.main()
