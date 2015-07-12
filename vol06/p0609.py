# solve problem
def solve(n, m, targets, games):
    counter = [0 for i in range(n+1)]

    for i in range(m):
        for j in range(n):
            if games[i][j] == targets[i]:
                counter[j+1] += 1
            else:
                counter[targets[i]] += 1

    return counter


# main function
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    tmp_targets = input().split()

    targets = []
    for i in range(m):
        targets.append(int(tmp_targets[i]))

    games = [[0 for i in range(n)] for j in range(m)]
    tmp_games = []
    for i in range(m):
        tmp_games = input().split()
        for j in range(n):
            games[i][j] = int(tmp_games[j])

    results = solve(n, m, targets, games)
    for i in range(1, n+1, 1):
        print(results[i])
