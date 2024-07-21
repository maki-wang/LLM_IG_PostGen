# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 01:59
# @Author  : Maki Wang
# @FileName: main.py
# @Software: PyCharm
# !/usr/bin/env python3

from utils import generate_IG
import streamlit as st

st.header('AI Writing Assistant for Viral Instagram Posts')
with st.sidebar:
    openai_api_key = st.text_input('Please enter the OpenAI API key:', type='password')
    st.markdown('[Get the OpenAI API Key yourself](https://platform.openai.com/account/api-keys)')
    st.write('### Or you can contact *Xianmu Wang* to help you get the key: ✉️wangxianmu@gmail.com ')

theme = st.text_input('Theme')
submit = st.button('Start writing')

if submit and not openai_api_key:
    st.info("Please enter your OpenAI API key!")
    st.stop()
if submit and not theme:
    st.info("Please enter the theme of the generated content")
    st.stop()
if submit:
    with st.spinner('🤖AI is trying to create, please wait...'):
        result = generate_IG(theme, openai_api_key)
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('##### ⭐️Instagram Post Title 1')
        st.write(result.titles[0])
        st.markdown('##### ⭐️Instagram Post Title 2')
        st.write(result.titles[1])
        st.markdown('##### ⭐️Instagram Post Title 3')
        st.write(result.titles[2])
        st.markdown('##### ⭐️Instagram Post Title 4')
        st.write(result.titles[3])
        st.markdown('##### ⭐️Instagram Post Title 5')
        st.write(result.titles[4])
    with c2:
        st.markdown('##### ⭐️Instagram Post Main Body')
        st.write(result.content)