
from __future__ import annotations

class TreeNode:
    def __init__(self, character, frequency, left: TreeNode = None, right: TreeNode = None):
        self.frequency = frequency
        self.left = left
        self.right = right
        self.char = character

    def __str__(self):
        string = str(self.char) + " " + str(self.frequency)
        return string

