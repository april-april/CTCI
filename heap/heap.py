import heapq

heapList = [6, 2, 3, 4, 5, 10, 20]
heapq.heapify(heapList)

print heapList

heapq._heapify_max(heapList)
print heapList

heapq.heapreplace(heaplist, 15)
print heapList