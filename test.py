# ---------------------------------------------------------------------------------------
# Moyesh Khanal and Charles Farmer
# 11/6/2019
# test.py
# ---------------------------------------------------------------------------------------

from __future__ import annotations
from HuffmanCompression import *


# ---------------------------------------------------------------------------------------
# class TreeNode:
#
#
#     def __init__(self, character, frequency, left: TreeNode = None, right: TreeNode = None):
#         self.frequency = frequency
#         self.left = left
#         self.right = right
#         self.char = character
#
#     def __str__(self):
#         string = str(self.char) + " " + str(self.frequency)
#         return string

# ---------------------------------------------------------------------------------------

# def compress():
#     pass
#
# def getBinaryHelper(root, code, codes_dic):
#     if root == None :
#         return
#     if root.char != "Value":
#         codes_dic[code] = root.char
#         return
#     getBinaryHelper(root.left, code + "0", codes_dic)
#     getBinaryHelper(root.right, code + "1", codes_dic)
#
# def getBinary(parent):
#     codes_dic = {}
#     root = (parent)
#     code = ""
#     getBinaryHelper(root, code, codes_dic)
#     x = 3
#
# def makeFrequency(filename):
#     freq = {}
#
#     with open("testFile.txt", "r") as line:
#         for word in line:
#             for c in word:
#                 # starts the freq count at 1, so we can add things later
#                 if c not in freq:
#                     freq[c] = 1
#                 else:
#                     freq[c] = freq[c] + 1
#     return freq

def main():
    compression = HuffmanCompression("testFile.txt")
    compression.makeFrequency()
    compression.getBinary(compression.makeTree())
    x = 3
    # freq table constructor
    # with open("testFile.txt", "r") as line:
    #     for word in line:
    #         for c in word:
    #             # starts the freq count at 1, so we can add things later
    #             if c not in freq:
    #                 freq[c] = 1
    #             else:
    #                 freq[c] = freq[c] + 1

    # Prints the value of the root node
# ---------------------------------------------------------------------------------------

# def makeTree(freqDic):
#
#     minQueue = []
#     parent = None
#
#     # creates queue with the shortest frequencies first
#     while freqDic:
#         minChar = None
#         minVal = min([v for c, v in freqDic.items()])
#         for c, v in freqDic.items():
#             if v == minVal:
#                 minChar = c
#         minQueue.append(TreeNode(minChar, minVal))
#         freqDic.pop(minChar)
#
#     # creates tree, returns parent
#     while len(minQueue) > 1:
#         newMin = minQueue[0].frequency + minQueue[1].frequency
#         parent = TreeNode("Value", newMin, minQueue[0], minQueue[1])
#         minQueue.pop(0)
#         minQueue.pop(0)
#         # if the length of the queue is 1 we know what it does next,
#         # so we do it here instead of doing another loop, then exit
#         if len(minQueue) == 1:
#             newMin = minQueue[0].frequency + parent.frequency
#             if parent.frequency > minQueue[0].frequency:
#                 parent = TreeNode("Value", newMin, minQueue[0], parent)
#             else:
#                 parent = TreeNode("Value", newMin, parent, minQueue[0])
#
#         else:
#             index = 0
#             while minQueue[index].frequency < parent.frequency:
#                 index += 1
#                 if index == len(minQueue):
#                     break
#             minQueue.insert(index, parent)
#
#     return parent

# ---------------------------------------------------------------------------------------
def printTree(parent):
    if parent:
        printTree(parent.left)
        print(parent)
        printTree(parent.right)

if __name__ == '__main__':
    main()