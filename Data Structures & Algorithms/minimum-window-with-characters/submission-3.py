class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # count t is for what we need and how many in s (duplicates matter we need that amount)
        count_t = {}
        for c in t:
            count_t[c]=count_t.get(c,0) + 1
        
        #we have the window which we will dynamically add and reduce to suit and check conditions. have is 0 at start, need is however the count_t is. res, is set to a default -1,-1 will update with the values of the window left and right later, and res_len is at infinity because it needs to decrease and this number works the best for edge cases. 
        window = {}
        have = 0
        need = len(count_t)
        res = [-1,-1]
        res_len = float("infinity")
        left = 0

        # takes right pointer through s and make sures it assigned the values and adds the value of the right index to the window dictionary which has the count of what is in the window we casted. 
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

        #if that value of c which is the right pointer valye is checked is it in the countt and windows c == count t checks if you counted the exact amount of because the key is the value and both are dicts not arrays so they check what we assigned and we made it the number with the .get earlier so the number is the same? we make have += 1. bc have doesnt count distinct characters it counts how many of the full characters requirements have been accepted, thats the only way you have a valid window. 
            if c in count_t and window[c] == count_t[c]:
                    have += 1
            
        # this is the main engine of the problem, once we have a valid window themn it checks that from have == need which is how we now, then since he res len is infifinity it automatically runs it once againdt the window len, which and saved the indices and reslen to the new window len.
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)
            # saves the left pointer to the var name left char,  
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                left += 1
        
        left, right = res
        return s[left:right + 1] if res_len != float("infinity") else ""


