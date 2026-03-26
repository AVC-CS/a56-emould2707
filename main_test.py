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

@pytest.mark.T1
def test_main_1():
    # N=3: triangle has 6 pairs
    content = open('result1.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 6, f'Expected 6 pairs, got {len(pairs)}'
    regex_test([r'(?<![,\d])0\s*,\s*2(?![,\d])', r'(?<![,\d])2\s*,\s*0(?![,\d])', r'(?<![,\d])2\s*,\s*2(?![,\d])'], content)

@pytest.mark.T2
def test_main_2():
    # N=10: triangle has 55 pairs
    content = open('result2.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 55, f'Expected 55 pairs, got {len(pairs)}'
    regex_test([r'(?<![,\d])0\s*,\s*9(?![,\d])', r'(?<![,\d])9\s*,\s*0(?![,\d])', r'(?<![,\d])9\s*,\s*9(?![,\d])'], content)

@pytest.mark.T3
def test_main_3():
    # N=1: triangle has 1 pair
    content = open('result3.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 1, f'Expected 1 pair, got {len(pairs)}'
    regex_test([r'(?<![,\d])0\s*,\s*0(?![,\d])'], content)

@pytest.mark.T4
def test_main_4():
    # N=4: triangle has 10 pairs
    content = open('result4.txt').read()
    pairs = re.findall(r'(?<![,\d])\d+\s*,\s*\d+(?![,\d])', content)
    assert len(pairs) == 10, f'Expected 10 pairs, got {len(pairs)}'
    regex_test([r'(?<![,\d])0\s*,\s*3(?![,\d])', r'(?<![,\d])3\s*,\s*0(?![,\d])', r'(?<![,\d])3\s*,\s*3(?![,\d])'], content)
