#!/usr/bin/env python3.6

# ----------------------------------------------------------------------
# test_ReadWrite.py
# Dave Reed
# 11/01/2017

# ----------------------------------------------------------------------

import sys
import unittest
import os

sys.path.insert(0, '..')
from WriteBitFile import *
from ReadBitFile import *


# ----------------------------------------------------------------------

class ReadWriteTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def testMixed(self):

        w = WriteBitFile("data.bin")
        w.writeBit(1)
        w.writeBit(0)
        w.writeBit(1)
        w.writeBit(1)
        w.writeUInt(10000042)
        w.writeBit(1)
        w.writeBit(0)
        w.writeUShort(50000)
        w.writeBit(1)
        w.writeUByte(42)
        w.close()

        r = ReadBitFile("data.bin")
        b = r.readBit()
        self.assertEqual(b, 1)
        b = r.readBit()
        self.assertEqual(b, 0)
        b = r.readBit()
        self.assertEqual(b, 1)
        b = r.readBit()
        self.assertEqual(b, 1)
        value = r.readUInt()
        self.assertEqual(value, 10000042)
        b = r.readBit()
        self.assertEqual(b, 1)
        b = r.readBit()
        self.assertEqual(b, 0)
        value = r.readUShort()
        self.assertEqual(value, 50000)
        b = r.readBit()
        self.assertEqual(b, 1)
        value = r.readUByte()
        self.assertEqual(value, 42)
        r.close()

        os.remove("data.bin")

    # ------------------------------------------------------------------

    def testB(self):

        w = WriteBitFile("data2.bin")
        for i in range(4):
            w.writeBit(1)
            w.writeBit(0)
        w.close()
        # self.assertEqual(True, True)

    # ------------------------------------------------------------------


# ----------------------------------------------------------------------

def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        # raised by sys.exit(True) when tests failed
        if inst.args[0] is True:
            raise


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
