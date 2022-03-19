# 158. Read N Characters Given read4 II - Call Multiple Times

'''
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
'''
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [""] * 4
        self.idx = 0
        self.bufLen = 0

    def read(self, buf: List[str], n: int) -> int:
        wcount = 0

        for i in range(n):
            if self.idx == 0:
                self.bufLen = read4(self.buf4)
                
            if self.bufLen == 0:
                break

            buf[i] = self.buf4[self.idx]
            wcount += 1
            self.idx = (self.idx + 1) % self.bufLen

        return wcount
