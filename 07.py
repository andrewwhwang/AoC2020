import re

def get_nesting(rules):
    bags = {}
    for rule in rules:
        out_bag, in_bags = rule.split(' bags contain ')
        parser = re.findall(r'(\d [a-z ]+) bag[s]?', in_bags)
        bags[out_bag] = {b[2:]:int(b[0]) for b in parser}
    return bags

if __name__ == "__main__":
    with open('inputs/07.txt', 'r') as file:
        rules = file.read().split('\n')

    bags = get_nesting(rules)

    # part 1
    def contains_shiny(bag):
        if 'shiny gold' in bags[bag]:
            return True
        return any(contains_shiny(b) for b in bags[bag])
    print(sum([contains_shiny(color) for color in bags if color != 'shiny gold']))

    # part 2
    def num_bags(bag):
        if bag not in bags:
            return 0
        return sum(v + v * num_bags(k) for k, v in bags[bag].items())
    print(num_bags('shiny gold'))