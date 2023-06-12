class FirstUnique(object):
    # 哈希表加linked list
    def __init__(self,nums):
        """
        :type nums: List[int]
        """
        self.dummy = ListNode(0)
        self.tail=self.dummy
        # 数据值=>数据节点的前一个节点
        self.num_to_prev = {}
        # 存放出现过的数字(>=2)
        self.duplicates = set()
        for num in nums:
            self.add(num)

        
        

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if not self.dummy.next:
            return -1
        return self.dummy.next.val
 
    def add(self, num):
        """
        :type value: int
        :rtype: None
        """
        if num in self.duplicates:
            return
        # 这个数字没出现过，是全新的
        if num not in self.num_to_prev:
            self.add_to_tail(num)
            return
        # 出现过一次，又出现了第二次，加入duplicates，从num_to_prev中删除
        self.remove(num)
        self.duplicates.add(num)
    
    def remove(self,num):
        # 通过num_to_prev 找到当前节点
        prev=self.num_to_prev.get(num) 
        prev.next=prev.next.next
        # 把num的映射关系从map中删除
        del self.num_to_prev[num]
        if prev.next:
            self.num_to_prev[prev.next.val] = prev 
        else:
            self.tail = prev
    
    def add_to_tail(self,num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail=self.tail.next

my_solution=FirstUnique([2,3,5])
my_solution.showFirstUnique([])


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

def firstUniqueNumber(self,nums,number):
    if not nums:
        return -1
    # 一个分类计数的dict，记录num出现的次数
    counter={}
    # 遍历一轮，用来记录，默认值为0
    for num in nums:
        counter[num] = counter.get(num,0) +1
        if num == number:
            break
            # 没有break的话触发else
    else:
        return -1
    
    for num in nums:
        if counter[num] ==1:
            return num
        if num ==number:
            break
    return -1

# 现实应用：抽奖，点名系统
import random
class RandomizedSet(object):

    def __init__(self):
        self.nums=[]
        self.valToIndexDict={}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.valToIndexDict:
            return False
        self.nums.append(val)
        # 用一个字典存放val在list中的位置索引
        self.valToIndexDict[val] = len(self.nums) - 1
        return True

    # O(1)
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # 增删：list的最后一个值： O(1)
        # 增删：list中间的值： O(1)
        # 改查：中间和末尾都是：O(1)
        if val not in self.valToIndexDict:
            return False
        deleted_index=self.valToIndexDict[val]
        if deleted_index < len(self.nums) - 1:
            last_num = self.nums[-1]
            self.nums[deleted_index] = last_num
            self.valToIndexDict[last_num] = deleted_index
        del self.valToIndexDict[val]
        self.nums.pop()
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        # 涉及随机就要使用index，使用index就要用list
        return self.nums[random.randint(0,len(self.nums)-1)]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# 缓存淘汰策略
# Cache Eviction Strategy
# Cache Replacement Policy

# 146. LRU Cache
class LinkedNode:
    def __init__(self,key=None,value=None,next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.key_to_prev = {}
    
    # 把新节点推入链表的尾部，并将其值写入映射表
    def push_back(self,node):
        self.key_to_prev[node.key]=self.tail
        self.tail.next=node
        self.tail=node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """ 
        if key not in self.key_to_prev:
            return -1
        # 刚刚被访问过的节点需要移动到链表的尾部
        self.kick(key)
        return self.tail.value

    # 加新节点
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_prev:
            self.kick(key)
            self.tail.value = value
            return
        self.push_back(LinkedNode(key,value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
    
    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    #  将目标节点从原来位置移除，并连接到尾部
    def kick(self,key):
        # 根据映射表找到前一个节点和目标节点
        prev = self.key_to_prev[key]
        key_node=prev.next
        if key_node == self.tail:
            return
        prev.next = key_node.next
        self.key_to_prev[key_node.next.key] = prev
        key_node.next = None
        self.push_back(key_node)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 有序字典：OrderDdict
# 类似数组的字典，保留键值对的顺序
from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in cache:
            return -1
        # 把被访问的键值对取出，再放回cache的末尾
        value = self.cache.pop(key)
        self.cache[key]=value
        return value
    
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # last = True时pop规则是FILO, last = False时FIFO
            self.cache.popitem(last=False)