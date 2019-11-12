from TreeNode import *
import pickle
#https://wiki.python.org/moin/UsingPickle

class HuffmanCompression:

    def __init__(self, filename):
        self.codesDictionary = {}
        self.filename = filename
        self.freq = {}

    def __getBinaryHelper(self, root, code):
        if root == None:
            return
        if root.char != "Value":
            self.codesDictionary[code] = root.char
            return
        self.__getBinaryHelper(root.left, code + "0")
        self.__getBinaryHelper(root.right, code + "1")

    def getBinary(self, parent):
        root = (parent)
        code = ""
        self.__getBinaryHelper(root, code)

    def makeFrequency(self):
        with open(self.filename, "r") as line:
            for word in line:
                for c in word:
                    # starts the freq count at 1, so we can add things later
                    if c not in self.freq:
                        self.freq[c] = 1
                    else:
                        self.freq[c] = self.freq[c] + 1
    def makeTree(self):
        freqDic = self.freq
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
            parent = TreeNode("Value", newMin, minQueue[0], minQueue[1])
            minQueue.pop(0)
            minQueue.pop(0)
            # if the length of the queue is 1 we know what it does next,
            # so we do it here instead of doing another loop, then exit
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

    def compress(self):
        codedChr = self.codesDictionary
        pickle.dump(codedChr, open("pickleTest.txt", "wb"))
    def deCompress(self):

        codedChr = pickle.load(open("pickleTest.txt", "rb"))
        return codedChr