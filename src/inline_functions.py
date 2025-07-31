from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        split_text = node.text.split(delimiter)

        if len(split_text) %2 == 0:
            raise Exception("Invalid markdown syntax")

        split_text = list(filter(None, split_text))

        split_nodes = [TextNode(text, TextType.TEXT) if i % 2 == 0 
                        else TextNode(text, text_type) 
                        for i, text in enumerate(split_text)]
        new_nodes.extend(split_nodes)

    return new_nodes

