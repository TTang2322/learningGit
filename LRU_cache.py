# class DLinkedNode():
#     def __init__(self,key=None, value=None):
#         self.key = 0 if key is None else key
#         self.value = 0 if value is None else value
#         self.pre = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
        
#         self.cache = dict()
#         self.size = 0
#         self.capacity = capacity
        
#         self.head, self.tail = DLinkedNode(), DLinkedNode()
        
#         self.head.next = self.tail
#         self.tail.pre = self.head
    
#     def remove(self,node):
#         node.pre.next = self.tail
#         self.tail.pre = node.pre
            
#     def add(self,node):
#         self.head.next = node
#         node.pre = self.head
        
#         node.next = self.tail
#         self.tail.pre = node
        
#     def get(self, key: int) -> int:
        
#         print(self.cache.keys())
        
#         get_node = self.cache.get(key)
#         if not get_node:
#             return -1
#         else:
#             self.remove(get_node)
#             self.add(get_node)
#             return get_node.value

#     def put(self, key: int, value: int) -> None:
        
#         print(self.cache.keys())
        
#         node = self.cache.get(key)
#         if not node:
#             new_node = DLinkedNode(key,value)
#             self.cache[key] = new_node
#             self.size += 1
#             if self.size > self.capacity:
#                 self.remove(self.tail.pre)
#                 print('No 55  {}'.format(self.tail.pre.key))
#                 del self.cache[self.tail.pre.key]
#                 self.size -= 1
#                 self.add(new_node)
                
#             else:
#                 self.add(new_node)
#         # else:
#         #     self.remove(new_node)
#         #     self.add(new_node)
                

from collections import OrderedDict

class LRUCache(object):
    dic = []
    cap = 0
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.pop(key)
        self.dic[key] = value
        if len(self.dic) > self.cap:
            self.dic.popitem(last=False)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)