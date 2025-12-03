class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (cx, cy), cnt in list(self.points.items()):
            if cx != x or cy == y:
                continue

            d = abs(cy - y)

            res += (cnt *
                    self.points[(x + d, y)] *
                    self.points[(x + d, cy)])

            res += (cnt *
                    self.points[(x - d, y)] *
                    self.points[(x - d, cy)])
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)