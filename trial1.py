# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:35:57 2022

@author: Roy Waswa
"""
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


source_df = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2022/survey_results_public.csv')
source_schema_df = pd.read_csv(
    'C:/Users/Roy Waswa/Documents/DEV/SO_DATA/so-survey-2022/survey_results_schema.csv')


focus_cols = [
    'MainBranch', 'Employment', 'RemoteWork',
    'CodingActivities', 'EdLevel', 'LearnCode', 'LearnCodeOnline',
    'LearnCodeCoursesCert', 'YearsCode', 'YearsCodePro', 'DevType',
    'OrgSize', 'PurchaseInfluence', 'Country', 'Currency',
    'CompTotal', 'CompFreq', 'Age', 'Gender'
]
focus_df = source_df[focus_cols]
#focus_df.to_csv("focus.csv", index=False)


employment_sr = focus_df['Employment']

employed_dev_df = focus_df[employment_sr.str.contains(
    'Employed', na=False)]['Employment'].count()
students_dev_df = focus_df[employment_sr.str.contains(
    'Student', na=False)]['Employment'].count()
retired_dev_df = focus_df[employment_sr.str.contains(
    'Retired', na=False)]['Employment'].count()
unemployed_dev_df = focus_df[employment_sr.str.contains(
    'Not employed', na=True)]['Employment'].count()

# percentage_employed = np.round((employed_dev_df['Employment'].count()/focus_df['Employment'].count())*100, 2)
employment_data = [
    ['Employed', 'Student', 'Retired', 'Unemployed'],
    [employed_dev_df, students_dev_df, retired_dev_df, unemployed_dev_df]
]

plt.style.use('seaborn-v0_8-notebook')
plt.tight_layout

# Plot data
labels = ['Employed', 'Student', 'Retired', 'Unemployed']
y_data = [employed_dev_df, students_dev_df, retired_dev_df, unemployed_dev_df]

employment_bar = plt.bar(
    employment_data[0],
    employment_data[1],
    color=['b', 'k', 'r', 'g'],
    animated=True,
    capstyle="butt"
)
employment_bar.set_label('EMPLOYMENT STATUS OF CORRESPONDANCE')


