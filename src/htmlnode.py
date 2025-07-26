
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotADirectoryError

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
