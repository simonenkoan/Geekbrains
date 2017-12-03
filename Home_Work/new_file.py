from curtsies.input import *

def main():
    """Ideally we shouldn't lose the first second of events"""
    with Input() as input_generator:
        for e in input_generator:
            print(repr(e))
if __name__ == '__main__':
    main()