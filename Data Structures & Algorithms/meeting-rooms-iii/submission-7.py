class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        count = [0] * n 

        for start, end in meetings:

            while used and used[0][0] <= start:
                _, room_number = heapq.heappop(used)
                heapq.heappush(available, room_number)
            if not available:
                meet_end, room = heapq.heappop(used)
                heapq.heappush(available, room)
                end = meet_end + (end - start)
            room_no = heapq.heappop(available)
            heapq.heappush(used, (end, room_no))
            count[room_no] += 1

        return count.index(max(count))