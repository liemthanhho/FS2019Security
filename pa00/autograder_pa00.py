#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:02:31 2018
@author: taylor@mst.edu
"""

import os
import csv
import subprocess
import sys
from glob import glob
import shutil
import numpy as np
import pandas as pd


def stdout_diff(student_folder, language, script):
    print('\t Testing stdout_diff')

    try:
        os.chdir(student_folder)

        subprocess.run([language,
                        script,
                        'test_input.txt',
                        language + '_your_test_output.txt'],
                       timeout=5)

        os.chdir('../../../pa00-environment_admin-grader/')

        diff_output1 = subprocess.run(['diff',
                                       student_folder + language + '_your_test_output.txt',
                                       'correct_output.txt'],
                                      timeout=5,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

        diff_output2 = subprocess.run(['diff',
                                       '--ignore-all-space',
                                       '--ignore-blank-lines',
                                       student_folder + language + '_your_test_output.txt',
                                       'correct_output.txt'],
                                      timeout=5,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)


        if diff_output1.returncode and diff_output2.returncode:
            return diff_output1.stderr.decode()
        else:
            with open(student_folder + language + '_your_diff_from_correct.txt', 'w') as output_file:
                output_file.write(diff_output1.stdout.decode())
                if len(diff_output1.stdout.decode()) == 0:
                    return 0
                elif len(diff_output2.stdout.decode()) == 0:
                    return 5
                else:
                    return len(diff_output1.stdout.decode())

    except Exception as e:
        os.chdir('../../../pa00-environment_admin-grader/')
        return e


def store_student_data(result_array, folder):
    with open("{}results.csv".format(folder), "w") as f:
        w = csv.writer(f)
        w.writerows(result_array)


# %%
# This helps when everyone has a different directory
# First argument is path relative to where you execute this script, e.g.,
# python3 grader.py ../../student_submissions/pa03
if(1 < len(sys.argv)):
    parent_dir_of_student_repos = sys.argv[1]
else:
    # Or, make the students directory the relative path to cwd
    parent_dir_of_student_repos = '../student_submissions/pa00-environment'

students_to_try = os.listdir(parent_dir_of_student_repos)

# For debugging a single or couple students, uncomment this line:
#students_to_try = ['mcmhd3']

#Name the fields with very informative names!
headers = ['Username',
           'python unit test (0 perfect, 5 had extra newlines, 10 had something else)',
           'bash unit test (0 perfect, 5 had extra newlines, 10 had something else)',
           '.bash_history file existed (10 for True, 0 for False)', 
           'diff.png file existed (10 for True, 0 for False)',
           'debug1.png file existed (10 for True, 0 for False)',
           'debug2.png file existed (10 for True, 0 for False)']

aggregate_results = pd.DataFrame(columns=headers)

# Assumes there is nothing else in the parent_dir_of_student_repos
for i, username in enumerate(students_to_try):
    print('Student: ' + str(i) + ': ' + username)
    student_folder = "{}/{}/".format(parent_dir_of_student_repos, username)

    shutil.copy('test_input.txt', student_folder + 'test_input.txt')

    student_results = [username]
    student_results.append(stdout_diff(student_folder, 'python3', 'pa00.py'))
    student_results.append(stdout_diff(student_folder, 'bash', 'pa00.sh'))
    student_results.append(os.path.exists(student_folder + '.bash_history'))
    student_results.append(os.path.exists(student_folder + 'diff.png'))
    student_results.append(os.path.exists(student_folder + 'debug1.png'))
    student_results.append(os.path.exists(student_folder + 'debug2.png'))

    store_student_data([headers, student_results], student_folder)
    aggregate_results.loc[len(aggregate_results)] = student_results

# aggregate_results.to_csv('aggregate_results.csv')
aggregate_results.to_pickle('aggregate_results.pkl')


# %% Re-import for any data processing. Compute weighted means of pass/fail:
df_reloaded = pd.read_pickle('aggregate_results.pkl')

df_reloaded['python_pts'] = \
    pd.to_numeric(df_reloaded['python unit test (0 perfect, 5 had extra newlines, 10 had something else)'],
                  errors='coerce')

df_reloaded['bash_pts'] = \
    pd.to_numeric(df_reloaded['bash unit test (0 perfect, 5 had extra newlines, 10 had something else)'],
                  errors='coerce')

df_reloaded['python_pts'] = df_reloaded['python_pts'].fillna(10)
df_reloaded['bash_pts'] = df_reloaded['bash_pts'].fillna(10)

df_reloaded['bash hist points'] = np.where(df_reloaded['.bash_history file existed (10 for True, 0 for False)'] == True, 0, 10)
df_reloaded['diff points'] = np.where(df_reloaded['diff.png file existed (10 for True, 0 for False)'] == True, 0, 10)
df_reloaded['debug1 points'] = np.where(df_reloaded['debug1.png file existed (10 for True, 0 for False)'] == True, 0, 10)
df_reloaded['debug2 points'] = np.where(df_reloaded['debug2.png file existed (10 for True, 0 for False)'] == True, 0, 10)

df_reloaded['Grand_avg'] = 60 - \
                           df_reloaded['python_pts'] - \
                           df_reloaded['bash_pts'] - \
                           df_reloaded['bash hist points'] - \
                           df_reloaded['diff points'] - \
                           df_reloaded['debug1 points'] - \
                           df_reloaded['debug2 points']

df_reloaded = df_reloaded.sort_index()

df_reloaded.to_csv('Grades.csv')

