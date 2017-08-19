#!/usr/bin/env python
# --coding:utf-8--

from os import path
from ctypes import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="set the proxy for IE.")
    parser.add_argument('-s', '--switch', help='turn on proxy', required=True)
    parser.add_argument('-p', '--proxy', help='proxy address', required=False)
    args = parser.parse_args()
    print(args.proxy, args.switch)
    dll_path = path.realpath(path.join(path.dirname(path.realpath(__file__)), "ieproxy"))
    lib = cdll.LoadLibrary(dll_path)
    lib.setproxy(args.proxy, args.switch == "1")
