import re

def parse(lines):
    input_split = lines.split('\n\n')
    passports = []
    for input in input_split:
        input = input.replace('\n', ' ')
        fields = [field.split(':') for field in input.split(' ')]
        passports.append(dict(fields))
    return passports

if __name__ == "__main__":
    with open('inputs/04.txt', 'r') as file:
        input = file.read()
    passports = parse(input)

    requirements = {
                    'byr': r'^19[2-9][0-9]$|^200[0-2]$',
                    'iyr': r'^(201[0-9]|2020)$',
                    'eyr': r'^202[0-9]$|2030$',
                    'hgt': r'^1(([5-8][0-9])|9[0-3])cm$|^(59|6[0-9]|7[0-6])in$',
                    'hcl': r'^#[a-f0-9]{6}$',
                    'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
                    'pid': r'^\d{9}$'
                    }
    fields = set(requirements.keys())

    # part 1
    print(sum([fields.issubset(passport) for passport in passports]))

    
    def is_valid(passport):
        return all([re.match(req, passport.get(field, "")) != None for field, req in requirements.items()])

    # part 2
    print(sum([is_valid(passport) for passport in passports]))