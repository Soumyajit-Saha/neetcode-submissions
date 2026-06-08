"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Iteration 1

        # get depth of q
        par = q
        depthq = 0
       
        while par:
            depthq += 1
            par = par.parent

        par = p
        depthp = 0
       
        while par:
            depthp += 1
            par = par.parent

        parq = q
        parp = p
        if depthq > depthp:
            while depthq != depthp:
                depthq -= 1
                parq = parq.parent

        else:
            while depthq != depthp:
                depthp -= 1
                parp = parp.parent

        while parq != parp:
            parq = parq.parent
            parp = parp.parent
        
        return parq


