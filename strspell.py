# Dan Towers 2021

import argparse  #  I'll make it freindly later
import re
from spellchecker import SpellChecker

spell = SpellChecker()

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str)


def read_file(path):
    try:
        with open(path) as f:
            return f.read().splitlines()
    except:
        return []


def find_str(line):
    strings = re.findall(r"(?:['\"](?:\w[^'\"s]*s?)*['\"])", line)
    if not strings:
        return []
    ret = []
    for string in strings:
        string = string[1:-1].split()
        ret.extend(string)
    return ret


def parse_strings(contents):
    corrections = []
    for line in contents:
        strings = find_str(line)
        for string in strings:
            candidate = spell.correction(string)
            if candidate != string:
                corrections.append((candidate, string))
    return corrections


def report(corrections):
    for candidate, string in corrections:
        print(f'{string} - Did you mean "{candidate}"?')


if __name__ == "__main__":
    args = parser.parse_args()
    contents = read_file(args.path)
    corrections = parse_strings(contents)
    report(corrections)
