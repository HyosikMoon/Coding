class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = []
        waiting = []
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # set curr
                if (i, j) not in visited:
                    curr = (i, j)
                else:
                    continue

                # if curr == 1, loop
                while grid[curr[0]][curr[1]] == "1":
                    visited.append(curr)

                    # step1. add adj 1s
                    # Right
                    if curr[1] < len(grid[i]) - 1 and grid[curr[0]][curr[1] + 1] == "1" and (curr[0], curr[1] + 1) not in visited:
                        waiting.append((curr[0], curr[1] + 1))
                    # Down
                    if curr[0] < len(grid) - 1 and grid[curr[0] + 1][curr[1]] == "1" and (curr[0] + 1, curr[1]) not in visited:
                        waiting.append((curr[0] + 1, curr[1]))
                    # Left
                    if curr[1] > 0 and grid[curr[0]][curr[1] - 1] == "1" and (curr[0], curr[1] - 1) not in visited:
                        waiting.append((curr[0], curr[1] - 1))
                    # Up
                    if curr[0] > 0 and grid[curr[0] - 1][curr[1]] == "1" and (curr[0] - 1, curr[1]) not in visited:
                        waiting.append((curr[0] - 1, curr[1]))

                    # step2. pop waiting value -> curr
                    if len(waiting) != 0:
                        curr = waiting.pop()
                    else:
                        cnt += 1
                        break
        return cnt

grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]

Solution().numIslands(grid)
