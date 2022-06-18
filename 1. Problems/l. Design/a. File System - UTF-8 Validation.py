# LC 393. UTF-8 Validation

'''
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.
'''
class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def getBin(d):
            binStr = bin(d)[2:]

            return "0" * (8 - len(binStr)) + binStr

        def getByteLength(b):
            count = 0

            for byte in b:
                if byte == "1":
                    count += 1
                else:
                    break

            return count

        counter = 0

        for d in data:
            if counter:
                if getBin(d)[:2] != "10":
                    return False

            else:
                if getBin(d)[0] == "0":
                    continue
                else:
                    counter = getByteLength(getBin(d))

                    if counter == 1 or counter > 4:
                        return False

            counter -= 1

        return counter == 0
