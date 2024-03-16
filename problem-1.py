
class LRUCache(object):
    
    def __init__(self, capacity):
        self.cache = {}
        if isinstance(capacity, int) == False or capacity <= 0:
            self.capacity = 0
        else:
            self.capacity = capacity
        
    def get(self, key):
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return -1

    def set(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            del self.cache[list(self.cache)[0]]
        
our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

## Test Case 1
print("## Test Case 1")

print("our_cache.get(1) = ",our_cache.get(1)) 
print("our_cache.get(2) = ",our_cache.get(2)) 
print("our_cache.get(9) = ",our_cache.get(9)) 
our_cache.set(5, 5) 
our_cache.set(6, 6) 
print("our_cache.get(3) = ",our_cache.get(3)) 

## Test Case 2
print("## Test Case 2")

our_cache = LRUCache(0)
print("our_cache.get(1) = ",our_cache.get(1)) 
print("our_cache.get(2) = ",our_cache.get(2)) 
print("our_cache.get(3) = ",our_cache.get(3)) 
our_cache.set(4, 4) 
print("our_cache.get(4) = ",our_cache.get(4)) 

## Test Case 3
print("## Test Case 3")

our_cache = LRUCache(None)
print("our_cache.get(1) = ",our_cache.get(1)) 
print("our_cache.get(2) = ",our_cache.get(2)) 
print("our_cache.get(3) = ",our_cache.get(3)) 
our_cache.set(4, 4) 
print("our_cache.get(4) = ",our_cache.get(4)) 