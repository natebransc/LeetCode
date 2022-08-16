# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        xs = str(x)
        # check if negative
        if xs[0] != "-":
            xsr = xs[::-1]
            if int(xsr) < 2147483648:
                return int(xsr)
            else:
                return 0
        else:
            xsr = xs[:0:-1]
            if -1 * int(xsr) >= -2147483648:
                return -1 * int(xsr)
            else:
                return 0
