class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maxLen = int(sqrt(len(s))+1)
        sLen = len(s)
        # print("sLen", sLen)
        if sLen == 1:
            return False
        if sLen == 2 and s[0] != s[1]:
            return False
        for length in range(1, maxLen+1):
            # print("====length====", length)
            if sLen % length == 0:
                times = sLen / length
                flag = True
                for i in range(times):
                    # print("range1", length*i, length*(i+1))
                    if s[0:length] != s[length*i:length*(i+1)]:
                        flag = False
                        break
                if flag:
                    return True
                # print("===second===")
                if length == 1:
                    continue
                flag = True
                for i in range(length):
                    # print("range2", times*i, times*(i+1))
                    if s[0:times] != s[times*i:times*(i+1)]:
                        flag = False
                        break
                if flag:
                    return True
        return False