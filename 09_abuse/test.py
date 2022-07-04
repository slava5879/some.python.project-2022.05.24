#!/usr/bin/env python3
"""tests for abuse.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './abuse.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'py {prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_adjective_str():
    """bad_adjectives"""

    bad = random_string()
    rv, out = getstatusoutput(f'py {prg} -a {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_adjective_num():
    """bad_adjectives"""

    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'py {prg} -a {n}')
    print(out)
    assert rv != 0
    assert re.search(f'--adjectives "{n}" must be > 0', out)


# --------------------------------------------------
def test_bad_number_str():
    """bad_number"""

    bad = random_string()
    rv, out = getstatusoutput(f'py {prg} -n {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_number_int():
    """bad_number"""

    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'py {prg} -n {n}')
    assert rv != 0
    assert re.search(f'--number "{n}" must be > 0', out)


# --------------------------------------------------
def test_bad_seed():
    """bad seed"""

    bad = random_string()
    rv, out = getstatusoutput(f'py {prg} -s {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_01():
    """test"""

    out = getoutput(f'py {prg} -s 1 -n 1')
    assert out.strip() == 'You cullionly, insatiate braggart!'


# --------------------------------------------------
def test_02():
    """test"""

    out = getoutput(f'py {prg} --seed 2')
    expected = """
You detestable, peevish ass!
You lecherous, insatiate carbuncle!
You heedless, caterwauling worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    """test"""

    out = getoutput(f'py {prg} -s 3 -n 5 -a 1')
    expected = """
You vile degenerate!
You peevish braggart!
You sodden-witted worm!
You cullionly villain!
You bankrupt worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_04():
    """test"""

    out = getoutput(f'py {prg} --seed 4 --number 2 --adjectives 4')
    expected = """
You lecherous, dishonest, rotten, sodden-witted degenerate!
You detestable, cullionly, base, rotten butt!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))