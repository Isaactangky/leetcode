class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        init_col = image[sr][sc]
        def flood(image, sr, sc,  color):
            if ( sr not in range(ROWS) or sc not in range(COLS) 
                or image[sr][sc] != init_col or image[sr][sc] == color):
                return
            image[sr][sc] = color
            
            flood(image, sr - 1, sc, color)
            flood(image, sr + 1, sc,  color)
            flood(image, sr , sc - 1,  color)
            flood(image, sr , sc + 1,  color)
            return
        flood(image, sr, sc, color)
        return image
