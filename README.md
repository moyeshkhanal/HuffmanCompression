# Huffman Compression To-Do List

Compressor
- Read from a text file, one character at a time (including whitespace(s))
- Create a dictionary of each character that appears, definition being the amount
- Make a tree out of the dictionary, based on the example from class
- Make a dictionary of each character, the definition being its binary representation
- Use this dictionary to convert the file into a new file in binary form
- Attach the table used to convert to the top of the new file

Decompressor
- Read new file, one bit at a time
- Use header table to convert these bits into characters
- Put characters in new new file
