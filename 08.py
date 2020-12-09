def is_loop(lines):
    acc, line_num = 0, 0
    history = set()
    while True:
        if line_num >= len(lines):
            return False, acc
        if line_num in history:
            return True, acc
        history.add(line_num)

        line = lines[line_num]
        instruction, num = line[:3], int(line[4:])
        if instruction == 'acc':
            acc += num
            line_num += 1
        elif instruction == 'jmp':
            line_num += num
        elif instruction == 'nop':
            line_num += 1

if __name__ == "__main__":
    with open('inputs/08.txt', 'r') as file:
        lines = file.read().split('\n')

    # part 1
    print(is_loop(lines)[1])

    # part 2
    possible = [i for i, l in enumerate(lines) if l[:3] != 'acc']
    for error in possible:
        test = lines.copy()
        if test[error][:3] == 'jmp':
            test[error] = 'nop' + test[error][4:]
        elif test[error][:3] == 'nop':
            test[error] = 'jmp' + test[error][4:]

        loop, acc = is_loop(test)
        if not loop:
            print(acc)
            break