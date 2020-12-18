import re

class a(int):
    def __mul__(self, b):
        return a(int(self) + b)
    def __add__(self, b):
        return a(int(self) + b)
    def __sub__(self, b):
        return a(int(self) * b)

def ev(expr, pt2=False):
    expr = re.sub(r"(\d+)", r"a(\1)", expr)
    expr = expr.replace("*", "-")
    if pt2:
        expr = expr.replace("+", "*")
    return eval(expr, {}, {"a": a})


if __name__ == "__main__":

    with open('inputs/18.txt', 'r') as file:
        lines = file.read().split("\n")

    print("Part 1:", sum(ev(l) for l in lines))
    print("Part 2:", sum(ev(l, pt2=True) for l in lines))