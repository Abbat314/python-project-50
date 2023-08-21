#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', nargs=1)
    parser.add_argument('second_file', nargs=1)

    args = parser.parse_args()

if __name__ == '__main__':
    main()