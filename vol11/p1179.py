#solve function
def solve(dates):
    counter = 0;
    start_month = dates[1]
    start_day, end_day = dates[2], 0

    for year in range(dates[0], 1000):
        for month in range(start_month, 11):
            if year%3 == 0 or month%2 == 1:
                end_day = 21
            else:
                end_day = 20

            # count days
            counter += (end_day - start_day)

            start_day = 1
        else:
            start_month = 1

    return counter


#main function
if __name__ == '__main__':
    n = int(input())

    dates = [0 for i in range(3)]
    tmp_dates = []
    for i in range(n):
        tmp_dates = input().split()
        for j, tmp_date in enumerate(tmp_dates):
            dates[j] = int(tmp_date)

        date_count = solve(dates)
        print(date_count)
