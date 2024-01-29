#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only
    need to handle the 8 least significant bits of each integer
    """
    # Variable for counting number of bytes in UTF-8 Character
    bytes_to_follow = 0

    # Masks for checking if byte is valid (Starts with 10)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:

        mask_n_byte = 1 << 7

        if bytes_to_follow == 0:
            # Count number of bytes the UTF-8 Character will have
            while mask_n_byte & byte:
                bytes_to_follow += 1
                mask_n_byte = mask_n_byte >> 1

            # If number of bytes did not increase then it has 1 byte
            # which is the same we are counting so no need to check next bytes
            # for current character
            if bytes_to_follow == 0:
                continue

            # A character in UTF-8 can be 1 to 4 bytes long
            # But 1 byte characters start in 0 so bytes_to_follow should never
            # be 1
            if bytes_to_follow == 1 or bytes_to_follow > 4:
                return False

        else:
            # Every byte that is not the first byte of a character should start
            # with 10, otherwise is not valid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # If bytes of character are valid, then the count will decrease with
        # each byte until a new character starts
        bytes_to_follow -= 1

    # All characters were verified correctly with their proper byte count
    if bytes_to_follow == 0:
        return True

    return False

