# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.


class Solution:
    def intToRoman(self, num):
        # step1. 10^3 = ?, 10^2, 10^1, 10^0 => ?
        # step2. 7 symbols (1,5,10,15,100,500,1000)
        # step3. exception -> 4, 9, 40, 90, 400, 900
        # step4. How to combine them?

        