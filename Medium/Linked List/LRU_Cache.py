"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, key, val): # each node is going to have a key value pair
        self.key, self.val = key, val
        self.prev = self.next = None #setting prev and next values to None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # creating the hashmap, will map the key to node
        
# left = LRU (Least Recently Used), right = most recently used

        self.left, self.right = Node(0, 0), Node(0, 0) # dummy pointers telling us the most recent and least recent values we just added 

        self.left.next, self.right.prev = self.right, self.left # connecting the nodes. If we want to put a new node then we place it in the middle, between the left and the right pointers

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev # node is now no longer between prev and next
    
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node # point both at node
        node.next, node.prev = nxt, prev
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # tells us the node; each key is mapped to a node
        return -1
        

    def put(self, key, value):
        if key in self.cache: # if we have a key thats already in our cache, that means that a node already exists in that list with the same key value
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # hashmap now has a pointer to this node
        self.insert(self.cache[key]) # pass that node into our insert function

        # compare the length of the cache to the capacity
        if len(self.cache) > self.cap:
            #remove from the list and delete the LRU from the cache (hashmap)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
