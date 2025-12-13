from typing import List
import re

class Solution:
    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool]
    ) -> List[str]:
        
        # Business line priority order
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        order_index = {b: i for i, b in enumerate(order)}
        
        valid = []
        
        for c, b, active in zip(code, businessLine, isActive):
            # Must be active
            if not active:
                continue
            
            # Business line must be valid
            if b not in order_index:
                continue
            
            # Code must be non-empty and contain only alphanumeric characters or underscore
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue
            
            valid.append((order_index[b], c))
        
        # Sort by business line order, then by code lexicographically
        valid.sort()
        
        # Return only the coupon codes
        return [c for _, c in valid]
