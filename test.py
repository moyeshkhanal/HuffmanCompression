from __future__ import annotations
class TreeNode:
    def __init__(self, frequency, left : TreeNode = None, right: TreeNode = None):
        self.frequency = frequency
        self.left = left
        self.right = right

def makeTree(freqDic):
    pass

def main():
    freq = {}
    with open("testFile.txt", "r") as line:
        for word in line:
            for c in word:
                if c not in freq:
                    freq[c] = 0
                else:
                    freq[c] = freq[c] + 1

    print(freq)
    makeTree(freq)

if __name__ == '__main__':
    main()