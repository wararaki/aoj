
# compare function
def comp(items):
    return (items[0]**2 + items[1]**2 == items[2]**2)


# main function
def main():
    n = int(input())

    items = [0] * 3
    for tm in range(n):
        str = (input()).split()
        for i in range(3):
            items[i] = int(str[i])

        items.sort()

        if(comp(items)):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
