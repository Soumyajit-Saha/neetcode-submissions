class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Suppose x is like 0101
        # Now if we want to make n nums whose bitwise and will result to x, we have to make sure all nums
        # will have to have same bits set as x.
        # So, basically we only allowed to make changes to the bits with 0 in x
        # So, we keep on filling the 0 bits from right with 01 then 10 the 11 and so on
        # If we keep on doing that we have to do it from 01 to binary of n - 1
        # So, we basically need to put bits from right in (n - 1) to 0 places of x
        # We keep two pointers to bit index of x and (n - 1) and taking bits from (n - 1) and putting it on pointer of x

        res = x
        i_x = 1 # Like a mask that masks the ith bit in x
        i_n = 1 # Like a mask that masks the ith bit in (n - 1)

        while i_n <= (n - 1): # if the ith mask shifts beyond left ost set bit of (n - 1)
            if x & i_x == 0: # index to fill in x
                if (n - 1) & i_n != 0: # If current bit of (n - 1) is set:
                    res = res | i_x
                i_x = i_x << 1
                i_n = i_n << 1  

            else:
                i_x = i_x << 1

        return res
