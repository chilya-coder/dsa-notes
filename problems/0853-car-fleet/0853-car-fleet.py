class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position = [3,5,7]
        # speed = [3,2,1]
        # target = 10
        # 10 - 3 = 7/3 -> 2.3h left
        # 10 - 5 = 5/2 -> 2.5h left
        # 10 - 7 = 3/1 -> 3h left

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        max_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > max_time:
                fleets += 1
                max_time = time 

        return fleets
