import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_no_tag(self):
        node = LeafNode(tag=None, value="Some Text")
        self.assertEqual(node.to_html(), "Some Text")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        child_node_one = LeafNode("span", "child")
        child_node_two = LeafNode("p", "paragraph")
        parent_node = ParentNode("div", [child_node_one, child_node_two])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><p>paragraph</p></div>"
        )

    def test_to_html_children_props(self):
        child_node = LeafNode("a", "Link", {'href': 'https://boot.dev'})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><a href=\"https://boot.dev\">Link</a></div>"
        )

    def test_to_html_grandchildren_props(self):
        grandchild_node = LeafNode("a", "Link", {'href': 'https://boot.dev'})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><a href=\"https://boot.dev\">Link</a></span></div>"
        )

    def test_to_html_complex_children(self):
        grandchild_node_one = LeafNode("a", "Link", {'href': 'https://boot.dev'})
        grandchild_node_two = LeafNode("b", "grandchild")
        child_node_one = ParentNode("span", [grandchild_node_one])
        child_node_two = ParentNode("div", [grandchild_node_two])
        parent_node = ParentNode("div", [child_node_one, child_node_two])
        expected_html = "<div><span><a href=\"https://boot.dev\">Link</a></span><div><b>grandchild</b></div></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_no_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode('p', None)
            node.to_html()

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            child = LeafNode('b', 'child')
            node = ParentNode(None, [child])
            node.to_html()



if __name__ == '__main__':
    unittest.main()
