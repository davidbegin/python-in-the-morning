def is_tuple(node):
    if isinstance(node, Node) and node.children == [LParen(), RParen()]:
        return True
    return (isinstance(node, Node)
            and len(node.children) == 3
            and isinstance(node.children[0], Leaf)
            and isinstance(node.children[1], Node)
            and isinstance(node.children[2], Leaf)
            and node.children[0].value == "("
            and node.children[2].value == ")")

## Which is Better

def is_tuple(node: Node) -> bool:
    match node:
        case Node(children=[LParen(), RParen()]):
            return True
        case Node(children=[Leaf(value="("), Node(), Leaf(value=")")]):
            return True
        case _:
            return False
