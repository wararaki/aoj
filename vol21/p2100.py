# solve
def solve(n, block):
    max_up = 0
    max_down = 0
    for i in range(n-1):
        if block[i] < block[i+1]:
            max_up = max(max_up, block[i+1]-block[i])
        elif block[i] > block[i+1]:
            max_down = max(max_down, block[i]-block[i+1])

    return (max_up, max_down)

# main function
if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        tmp_block = input().split()

        block = []
        for j in range(n):
            block.append(int(tmp_block[j]))

        max_up, max_down = solve(n, block)
        print(max_up, max_down)
