#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

import math


def geometric_zn(*args):
    if args:
        value = 1
        for arg in args:
            value *= arg
        return math.pow(value, 1 / len(args))
    else:
        return None


if __name__ == "__main__":
    print(geometric_zn(1, 3, 2))
