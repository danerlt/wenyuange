#!/usr/bin/env python
# -*- coding:utf-8 -*-  
""" 
@author: danerlt
@file: main.py 
@time: 2022-11-08
@contact: danerlt001@gmail.com
@desc: 
"""


import typer


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)