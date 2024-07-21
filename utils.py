# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 00:16
# @Author  : Maki Wang
# @FileName: utils.py
# @Software: PyCharm
# !/usr/bin/env python3

from prompt_template import system_template_text, user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from IG_model import IG_model

def generate_IG(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ('system', system_template_text),
        ('user', user_template_text)
    ])
    model = ChatOpenAI(model='gpt-3.5-turbo', api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=IG_model)

    chain = prompt | model | output_parser
    result = chain.invoke({
        'parser_instructions':output_parser.get_format_instructions(),
        'theme':theme
    })
    return result