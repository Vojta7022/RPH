from pathlib import Path

class MyMatrix:
    def __init__(self, matrix = []):
        self.matrix = matrix

    def save(self, filename):
        p = Path(filename)
        with p.open("wt", encoding="utf-8") as f:
            for row in self.matrix:
                f.write(" ".join(map(str, row)) + "\n")
                
    def load(self, filename):
        p = Path(filename)
        with p.open("rt", encoding="utf-8") as f:
            elem = f.read().strip().split("\n")
            self.matrix += [list(map(int, e.split())) for e in elem]
            
    def get_matrix(self):
        return self.matrix


if __name__ == "__main__":
    a = MyMatrix([[1, 2, 3], [2, 3, 4]])
    a.save('matrix.txt')
    print(a.get_matrix())
    b = MyMatrix()
    b.load('matrix.txt')
    print(b.get_matrix())
    print(a.get_matrix() == b.get_matrix())
