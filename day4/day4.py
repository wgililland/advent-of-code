from functools import partial
import re

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

hair_color_re = re.compile('^#[0-9a-f]{6}$')
pid_re = re.compile('^[0-9]{9}$')


def parse_passport(raw_passport):
    return dict(field.split(':') for field in raw_passport.split())


def parse_passports(raw_passports):
    return [parse_passport(raw_passport)
            for raw_passport in raw_passports.split('\n\n')]


def validate_year(year, low, high):
    return year.isdigit() and low <= year <= high


def validate_height(height):
    measure, height = height[-2:], height[:-2]
    if measure == 'cm':
        return height.isdigit() and '150' <= height <= '193'
    elif measure == 'in':
        return height.isdigit() and '59' <= height <= '76'


def validate_hair_color(color):
    return bool(hair_color_re.match(color))


def validate_eye_color(color):
    return color in eye_colors


def validate_pid(pid):
    return bool(pid_re.match(pid))


def validate_cid(cid):
    return True


validate_fields = {
    'byr': partial(validate_year, low='1920', high='2002'),
    'iyr': partial(validate_year, low='2010', high='2020'),
    'eyr': partial(validate_year, low='2020', high='2030'),
    'hgt': validate_height,
    'hcl': validate_hair_color,
    'ecl': validate_eye_color,
    'pid': validate_pid,
    'cid': validate_cid,
}


def check_fields_exist(passport, fields):
    return all(rule in passport for rule in fields)


def validate_passport(passport, fields):
    return (
        check_fields_exist(passport, fields)
        and all(validate_fields[field](value)
                for field, value in passport.items())
    )


if __name__ == '__main__':
    with open('input_day4', 'r') as passport_data:
        passports = parse_passports(passport_data.read())
    print('P1:', sum(check_fields_exist(passport, fields)
                     for passport in passports))

    print('P2:', sum(validate_passport(passport, fields)
                     for passport in passports))
