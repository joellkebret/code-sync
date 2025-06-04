class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic_s= {}
        dic_t= {}
        
        for i in range(len(s)):
            if s[i] in dic_s:
                dic_s[s[i]] += 1
            else:
                dic_s[s[i]] = 1
            if t[i] in dic_t:
                dic_t[t[i]] += 1
            else:
                dic_t[t[i]] = 1

        for count in dic_t:
            if dic_t[count] != dic_s.get(count, 0):
                return False
        
        return True