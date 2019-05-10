#!/usr/bin/env python
#This program will open and reformat the diabetes dataset

import os

file_path = 'diabetes.data'
if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, program will crash')

file = open('diabetes.data')

corrected_file = []
i = 0
for line in file.readlines():
	clean_line = line.replace("\t",' ').strip()
	line_values = clean_line.split(' ')
	corrected_line = []
#First line of the file are strings, they are the column labels
	if i > 0:
		for value in line_values:
			if (float(value)).is_integer():
				corrected_line.append(int(value))	 
			else:
				corrected_line.append(float(value))
		corrected_file.append(corrected_line)
	else:
		corrected_file.append(line_values)
	i = i+1
#print(corrected_file)

#Reach part of homework, transposing values
corrected_list = list(map(list,zip(*corrected_file)))
#print(corrected_list)

#Reach part of class 4 homework

import pandas as pd
import numpy as np

df = pd.DataFrame(corrected_file, )
df_new=df.drop([0], axis=0)
df_new.columns = ['Age', 'Sex', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']
print(df_new)

print(df_new.mean(axis=0))
print(df_new.std(axis=0))
file.close()
