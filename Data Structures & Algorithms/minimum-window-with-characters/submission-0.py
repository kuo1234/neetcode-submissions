class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = {}

        for char in t:
            t_count[char] = t_count.get(char,0)+1
        
        l,r = 0,0
        formed =  0
        required = len(t_count)

        window_count = {}
        min_len = float('inf')
        result = ""

        while r< len(s):
            char = s[r]
            window_count[char] = window_count.get(char,0)+1

            if char in t_count and window_count[char] == t_count[char]:
                formed +=1
            while l<=r and formed == required:
                char = s[l]

                current_len = r-l+1
                if current_len < min_len:
                    result = s[l:r+1]
                    min_len  = current_len
                
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -=1
                
                l+=1
            r+=1

        return result
