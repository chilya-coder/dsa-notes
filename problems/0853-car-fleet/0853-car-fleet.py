class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       # (0,1; 3,3; 5,1; 8,1; 10,2)
       #  12     3    7    4     1
       #
       # 1. Sort input array desc by position and speed
       # 2. If current time > max_time - it forms a fleet.


        cars_sorted = sorted(zip(position, speed), reverse = True)
        max_time = 0
        fleets = 0
        for pos, speed in cars_sorted:
            time = (target - pos)/speed
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets