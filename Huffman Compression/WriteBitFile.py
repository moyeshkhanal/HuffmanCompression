#!/usr/bin/env python3.6

# ----------------------------------------------------------------------
# WriteBitFile.py
# Dave Reed
# 11/01/2017
# ----------------------------------------------------------------------

import struct

# ----------------------------------------------------------------------

class WriteBitFile:
    """ """

    # ------------------------------------------------------------------

    def __init__(self, filename: str):

        """

        :param filename: name of file we are creating/writing to
        :var self.outfile: var for file we're writing to
        :var self.bitValue: bits that will be written once a byte
        :var self.numberOfBits: total number of bits in the outfile
        """

        self.outfile = open(filename, 'wb')
        self.bitValue = 0
        self.numberOfBits = 0

    # ------------------------------------------------------------------

    def writeBit(self, bit: int):

        """
        write a single bit to the file
        :param bit: 0 or 1 to write to file
        :return: None
        """

        assert bit == 0 or bit == 1
        self.bitValue = (self.bitValue << 1) + bit
        self.numberOfBits += 1
        # so only a byte is written at a time
        if self.numberOfBits == 8:
            value = self.bitValue
            self.bitValue = 0
            self.numberOfBits = 0
            self.writeUByte(value)

    # ------------------------------------------------------------------

    def _finishBits(self):

        """
        helper method to make certain we complete a byte of bits before writing out non-bits or closing file
        :return:
        """

        if self.numberOfBits != 0:
            self.bitValue = self.bitValue << (8 - self.numberOfBits)
            self.numberOfBits = 0
            self.writeUByte(self.bitValue)
            self.bitValue = 0

    # ------------------------------------------------------------------

    def writeUByte(self, value: int):

        """

        :param value: unsigned byte to write out to the file
        :return: None
        """

        assert 0 <= value < 256

        self._finishBits()
        s = struct.pack('<B', value)
        self.outfile.write(s)

    # ------------------------------------------------------------------

    def writeUShort(self, value: int):

        """

        :param value: unsigned short to write to the file
        :return: None
        """

        assert 0 <= value < 65536

        self._finishBits()
        s = struct.pack('<H', value)
        self.outfile.write(s)

    # ------------------------------------------------------------------

    def writeUInt(self, value: int):

        """
        write an unsigned int to the file
        :param value: unsigned int to write to file
        :return: None
        """

        assert 0 <= value <= 2**32

        self._finishBits()
        s = struct.pack('<I', value)
        self.outfile.write(s)

    # ------------------------------------------------------------------

    def close(self):

        """
        close the file
        :return: None
        """

        self._finishBits()
        self.outfile.close()

    # ------------------------------------------------------------------
