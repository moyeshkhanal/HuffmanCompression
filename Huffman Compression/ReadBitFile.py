#!/usr/bin/env python3.6

# ----------------------------------------------------------------------
# ReadBitFile.py
# Dave Reed
# 11/01/2017
# ----------------------------------------------------------------------

import struct

# ----------------------------------------------------------------------

class ReadBitFile:

    """

    """

    # ------------------------------------------------------------------

    def __init__(self, filename: str):

        """

        :param filename: file to read from
        """

        self.infile = open(filename, "rb")
        self.bitValue = 0
        self.numberOfBits = 0

    # ------------------------------------------------------------------

    def _resetBits(self):

        """
        helper method to start reading bits fresh
        :return: None
        """

        self.bitValue = 0
        self.numberOfBits = 0

    # ------------------------------------------------------------------

    def readBit(self) -> int:

        """
        read a single bit from file
        :return: the bit 0 or 1 as an int
        """

        # if no bits remaining in the byte we read, read a new byte
        if self.numberOfBits == 0:
            self.bitValue = self.readUByte()
            self.numberOfBits = 8

        # get the left most bit
        b = (self.bitValue & 128) >> 7
        # shift so leftmost bit is ready for next call
        self.bitValue = (self.bitValue << 1)
        self.numberOfBits -= 1
        return b

    # ------------------------------------------------------------------

    def readUByte(self) -> int:

        """
        read an unsigned byte from the file
        :return: the unsigned byte that was read as an int
        """

        self._resetBits()
        s = self.infile.read(1)
        if len(s) != 1:
            raise ValueError("ReadBitFile.readUInt error")
        v = struct.unpack('<B', s)[0]
        return v

    # ------------------------------------------------------------------

    def readUShort(self) -> int:

        """
        read an unsigned short from the file
        :return: the unsigned short that was read as an int
        """

        self._resetBits()
        s = self.infile.read(2)
        if len(s) != 2:
            raise ValueError("ReadBitFile.readUInt error")
        v = struct.unpack('<H', s)[0]
        return v

    # ------------------------------------------------------------------

    def readUInt(self) -> int:

        """
        read an unsigned int from the file
        :return: the unsigned int that was read as an int
        """

        self._resetBits()
        s = self.infile.read(4)
        if len(s) != 4:
            raise ValueError("ReadBitFile.readUInt error")
        v = struct.unpack('<I', s)[0]
        return v

    # ------------------------------------------------------------------

    def close(self):

        """
        close the file
        :return: None
        """

        self.infile.close()


    # ------------------------------------------------------------------
