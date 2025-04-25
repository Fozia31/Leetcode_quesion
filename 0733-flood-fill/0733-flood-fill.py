class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        start_point = image[sr][sc]
        if start_point == color:
            return image

        def dfs(sr , sc):
            if 0 <= sr < rows and 0 <= sc < cols and image[sr][sc] == start_point:
                image[sr][sc] = color
                dfs(sr + 1 , sc)
                dfs(sr - 1 , sc)
                dfs(sr , sc + 1)
                dfs(sr , sc - 1)

            else:
                return

        dfs(sr , sc)
        return image