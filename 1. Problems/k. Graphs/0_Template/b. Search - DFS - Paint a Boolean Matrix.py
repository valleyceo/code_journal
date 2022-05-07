# Paint a Boolean Matrix (Flip Color region, DFS)

'''
- Given a 2D array with black or white cell and a coordinate
- Change all neighbor of same color to opposite
'''

# Time complexity: O(mn)
def flip_color(x: int, y: int, image: List[List[bool]]) -> None:

    color = image[x][y]
    q = collections.deque([(x, y)])
    image[x][y] = not image[x][y]  # Flips.
    while q:
        x, y = q.popleft()
        for next_x, next_y in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
                    and image[next_x][next_y] == color):
                # Flips the color.
                image[next_x][next_y] = not image[next_x][next_y]
                q.append((next_x, next_y))
