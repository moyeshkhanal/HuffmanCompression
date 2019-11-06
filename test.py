# ---------------------------------------------------------------------------------------
# Moyesh Khanal and Charles Farmer
# 11/6/2019
# test.py
# ---------------------------------------------------------------------------------------

from __future__ import annotations

# ---------------------------------------------------------------------------------------

class TreeNode:


    def __init__(self, character, frequency, left: TreeNode = None, right: TreeNode = None):
        self.frequency = frequency
        self.left = left
        self.right = right
        self.char = character

    def __str__(self):
        string = str(self.char) + " " + str(self.frequency)
        return string


# ---------------------------------------------------------------------------------------

def main():
    freq = {}
    # freq table constructor
    with open("testFile2.txt", "r") as line:
        for word in line:
            for c in word:
                # starts the freq count at 1, so we can add things later
                if c not in freq:
                    freq[c] = 1
                else:
                    freq[c] = freq[c] + 1

    print(makeTree(freq))

# ---------------------------------------------------------------------------------------
def makeTree(freqDic):

    minQueue = []
    parent = None

    # creates queue with the shortest frequencies first
    while freqDic:
        minChar = None
        minVal = min([v for c, v in freqDic.items()])
        for c, v in freqDic.items():
            if v == minVal:
                minChar = c
        minQueue.append(TreeNode(minChar, minVal))
        freqDic.pop(minChar)

    # creates tree, returns parent
    while len(minQueue) > 1:
        newMin = minQueue[0].frequency + minQueue[1].frequency
        parent = TreeNode("Value", newMin, minQueue[1], minQueue[0])
        minQueue.pop(0)
        minQueue.pop(0)
        if len(minQueue) == 1:
            newMin = minQueue[0].frequency + parent.frequency
            if parent.frequency > minQueue[0].frequency:
                parent = TreeNode("Value", newMin, minQueue[0], parent)
            else:
                parent = TreeNode("Value", newMin, parent, minQueue[0])
        else:
            index = 0
            while minQueue[index].frequency < parent.frequency:
                index += 1
                if index == len(minQueue):
                    break
            minQueue.insert(index, parent)

    return parent

# ---------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()