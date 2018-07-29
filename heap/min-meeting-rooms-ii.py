class Solution(object):
    
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # sort the intervals by start time
        intervals.sort(key=lambda x:x.start) 
        # stores the END time of intervals in a heap
        heap = []
        # loop through the intervals
        for i in intervals:
            # if start time of current interval is GREATER than the 
            # LOWEST end time, then you can reuse the room.
            if heap and i.start >= heap[0]: 
                # this means two intervals can use the same room
                # heapreplace pops the lowest element in the minheap and inserts an element
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated because start time
                # is less than lowest end time, so it overlaps
                heapq.heappush(heap, i.end)
                
        #this returns the number of rooms left in heap      
        return len(heap)