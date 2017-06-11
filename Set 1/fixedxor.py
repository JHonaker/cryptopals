import codecs

def xor(in1, in2):
    assert len(in1) == len(in2)

    return bytes([left ^ right for left, right in zip(in1, in2)])



if __name__ == "__main__":
    input1 = codecs.decode(b"1c0111001f010100061a024b53535009181c", "hex")
    input2 = codecs.decode(b"686974207468652062756c6c277320657965", "hex")
    xor_result = codecs.decode(b"746865206b696420646f6e277420706c6179", "hex")

    test = xor(input1, input2)

    print(test)

    assert test == xor_result
