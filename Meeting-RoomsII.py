class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Store rooms and ending times of meetings in priority queue
        pq = []

        # Sort meeting time intervals in order of the starting times
        intervals.sort(key = lambda x: x[0])


        for i in intervals:
            if len(pq) == 0:
                heapq.heappush(pq, i[1])
                continue
            # if room at the top of the pq is empty
            if pq[0] <= i[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, i[1])   
        
        return len(pq)



