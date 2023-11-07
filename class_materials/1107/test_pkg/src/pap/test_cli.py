import argparse

from pap.test import do_something

def test_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--option")
    args = parser.parse_args()
    
    do_something(args.option)
