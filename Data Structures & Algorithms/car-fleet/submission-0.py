class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort lists by position
        paired = list(zip(position, speed))
        paired.sort(reverse=True)
        
        fleets = [] # time to destination
        for pair in paired:
            dest_time = (target - pair[0])/pair[1]

            if not fleets or fleets[-1] < dest_time:
                fleets.append(dest_time)

        return len(fleets)