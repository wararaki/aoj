def main():
    n = int(input())
    debt = 100000

    for i in range(n):
        tmp_debt = debt * 1.05
        debt = int(tmp_debt / 1000) * 1000

        if int(tmp_debt) > debt:
            debt += 1000

    print(debt)


if __name__ == '__main__':
    main()
