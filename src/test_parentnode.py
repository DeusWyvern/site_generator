import unittest

from htmlnode import ParentNode, LeafNode

class TestParenNode(unittest.TestCase):
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
