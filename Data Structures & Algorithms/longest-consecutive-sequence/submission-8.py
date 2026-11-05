class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #loop through the sorted, set the counter to 0. set the counter to ` if the next element is 1 higher, then the next element is more than 1 breaking the sequence reset the counter to 0. make sure you return the proper latest counter.
        
         
        counter = 1
        max_length = 0
        seen_list=[]
        for num in nums:
            if num not in seen_list:
                seen_list.append(num)
            
        seen_list.sort()  

        if len(seen_list)==1:
            return 1

        for num in range(len(seen_list)-1):
            current_element = seen_list[num]
            next_element = seen_list[num+1]
            if current_element + 1 == next_element:
                counter += 1
            else:
                if counter>max_length:
                    max_length=counter
                counter = 1

            if num == (len(seen_list)-2) and counter>max_length:
                    max_length = counter

            

        return max_length

