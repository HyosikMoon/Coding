# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1, s2):
        # # Solution 1 - Time Over, O(len(s1)*len(s2))
        # # Compare every s2 in s1 from each index.
        # length = len(s1)
        # for i, c in enumerate(s2):
        #     # Variable setting
        #     word = s2[i:i+length]
        #     dict1, dict2 = {}, {}

        #     # Make two dicts for compare s1 and the word in s2
        #     for char in s1:
        #         dict1[char] = dict1.get(char, 0) + 1
        #     for char in word:
        #         dict2[char] = dict2.get(char, 0) + 1
            
        #     # Compare two dicts
        #     if dict1 == dict2:
        #         return True
        
        # # There is no permuation in s2.
        # return False


        # # Solution 2 - Time Over, O(len(s1)*len(s2))
        # length = len(s1)
        # for i, c in enumerate(s2):
        #     word = s2[i:i+length]
        #     if sorted(s1) == sorted(word):
        #         return True
        # return False


        # Solution 3 - A little bit faster but still quite late
        # Compare every s2 in s1 from each index.
        length = len(s1)

        # Count s1 elements
        dict1 = {}
        for char in s1:
            dict1[char] = dict1.get(char,0) + 1

        # Count s2 elements and compare it with dict1
        for i, c in enumerate(s2):
            # Variable setting
            word = s2[i:i+length]
            dict2 = {}

            # Make two dicts for compare s1 and the word in s2
            for char in word:
                dict2[char] = dict2.get(char, 0) + 1
            
            # Compare two dicts
            if dict1 == dict2:
                return True

        # There is no permuation in s2.
        return False


        # # Solution 4 
        # A = [ord(x) - ord('a') for x in s1]
        # B = [ord(x) - ord('a') for x in s2]
        
        # target = [0] * 26
        # for x in A:
        #     target[x] += 1
        
        # window = [0] * 26
        # for i, x in enumerate(B):
        #     window[x] += 1
        #     if i >= len(A):
        #         window[B[i - len(A)]] -= 1
        #     if window == target:
        #         return True
        # return False


sol = Solution()
sol.checkInclusion('ab','eidbaooo')