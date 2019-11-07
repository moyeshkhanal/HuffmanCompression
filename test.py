from __future__ import annotations
from ReadBitFile import *
class TreeNode:
    def __init__(self, frequency, left : TreeNode = None, right: TreeNode = None):
        self.frequency = frequency
        self.left = left
        self.right = right

def makeTree(freqDic):
    pass

def main():
    freq = {}
    # freq table constructor
    with open("testFile.txt", "r") as line:
        for word in line:
            for c in word:
                # starts the freq count at 0
                if c not in freq:
                    freq[c] = 0
                else:
                    freq[c] = freq[c] + 1

    print(freq)
    makeTree(freq)

if __name__ == '__main__':
    main()