"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(subordinates):
            total = 0
            for s_id in subordinates:
                for emp in employees:
                    if emp.id == s_id:
                        total += emp.importance
                        total += dfs(emp.subordinates)
            return total

        Total = 0
        for emp in employees:
            if emp.id == id:
                Total += emp.importance
                Total += dfs(emp.subordinates)

        return Total