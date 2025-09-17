#code for duplicate detection problem using sets

def hasDuplicate(self, nums):
        dup_map = set()
        for num in nums:
            if num in dup_map:
                return True
            dup_map.add(num)
        return False