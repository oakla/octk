from octk import pytree
import pytest


def test_pytree():
    test_path = r'.'
    tree = pytree.FileTree(pytree.Path(test_path))
    assert tree
    assert str(tree)
    assert tree.output_tree_lines
    assert tree.output_message_lines
    

