#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxLen = 0
        hashMap = dict()
        j = i
        while j < len(s):
            char = s[j]
            if char not in hashMap:
                hashMap[char] = j
            else:
                maxLen = max(maxLen, j - i)
                k = hashMap[char]
                for letter in s[i:k]:
                    hashMap.pop(letter)
                i = k + 1
                hashMap[char] = j
            j += 1
        maxLen = max(maxLen, j - i) # Edge case
        return maxLen
