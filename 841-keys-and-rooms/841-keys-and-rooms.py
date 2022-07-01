class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = collections.deque()
        unique = set()
        q.append(0)
        while len(q) > 0 and len(unique) < len(rooms): 
            curr_index = q.popleft() 
            unique.add(curr_index)
            curr_arr = rooms[curr_index]
            for i in range(len(curr_arr)): 
                curr_elem = curr_arr[i]
                if curr_elem not in unique: 
                    q.append(curr_arr[i])

        return len(unique) == len(rooms)