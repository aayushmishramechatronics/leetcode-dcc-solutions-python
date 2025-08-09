import heapq
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        count = [0] * n  
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        busy_rooms = []

        for start, end in meetings:
            duration = end - start
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
                count[room] += 1
            else:
                earliest_end, room = heapq.heappop(busy_rooms)
                new_end = earliest_end + duration
                heapq.heappush(busy_rooms, (new_end, room))
                count[room] += 1

        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
