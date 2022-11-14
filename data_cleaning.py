# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:27:24 2022

@author: Roy Waswa
"""


import pandas as pd

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 90)


so_data_2022 = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2022/survey_results_public.csv')
so_data_2021 = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2021/survey_results_public.csv')
so_data_2020 = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2020/survey_results_public.csv')
so_data_2019 = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2019/survey_results_public.csv')
so_data_2018 = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2018/survey_results_public.csv')
so_data_2017 = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2017/survey_results_public.csv')
