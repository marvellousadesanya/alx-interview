#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Check if the most significant bit is 0
        if byte & 0x80 == 0:
            # This is a single-byte character
            if num_bytes != 0:
                return False
        else:
            # Check the number of bytes in the character
            if num_bytes == 0:
                # Calculate the number of bytes based on the first byte
                if byte & 0xE0 == 0xC0:
                    num_bytes = 2
                elif byte & 0xF0 == 0xE0:
                    num_bytes = 3
                elif byte & 0xF8 == 0xF0:
                    num_bytes = 4
                else:
                    return False
            else:
                # Check if the byte is a continuation byte
                if byte & 0xC0 != 0x80:
                    return False

                num_bytes -= 1

        # Check if all bytes of the character have been processed
        if num_bytes == 0:
            continue
        else:
            return False

    # Check if there are any remaining bytes
    return num_bytes == 0


if __name__ == '__main__':
    data = [197, 130, 1]  # Example data set

    if valid_utf8(data):
        print("Valid UTF-8 encoding")
    else:
        print("Invalid UTF-8 encoding")

