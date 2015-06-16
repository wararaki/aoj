# directions
x_dir = [0, 1, 0, -1]
y_dir = [1, 0, -1, 0]

# map info
visited = []
maps = []

# bfs algorithm
def bfs(h, w, cheese, sx, sy, moves):
    que = [(moves, sx, sy)]

    for i in range(h):
        for j in range(w):
            visited[i][j] = (maps[i][j] != 'X')

    visited[sy][sx] = False

    while len(que) > 0:
        c_moves, c_x, c_y = que.pop(0)
        if maps[c_y][c_x] == cheese:
            return (c_moves, c_x, c_y)

        for i in range(4):
            n_x = c_x + x_dir[i]
            n_y = c_y + y_dir[i]

            if(0 <= n_x < w and 0 <= n_y < h and visited[n_y][n_x]):
                que.append((c_moves+1, n_x, n_y))
                visited[n_y][n_x] = False

    return (-1, -1, -1)

# main function
if __name__ == '__main__':
    inputs = (input()).split()

    H = int(inputs[0])
    W = int(inputs[1])
    N = int(inputs[2])

    visited = [[True for i in range(W)] for j in range(H)]
    maps = ["" for i in range(H)]

    x, y = 0, 0
    for i in range(H):
        maps[i] = input()
        for j in range(W):
            if maps[i][j] == 'S':
                x, y = j, i

    moves = 0
    for i in range(1, N+1, 1):
        moves, x, y = bfs(H, W, str(i), x, y, moves)

    print(str(moves))
