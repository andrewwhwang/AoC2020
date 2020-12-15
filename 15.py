
def game(input, steps):
    last = input[-1]
    history = {n: i + 1 for i, n in enumerate(input)}

    for i in range(len(input), steps):
        history[last], last = i, i - history.get(last, i)

    return last

if __name__ == "__main__":
    # part 1
    input = [16,11,15,0,1,7]
    steps = 2020
    print(game(input, steps))

    # part 2
    input = [16,11,15,0,1,7]
    steps = 30000000
    print(game(input, steps))