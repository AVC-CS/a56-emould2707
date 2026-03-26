import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {token}'
        pos += res.start() + 1

def p(i, j):
    return rf'(?<![,\d]){i}\s*,\s*{j}(?![,\d])'

@pytest.mark.T1
def test_main_1():
    # N=3: triangle has 6 pairs
    content = open('result1.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 6, f'Expected 6 pairs, got {len(pairs)}'
    regex_test([
        p(0,2),
        p(1,1), p(1,2),
        p(2,0), p(2,1), p(2,2),
    ], content)

@pytest.mark.T2
def test_main_2():
    # N=10: triangle has 55 pairs
    content = open('result2.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 55, f'Expected 55 pairs, got {len(pairs)}'
    regex_test([
        p(0,9),
        p(1,8), p(1,9),
        p(2,7), p(2,8), p(2,9),
        p(3,6), p(3,7), p(3,8), p(3,9),
        p(4,5), p(4,6), p(4,7), p(4,8), p(4,9),
        p(5,4), p(5,5), p(5,6), p(5,7), p(5,8), p(5,9),
        p(6,3), p(6,4), p(6,5), p(6,6), p(6,7), p(6,8), p(6,9),
        p(7,2), p(7,3), p(7,4), p(7,5), p(7,6), p(7,7), p(7,8), p(7,9),
        p(8,1), p(8,2), p(8,3), p(8,4), p(8,5), p(8,6), p(8,7), p(8,8), p(8,9),
        p(9,0), p(9,1), p(9,2), p(9,3), p(9,4), p(9,5), p(9,6), p(9,7), p(9,8), p(9,9),
    ], content)

@pytest.mark.T3
def test_main_3():
    # N=1: triangle has 1 pair
    content = open('result3.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 1, f'Expected 1 pair, got {len(pairs)}'
    regex_test([p(0,0)], content)

@pytest.mark.T4
def test_main_4():
    # N=4: triangle has 10 pairs
    content = open('result4.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 10, f'Expected 10 pairs, got {len(pairs)}'
    regex_test([
        p(0,3),
        p(1,2), p(1,3),
        p(2,1), p(2,2), p(2,3),
        p(3,0), p(3,1), p(3,2), p(3,3),
    ], content)
