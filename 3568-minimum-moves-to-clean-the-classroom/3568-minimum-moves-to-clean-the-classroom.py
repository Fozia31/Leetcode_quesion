class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """

        from collections import deque

        m = len(classroom)
        n = len(classroom[0])

        # Find start and number every litter
        litter_id = [[-1] * n for _ in range(m)]

        sr = sc = 0
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        all_mask = (1 << litter_count) - 1

        # best[r][c][mask] = maximum energy with which
        # we have reached (r,c) having collected mask.
        #
        # Using a dictionary avoids allocating a huge 3D array.
        best = {}

        start = (sr, sc, 0)
        best[start] = energy

        q = deque()
        q.append((sr, sc, energy, 0))

        moves = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:

            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == all_mask:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    # Recharge
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        nmask |= 1 << litter_id[nr][nc]

                    key = (nr, nc, nmask)

                    # If we have already reached this position with
                    # this mask using at least as much energy,
                    # this state can never be useful.
                    if key in best and best[key] >= ne:
                        continue

                    best[key] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1