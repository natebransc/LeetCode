class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        if len(xs) % 2 == 0:
            return xs[::1] == xs[::-1]
        else:
            middle = int(len(xs) / 2)
            return xs[:middle:1] == xs[:middle:-1]
