class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stk = [0]
        while stk:
            room  = stk.pop()
            if room not in visited:
                visited.add(room)

                for i in rooms[room]:
                    if i not in visited:
                        stk.append(i)
        return len(visited) == len(rooms)

        


  