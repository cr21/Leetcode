"""

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.



Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61



"""


class Solution(object):
    def checkYear(self, year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """

        no_of_days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        date_arr = date.split("-")
        d = int(date_arr[2])
        m = int(date_arr[1])
        y = int(date_arr[0])
        # print(self.checkYear(2004))
        no_of_days = 0
        for i in range(0, m - 1):
            if i == 1 and self.checkYear(y):
                no_of_days += 29
            else:
                no_of_days += no_of_days_month[i]
        no_of_days += d

        return no_of_days