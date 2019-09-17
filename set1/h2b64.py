import base64

"""Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
"""


def h2b64(hex: bytearray) -> str:
    """Convert the given bytearray into a b64 string.

    Arguments:
        hex {bytearray} -- byte array input hex

    Returns:
        str -- base64 encoded bytes
    """

    return base64.b64encode(hex)

if __name__ == "__main__":
    my_bytes = bytearray.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    my_b64 = h2b64(my_bytes)

    print(f"Hex: {my_bytes}")
    print(f"Base64: {my_b64}")

    assert(my_b64 == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
