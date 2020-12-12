import math

class ship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ang = 0
    
    def manhattan(self):
        return abs(self.y) + abs(self.x)

    def forward(self, dist):
        self.y += dist * round(math.sin(self.ang * math.pi / 180))
        self.x += dist * round(math.cos(self.ang * math.pi / 180))

class waypoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def turn(self, ang):
        ang *= math.pi / 180
        x, y = self.x, self.y

        self.x = round(x * math.cos(ang) - y * math.sin(ang))
        self.y = round(x * math.sin(ang) + y * math.cos(ang))

if __name__ == "__main__":
    with open('inputs/12.txt', 'r') as file:
        lines = file.read().split('\n')

    # part 1
    s = ship()
    for line in lines:
        action, mag = line[0], int(line[1:])
        if action == 'N':
            s.y += mag
        elif action == 'S':
            s.y -= mag
        elif action == 'E':
            s.x += mag
        elif action == 'W':
            s.x -= mag
        elif action == 'L':
            s.ang += mag
            s.ang %= 360
        elif action == 'R':
            s.ang -= mag
            s.ang %= 360
        elif action == 'F':
            s.forward(mag)

    print(s.manhattan())

    # part 2
    s = ship()
    w = waypoint(10, 1)
    for line in lines:
        action, mag = line[0], int(line[1:])
        if action == 'N':
            w.y += mag
        elif action == 'S':
            w.y -= mag
        elif action == 'E':
            w.x += mag
        elif action == 'W':
            w.x -= mag
        elif action == 'L':
            w.turn(mag)
        elif action == 'R':
            w.turn(-mag)
        elif action == 'F':
            s.x += w.x * mag
            s.y += w.y * mag

    print(s.manhattan())