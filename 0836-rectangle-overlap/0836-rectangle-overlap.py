class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return not (x2 <= x3 or  # rec1 is to the left
                x1 >= x4 or  # rec1 is to the right
                y2 <= y3 or  # rec1 is below
                y1 >= y4)    # rec1 is above