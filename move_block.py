from collections import deque
directions = [(-1, 0), (1, 0), (0,-1), (0, 1)]


def check(loc):
    y, x = loc
    if y < 0 or y > N-1 or x < 0 or x > N-1:
        return False
    if table[y][x] == 1:
        return False
    return True


def move(loc1, loc2):
    Y, X = 0, 1
    path = []
    for dy, dx in directions:
        next_loc1 = (loc1[Y] + dy, loc1[X] + dx)
        next_loc2 = (loc2[Y] + dy, loc2[X] + dx)
        if check(next_loc1) and check(next_loc2):
            path.append((next_loc1, next_loc2))

    if loc1[Y] == loc2[X]:
        U, D = -1,1
        for d in [U, D]:
            next_loc1 = (loc1[Y]+d, loc1[X])
            next_loc2 = (loc2[Y]+d, loc2[X])
            if check(next_loc1) and check(next_loc2):
                path.append((loc1, next_loc1))
                path.append((loc2, next_loc2))
    else:
        L, R = -1, 1
        for d in [L, R]:
            next_loc1 = (loc1[Y], loc1[X] + d)
            next_loc2 = (loc2[Y], loc2[X] + d)
            if check(next_loc1) and check(next_loc2):
                path.append((next_loc1, loc1))
                path.append((next_loc2, loc2))

    return path


def solution(board):
    global table, N
    table = board
    N = len(table)
    q = deque([((0, 0), (0, 1), 0)])
    visit = set()
    visit.add(((0, 0), (0, 1)))
    while q:
        loc1, loc2, answer = q.popleft()
        if loc1 == (N-1, N-1) or loc1 == (N-1, N-1):
            return answer

        for loc in set(move(loc1, loc2)) - visit:
            q.append((*loc, answer+1))
            visit.add(loc)
