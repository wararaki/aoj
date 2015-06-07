def main():
    n = int(input())

    for i in range(n):
        result = str(int(input()) + int(input()))

        if len(result) > 80:
            print("overflow")
        else:
            print(result)

if __name__ == '__main__':
    main()
