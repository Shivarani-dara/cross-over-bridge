from collections import deque

times = {'A':5, 'B':10, 'G':20, 'D':25}

def bfs():
    init = (frozenset(['A','B','G','D']), frozenset(), 'L', 0)
    queue = deque()
    queue.append((init, [init]))
    visited = set()

    while queue:
        state, path = queue.popleft()
        left, right, side, time_so_far = state
        if time_so_far > 60:
            continue
        if len(left)==0 and side=='R':
            return path
        key = (left, side)
        if key in visited:
            continue
        visited.add(key)

        if side=='L':
            for p1 in left:
                for p2 in left:
                    if p1==p2:
                        t = times[p1]
                        new_left = set(left)
                        new_left.remove(p1)
                        new_right = set(right)
                        new_right.add(p1)
                        new_state = (frozenset(new_left), frozenset(new_right), 'R', time_so_far+t)
                        queue.append((new_state, path+[new_state]))
                    else:
                        t = max(times[p1], times[p2])
                        new_left = set(left)
                        new_left.remove(p1)
                        new_left.remove(p2)
                        new_right = set(right)
                        new_right.add(p1)
                        new_right.add(p2)
                        new_state = (frozenset(new_left), frozenset(new_right), 'R', time_so_far+t)
                        queue.append((new_state, path+[new_state]))
        else:
            for p in right:
                t = times[p]
                new_right = set(right)
                new_right.remove(p)
                new_left = set(left)
                new_left.add(p)
                new_state = (frozenset(new_left), frozenset(new_right), 'L', time_so_far+t)
                queue.append((new_state, path+[new_state]))
    return None

res = bfs()
if res:
    print("BFS found solution:")
    for step in res:
        left,right,side,time = step
        print(f"L:{left} | R:{right} | Umbrella:{side} | Time:{time}")
else:
    print("No solution")
