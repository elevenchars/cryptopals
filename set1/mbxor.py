"""Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""

def mbxor(msg: bytearray, key: bytearray) -> bytearray:
    """Encrypt a message using the repeating key xor.
    
    Arguments:
        msg {bytearray} -- Message to be encrypted
        key {bytearray} -- Key to be used
    
    Returns:
        bytearray -- Ciphertext of msg ^ key, length of longer msg
    """
    cipher = bytearray(len(msg))
    for i in range(len(msg)):
        cipher[i] = msg[i] ^ key[i % len(key)]
    return cipher

if __name__ == "__main__":
    plain = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    plain = bytearray(plain.encode())
    my_key = bytearray("ICE".encode())
    cipher = mbxor(plain, my_key)
    print(f"Plaintext: {plain}")
    print(f"Key: {my_key}")
    print(f"Ciphertext: {cipher}")

    assert(cipher.hex() == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
