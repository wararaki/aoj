import time
from datetime import date

#solve function
def solve(str_dates):
    dates = []
    for i in range(len(str_dates)):
        dates.append(int(str_dates[i]))

    date_start = date(dates[0], dates[1], dates[2])
    date_end = date(dates[3], dates[4], dates[5])

    return (date_end - date_start)


#main function
if __name__ == '__main__':
    while True:
        dates = input().split()

        if dates[0] == "-1":
            break

        date_diff = solve(dates)

        print(date_diff.days)
