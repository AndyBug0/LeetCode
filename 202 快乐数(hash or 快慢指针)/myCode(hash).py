class Solution:
    def isHappy(self, n: int) -> bool:
        a = [i * i for i in range(10)]
        b = set([])
        s = 0
        count = 0
        while n != 1:
            if n in b:
                return False
            b.add(n)
            count += 1
            while n > 0:
                s += a[n%10]
                n = int(n / 10)
            n = s
            s = 0
        return True