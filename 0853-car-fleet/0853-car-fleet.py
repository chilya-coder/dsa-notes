class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = []

        for position, speed in cars:
            time_left = (target - position) / speed
            if not fleets:
                fleets.append(time_left)
            else:
                if fleets[-1] < time_left: # it means our last car time is actually more than current, so we have fleet
                    fleets.append(time_left)
        return len(fleets)
        