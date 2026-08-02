class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        x,y = 0, 0
        seen.add((x, y))
        for p in path:
            if p == 'W':
                x -= 1
            elif p == 'E':
                x  += 1
            elif p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            if (x,y) in seen:
                return True
            else:
                seen.add((x,y))
        print(seen)
        return False