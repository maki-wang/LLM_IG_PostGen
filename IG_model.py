# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 01:16
# @Author  : Maki Wang
# @FileName: IG_model.py
# @Software: PyCharm
# !/usr/bin/env python3

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class IG_model(BaseModel):
    titles: List[str] = Field(description='5 Titles for Instagram', min_items=5, max_items=5)
    content: str = Field(description="The body content of Instagram")