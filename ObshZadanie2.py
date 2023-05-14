#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def harmonic(*args):
    return len(args) / sum([1 / i for i in args])


if __name__ == "__main__":
    print(harmonic(2, 1, 7))
