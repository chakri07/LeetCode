class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        if the canditate == target then return true 
        it will always be the same lenth 
        2 ** (n-1) options unnayi.
        if at any point if one of the number is in the triplet > traget[idx]
        remove
        then atleast one idx lo target == max ledhu anuko 

        with n elements ., 
        '''
        cleaned_triplets = []

        max_arr = [0,0,0]

        for i,j,k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            elif i == target[0] or j == target[1] or k == target[2]:
                cleaned_triplets.append([i,j,k])

        if len(cleaned_triplets) == 0:
            return False
        
        found = {}

        for i,j,k in cleaned_triplets:
            if i == target[0]:
                found[0] = True
            
            if j == target[1]:
                found[1] = True

            if k == target[2]:
                found[2] = True

        return len(found) == 3 
            


        







    