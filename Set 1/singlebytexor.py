# Challenge 3: Single-byte XOR cipher

# The hex encoded string:
#     1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# has been XOR'd against a single character. Find the key, decrypt the message.
#
# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext.
# Character frequency is a good metric.
# Evaluate each output and choose the one with the best score.

import codecs
from fixedxor import xor

# Spaces are slightly more frequenct than E, and digits/punctuation between T and A
ENG_FREQ = {
    "E": 12.02,
    "T": 9.10,
    "A": 8.12,
    "O": 7.68,
    "I": 7.31,
    "N": 6.95,
    "S": 6.28,
    "R": 6.02,
    "H": 5.92,
    "D": 4.32,
    "L": 3.98,
    "U": 2.88,
    "C": 2.71,
    "M": 2.61,
    "F": 2.30,
    "Y": 2.11,
    "W": 2.09,
    "G": 2.03,
    "P": 1.82,
    "B": 1.49,
    "V": 1.11,
    "K": 0.69,
    "X": 0.17,
    "Q": 0.11,
    "J": 0.10,
    "Z": 0.07
}

def character_frequency(inputstr):
    freq = {letter: 0 for letter in range(256)}
    for byte in inputstr:
        freq[int(byte)] += 1

    return freq

def single_byte_xor(inputbytes, xorbyte):
    xorarray = bytes([xorbyte] * len(inputbytes))
    return xor(inputbytes, xorarray)

def score_str(inputstr):
    """
    Score is based off of letter frequency (including spaces).
    The cost function is just squared error loss from the expected distribution of letters.
    """
    nbytes = len(inputstr)
    char_freq = character_frequency(inputstr)
    sq_err = 0.0
    for code, freq in char_freq.items():
        if ord('a') <= code <= ord('z'):
            continue
        elif ord('A') <= code <= ord('Z'):
            lower = code - (ord('A') - ord('a'))
            sq_err += ((char_freq[lower] + freq) / nbytes - ENG_FREQ[chr(code)]) ** 2
        elif ord(' ') == code:
            sq_err += (char_freq[code] / nbytes - 13) ** 2
        else:
            sq_err += (char_freq[code] / nbytes) ** 2

    return sq_err

def cipher(inputstr):
    xor_results = [single_byte_xor(inputstr, letter) for letter in range(256)]
    scores = [score_str(xorstr) for xorstr in xor_results]
    min_index = scores.index(min(scores))
    min_code = range(256)[min_index]

    return (min_code, chr(min_code), xor_results[min_index])





if __name__ == "__main__":
    testhex = codecs.decode(b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 'hex')

    print(cipher(testhex))
