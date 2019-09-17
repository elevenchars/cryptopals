"""Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179
"""


def fixed_xor(a: bytearray, b: bytearray) -> bytearray:
    """Returns the xor of two equal length bytearrays.
    
    Arguments:
        a {bytearray} -- Bytearray to be used
        b {bytearray} -- Bytearray to be used
    
    Returns:
        bytearray -- a ^ b
    """
    
    assert(len(a) == len(b)), "Bytearrays are not the same length"

    result = bytearray(len(a))

    for i in range(len(a)):
        result[i] = a[i] ^ b[i]

    return result

if __name__ == "__main__":
    my_a = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
    my_b = bytearray.fromhex("686974207468652062756c6c277320657965")

    my_result = fixed_xor(my_a, my_b)

    print(f"Bytearray a: {my_a}")
    print(f"Bytearray b: {my_b}")
    print(f"a ^ b: {my_result}")
    assert(my_result == bytearray.fromhex("746865206b696420646f6e277420706c6179"))