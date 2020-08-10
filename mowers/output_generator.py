class OutputGenerator:

    def __init__(self):
        self.results = {}

    def append_result(self, x, y, orientation, order):
        self.results[order] = f"{x} {y} {orientation}"

    def print_in_order(self):
        for order in sorted(self.results):
            print(self.results[order])
