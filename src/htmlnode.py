
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = self.props
        prop_string = ""
        if props is None:
            return prop_string
        for key, value in props.items():
            prop_string = prop_string + f' {key}="{value}"'
        return prop_string

    def __repr__(self):
        string = f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"
        return string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        tag = self.tag
        value = self.value
        props = self.props_to_html()
        string = f'<{tag}{props}>{value}</{tag}>'
        return string

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError

        if self.children is None:
            raise ValueError("ValueError: Parent Node has no children.")

        tag = self.tag
        children = self.children
        props = self.props_to_html()

        if props is None:
            props = ""

        string = f'<{tag}{props}>'

        for child in children:
            string += f'{child.to_html()}'

        string += f'</{tag}>'

        return string
