import sys
import collections

def get_input():
    return [list(line.strip()) for line in sys.stdin]

def solve(data):
    starts = []
    all_keys = 0
    rows, cols = len(data), len(data[0])
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '@':
                starts.append((i, j))
            elif 'a' <= data[i][j] <= 'z':
                all_keys |= 1 << (ord(data[i][j]) - ord('a'))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = collections.deque()
    initial_pos = tuple(starts)
    sorted_initial = tuple(sorted(initial_pos))
    visited.add((sorted_initial, 0))
    queue.append((initial_pos, 0, 0))

    while queue:
        positions, keys_mask, steps = queue.popleft()
        if keys_mask == all_keys:
            return steps

        for idx in range(4):
            x, y = positions[idx]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    cell = data[nx][ny]
                    if cell == '#':
                        continue
                    if 'A' <= cell <= 'Z' and not (keys_mask & (1 << (ord(cell) - ord('A')))):
                        continue

                    new_positions = list(positions)
                    new_positions[idx] = (nx, ny)
                    new_positions_sorted = tuple(sorted(new_positions))
                    new_mask = keys_mask
                    if 'a' <= cell <= 'z':
                        new_mask |= 1 << (ord(cell) - ord('a'))

                    state = (new_positions_sorted, new_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((tuple(new_positions), new_mask, steps + 1))

    return -1

def main():
    data = get_input()
    result = solve(data)
    print(result)

if __name__ == '__main__':
    main()