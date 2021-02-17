import csv
import pandas as pd

# File Path Location
root_path = r'D:/celonis_case_study/'
raw_data_folder = 'raw_data/'
file_name = 'claims-data-export'
raw_data_path = root_path + raw_data_folder + file_name

def create_path(root_path, raw_folder, file_name):
     """Takes in strings and generates file path for txt file and csv file"""
     raw_data_path = root_path + raw_data_folder + file_name
     return (f"{raw_data_path}.txt", f"{raw_data_path}.csv")

# Creates tuple storing file path information for both txt and csv files. 
txt_file, csv_file = create_path(root_path, raw_data_folder, file_name)

with open(txt_file, 'r') as infile, open(csv_file, 'w') as outfile:
     stripped = (line.strip() for line in infile)
     lines = (line.split("|") for line in stripped if line)
     writer = csv.writer(outfile)
     writer.writerows(lines)
