from openpyxl import load_workbook
import csv

def parse_xls(location):
  load_wb = load_workbook(location, data_only=True)
  load_ws = load_wb.active
  
  return list(load_ws.iter_rows(values_only=True))

def parse_csv(location):
  with open(location, 'r') as csv_file:
    parsed_list = []
    
    for row in csv.reader(csv_file):
      parsed_list.append(row)

  return parsed_list
