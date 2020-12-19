def parse(rules):
    rules_dict = {}
    for line in rules:
        num, rule = line.split(": ")
        if '"' in rule:
            rules_dict[int(num)] = rule[1]
        else:
            rules_dict[int(num)] = [[int(r) for r in r.split()] for r in rule.split("|")]

    return rules_dict

def get_matches(message, rules_dict):

    def helper(message, r):
        if rules_dict[r] == 'a' or rules_dict[r] == 'b':
            return {1} if (message and message[0] == rules_dict[r]) else set()
        else:
            overall_matches = set()
            for opt in rules_dict[r]:
                opt_match = {0}
                for rule in opt:
                    new_match = set()
                    for n in opt_match:
                        new_match |= {n+m for m in helper(message[n:], rule)}
                    opt_match = new_match
                overall_matches |= opt_match
            return overall_matches

    return helper(message, 0)


if __name__ == "__main__":

    with open('inputs/19.txt', 'r') as file:
        rules, inputs = file.read().split("\n\n")

    rules = rules.split("\n")
    inputs = inputs.split("\n")

    rules_dict = parse(rules)

    # part 1
    print(sum(len(i) in get_matches(i,rules_dict) for i in inputs))

    # part 2
    rules_dict[8] = [[42], [42, 8]]
    rules_dict[11] = [[42, 31], [42, 11, 31]]
    print(sum(len(i) in get_matches(i,rules_dict) for i in inputs))
