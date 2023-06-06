# The Supermarket Queue
"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers and an integer
    the array can be empty or null
    integer values will be greater than or equal to 0
"""
# Return:
"""
    an integer representing the total queue time for all elements in the array to pass the integer queue
"""
# Examples:
"""
    [5,3,4], 1 => 12
    [10,2,3,3], 2 => 10
    [2,3,10], 2 => 12
    [], 1 => 0
    [5], 1 => 5
    [2], 5 => 2
    [1,2,3,4,5], 1 => 15
    [1,2,3,4,5], 100 => 5
    [2,2,3,3,4,4], 2 => 9
"""
# Pseudocode:
"""
    # create an n array of elements of integer 0
    # iterate through the input array
    # at each iteration sort result 
    # add the current element of the input array to the resorted result element at index 0
    # return the highest element from result
"""

# my answer
def queue_time(arr, n):
    # create an n array of elements of integer 0 
    result = [0] * n
    # iterate through the input array
    for i in arr:
        # at each iteration sort result
        result.sort()
        # add the current element of the input array to the resorted result element at index 0
        result[0] += i
    # return the highest element from result
    return max(result)

print(queue_time([], 1)) # 0
print(queue_time([5], 1)) # 5
print(queue_time([2], 5)) # 2
print(queue_time([1,2,3,4,5], 1)) # 15
print(queue_time([1,2,3,4,5], 100)) # 5
print(queue_time([2,2,3,3,4,4], 2)) # 9

# best practices and most clever
# using index and min instead of sorting each time and adding to index 0
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

# importing heapq to use heapreplace(heap, item)
import heapq

def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)

# same as my idea sorting every iteration inside a for loop
def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)

# here they are using min for index instead of re sorting per each iteration
def queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        indexMin = tills.index(min(tills))
        tills[indexMin] += i
    return max(tills)

# they built an entire class object wow
class MarketQueue():
    
    def __init__(self,customers,n):
        self.customers = customers
        self.n=n
        self.timer = 0
        self.active_checkouts = []
        
    def calculate_total_time(self):
        while self.customers:
            self.process_queue()   
        return self.timer

    def process_queue(self):
        if len(self.active_checkouts) < self.n:
            queue_index = self.n - len(self.active_checkouts)
            self.active_checkouts.extend(self.customers[:queue_index])
            self.customers[:queue_index] = []
        while self.active_checkouts and (len(self.active_checkouts) == self.n or not self.customers) :
            self.timer += 1
            self.process_active_checkouts()
    
    def process_active_checkouts(self):
        finished_customers = []
        for index,customer in enumerate(self.active_checkouts):
            if customer > 1:
                self.active_checkouts[index] = int(customer-1)
            else:
                finished_customers.append(customer)
        
        for finished in finished_customers:
            self.active_checkouts.remove(finished)

# implementing requirements
def queue_time(customers,n):
    return MarketQueue(customers,n).calculate_total_time()

# while loop and array copies
def queue_time(customers, n):
    time = 0
    while len(customers[:])>0:
      time=time+1
      customers[:n]=[x-1 for x in customers[:n]]
      customers=[y for y in customers if y !=0]
    return time

# while loop with sort() and pop()
def queue_time(customers, n):
    buckets = [0 for i in range(0, n)]
    while customers:
        buckets.sort()
        buckets[0] += customers.pop(0)
    return max(buckets)