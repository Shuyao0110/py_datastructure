print('helloworld')
class Cookie:
    def __init__(self,color) :
        self.color=color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color=color

cokie1=Cookie('green')
print(cokie1.get_color())
cokie1.set_color('red')
print(cokie1.get_color())

class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None

class LinkedList:
    # init是class的而不是function
    # value用来放第一个node
    def __init__(self,value) :
        new_node=Node(value) 
        self.head=new_node
        self.tail=new_node 
        self.length=1
    def append(self,value):
        new_node=Node(value)
        # 先判断链表是否为空，如果是空的就把头和尾都指向新node
        if self.head is None:
            self.tail=new_node
            self.tail.next=new_node
            self.head=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node 
        self.length+=1
    def pop(self):
        if self.head is None:
            print('linked list is empty')
        elif self.length==1:
            print(self.tail)
            self.head=None
            self.tail=None
            self.length==0
        else: 
            print(self.tail.value)
            pre=self.head
            temp=self.head
            while(temp.next):
            # while temp.next is not None:
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
# 相当于我们只知道头和尾
# 简单数据类型“=”是直接赋值
# 复杂数据类型（字典）“=”是pointer
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def pop_first(self):
        if self.length==0:
            return None
        elif self.length==1:
            print(self.head.value)
            self.head=None
            self.tail=None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length-=1
            return temp
    def get(self,index):
        if index<0 or index>self.length-1:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return temp.value
        else: return False
    def insert(self,index,value):
        new_node=Node(value)
        temp=self.get(index)
        if index==0:
            return self.prepend(value)
        else:
            pre=self.get(index-1)
            if temp and pre:
                pre.next=new_node
                new_node.next=temp
                self.length+=1
            else: return False
    def remove(self,index):
        if index<0 or index>self.length-1:
            return None
        elif index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            pre=self.get(index-1)
            temp=self.get(index)
            pre.next=temp.next
            temp.next=None
            self.length-=1
            return temp.value
    def reverse(self):
        temp=self.head
        before=None
        after=temp.next
        self.head=self.tail
        self.tail=temp
        for _ in range(self.length):
            temp.next=before
            before=temp
            temp=after
            after=after.next
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


# 如果是在原链表基础上进行操作，返回boolean表示是否成功
#返回元素，则用none
    
my_linked_lisk=LinkedList(4)
my_linked_lisk.append(3)
# my_linked_lisk.print_list()
#my_linked_lisk.pop()
my_linked_lisk.prepend(5)
#my_linked_lisk.print_list()
#my_linked_lisk.pop_first()
print(my_linked_lisk.get(0))
print(my_linked_lisk.set_value(0,1))
my_linked_lisk.print_list()


class DoubleNode:
    def __init__(self,value) :
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node=DoubleNode(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=DoubleNode(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            temp.prev=None
        self.length-=1
        return temp

    def prepend(self,value):
        new_node=DoubleNode(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp

    def get(self,index):
        if index<0 or index>self.length-1:
            return None
        if index<self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
            return temp

    def set_value(self,index,value):
        temp=self.get(index)
        if temp :
            temp.value=value
            return True
        else: return False

    def insert(self,index,value):
        if index<0 or index>self.length-1:
            return False
        if index==0:
            self.prepend(value)
        elif index==self.length-1:
            self.append(value)
        else:
            new_node=DoubleNode(value)
            temp=self.get(index)
            new_node.prev=temp.prev
            new_node.next=temp
            temp.prev.next=new_node
            temp.prev=new_node
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>self.length-1:
            return False
        if index==0:
            self.pop_first()
        elif index==self.length-1:
            self.pop()
        else:
            temp=self.get(index)
            temp.next.prev=temp.prev
            temp.prev.next=temp.next
            temp.prev=None
            temp.next=None
        self.length-=1
        return True

    def print_list(self):
        temp=self.head
        while (temp):
            print(temp.value)
            temp=temp.next

my_doubly_linked_list=DoublyLinkedList(5)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
print(my_doubly_linked_list.pop_first().value)
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()


 
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return True
    
    def pop(self):
        if self.height==0:
            return None
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
            self.length-=1
            return temp

    def print_stack(self):
        temp=self.top
        while temp:
            print(temp.value)
            temp=temp.next

    

my_stack=Stack(4)
my_stack.print_stack()


class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.last is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return True

    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=temp.next
            temp.next=None
        self.length-=1
        return temp

    def print(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next

my_queue=Queue(8)
my_queue.print()

class treeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=treeNode(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            elif new_node.value==temp.value:
                return False
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def contains(self,value):
        if self.root is None:
            return False
        temp=self.root
        while temp:
            if temp.value>value:
                temp=temp.left
            elif temp.value<value:
                temp=temp.right
            else:
                return True
        return False

    def BFS(self):
        current_node=self.root
        queue=[]
        results=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_pre_order(self):
        results=[]
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def DFS_post_order(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node)
        traverse(self.root)
        return results

    def DFS_in_order(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


my_binary_tree=BinarySearchTree()
my_binary_tree.insert(45)
my_binary_tree.insert(87)
my_binary_tree.insert(39)
print(my_binary_tree.root.value)
print(my_binary_tree.root.left.value)
print(my_binary_tree.root.right.value)
print(my_binary_tree.contains(3))
print(my_binary_tree.BFS())
print(my_binary_tree.DFS_pre_order())


class HashTable:
    def __init__(self,size=7) :
        self.data_map=[None] * size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)%len(self.data_map)
        return my_hash

    def set_item(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
            # 在空位里初始化一个数组
        self.data_map[index].append([key,value])
    
    def get_item(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def item_in_commom(list1,list2):
        my_dict={}
        for i in list1:
            my_dict[i]=True
        for j in list2:
            if j in my_dict:
                return True
        return False

    def print_table(self):
        # enumerate函数內是一个可迭代对象，返回索引和元素
        for i, val in enumerate(self.data_map):
            print(i,":", val)

my_hash_table=HashTable()
my_hash_table.set_item('bolts',1400)
my_hash_table.set_item('washers',50)
my_hash_table.set_item('lumber',70)
my_hash_table.print_table()
print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.keys())


class Graph:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
    
    def add_edge(self, v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])

    

my_graph=Graph()
my_graph.add_vertex('A')
my_graph.print()



