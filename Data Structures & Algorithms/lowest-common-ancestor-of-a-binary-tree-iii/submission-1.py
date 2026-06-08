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

        # Get depth of p
        par = p
        depthp = 0
       
        while par:
            depthp += 1
            par = par.parent

        # If one node is in greater depth than other, bring it to same level
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

        # After both are at same level, search for its parent
        while parq != parp:
            parq = parq.parent
            parp = parp.parent
        
        return parq


