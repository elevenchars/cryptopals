import string
import collections

""" The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 
"""


def sbxor(a: bytearray, k: int) -> bytearray:
    """Calculate the single byte xor a ^ k

    Arguments:
        a {bytearray} -- Bytearray to be xor'd with
        k {int} -- single byte key to test

    Returns:
        bytearray -- a ^ k
    """
    assert(k < 0x100 and k >= 0x0), "k must be a single byte"

    n = bytearray(len(a))
    for i in range(len(a)):
        n[i] = a[i] ^ k
    return n


def ascii_freq(a: bytearray) -> float:
    """Return the frequency of valid ascii characters in a bytearray.

    Arguments:
        a {bytearray} -- Bytearray to test against

    Returns:
        float -- Frequency of valid ascii in a bytearray
    """
    total = len(a)

    ascii_chars = 0
    for i in range(total):
        if chr(a[i]) in string.ascii_letters:
            ascii_chars += 1
    return ascii_chars / total


def all_sbxor(a: bytearray) -> list:
    """Find all single byte xor bytearrays given an input

    Arguments:
        a {bytearray} -- Input bytearray

    Returns
        list -- List of all possible values of a ^ k, k is some byte
    """
    sols = []
    for i in range(0x100):
        sols.append(sbxor(a, i))
    return sols


def solve(a: bytearray) -> list:
    """Find the plaintext from the single-byte xor cipher.
    This is a very opinionated function, for some cases better to use
    all_sbxor and parse

    Arguments:
        a {bytearray} -- cipher

    Returns:
        list -- Most likely plaintexts
    """
    potential_solutions = all_sbxor(a)
    print(len(potential_solutions))

    # Remove unprintable plaintext candidates
    for s in potential_solutions[:]: # this iterates through a copy of the list
        for b in s:
            if chr(b) not in string.printable:
                potential_solutions.remove(s)
                break

    # Letter % > 80
    for s in potential_solutions[:]:
        if ascii_freq(s) < 0.75:
            potential_solutions.remove(s)

    # ETAOIN SHRDLU
    for s in potential_solutions[:]:
        c = collections.Counter(s.decode().lower())
        fq = c["e"] + c["t"] + c["a"] + c["o"] + c["i"] + c["n"]
        fq /= len(s)
        if fq < 0.3:
            potential_solutions.remove(s)

    print(len(potential_solutions))

    return potential_solutions

if __name__ == "__main__":
    my_bytes = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    sol = solve(my_bytes)

    print(f"Input ciphertext: {my_bytes}")
    print(f"Possible solutions:\n")
    for b in sol:
        print(b.decode())