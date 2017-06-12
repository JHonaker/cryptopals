# Challenge 4: Detect single-character XOR
#
# One of the 60-character strings in this file has been encrypted by a single-character XOR.
#
# Find it.

import codecs
import singlebytexor

if __name__ == "__main__":
    f = open("4.txt", "r")
    lines = f.readlines()
    f.close()

    lines = [line[:-1] if line[-1] == '\n' else line for line in lines] # strip the \n off the lines
    # for idx, line in enumerate(lines):
    #     print(idx)
    #     print(line)
    #     codecs.decode(line, 'hex')

    bytestrings = [codecs.decode(bt, 'hex') for bt in lines]
    plaintexts = [singlebytexor.cipher(bt) for bt in bytestrings]

    candidate = min(plaintexts, key = lambda x: x[2])
    line_number = plaintexts.index(candidate)

    print("Line number:", line_number)
    print(candidate)
