"""
LC 1185. Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        leaps = 0
        
        for i in range(1971, year):
            if i % 4 == 0:
                if i % 100 == 0 and i % 400 != 0: # 1700, 1800, 1900 are non leap years. But 2000, 2400 are leap years
                    continue
                    
                leaps += 1
        
        y2d = (year - 1971 - leaps) * 365 + leaps * 366
        m2d =  months[month-1]
        
        if year % 4 == 0 and month > 2 and year % 100 != 0:
            m2d += 1
            
        d = (day + y2d + m2d + 4) % 7 # 1971.1.1 is a Friday
        
        return days[d]