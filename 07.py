import re

if __name__ == "__main__":
    with open('inputs/07.txt', 'r') as file:
        rules = file.read().split('\n')

    bags = {}
    for rule in rules:
        out_bag, in_bags = rule.split(' bags contain ')
        parser = re.findall(r'(\d [a-z ]+) bag[s]?', in_bags)
        bags[out_bag] = {b[2:]:int(b[0]) for b in parser}
        if 'shiny gold' in bags[out_bag]:
            print(out_bag)
    # print(bags)
