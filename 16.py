import re

def get_invalid(rules, nearby):
    # build valid set
    valid = set()
    for v in rules.values():
        valid |= set(range(v[0],v[1]+1)) | set(range(v[2],v[3]+1))

    total = 0
    valid_tickets = []
    for line in nearby:
        line_total = sum([num for num in line if num not in valid])

        if line_total == 0:
            valid_tickets.append(line)
        total += line_total

    return total, valid_tickets

if __name__ == "__main__":
    with open('inputs/16.txt', 'r') as file:
        lines = file.read()

    rules, my_ticket, nearby = lines.split("\n\n")

    rules = {rule.split(':')[0]: list(map(int, re.findall(r'\d+', rule))) for rule in rules.split('\n')}
    my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
    nearby = [list(map(int, line.split(','))) for line in nearby.split('\n')[1:]]


    total, valid_tickets = get_invalid(rules, nearby)
    print(total)

    print(len(valid_tickets))