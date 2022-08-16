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
