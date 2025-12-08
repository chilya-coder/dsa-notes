class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tankLvl = 0
        start = 0
        total = 0
        for i, x in enumerate(gas):
            diff = gas[i] - cost[i]
            tankLvl += diff
            total += diff

            if tankLvl < 0:
                start = i + 1
                tankLvl = 0

        if total < 0:
            return -1
        
        return start






