class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        index = 0
        for house in houses:
            while index < len(heaters) - 1 and abs(heaters[index] - house) >= abs(heaters[index + 1] - house):
                index += 1
            distance = abs(heaters[index] - house)
            radius = max(radius, distance)
        return radius

        