class Solution:
    def minSetSize(self, arr):

        freq_dict = {}
        for num in arr:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        counter = sorted(freq_dict.values(), reverse=True)
        
        removed, count, half_size = 0, 0, len(arr) // 2
        
        for freq in counter:
            removed += freq
            count += 1
            if removed >= half_size:
                return count
        
        return count 
