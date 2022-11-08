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

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    app.run()