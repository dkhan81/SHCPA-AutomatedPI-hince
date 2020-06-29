from ..util.parse_list_file import parse_xlsv
from ..constants import directory
from ..initialization.mysql import *
from ..util import db
from ..constants import query


# load a csv file into list
parsed_list = parse_xlsv(directory.BROWSER_AUTOMATION_DOWNLOAD + "/" + "naver_storefarm.xlsx")

# set an empty list for storing results
parsed_list_to_export = []

for item in parsed_list[1:]:

  # align each row according to the table schema
  row = {
    "channel" : 'naver_storefarm',
    "order_number" : item[0],
    "product_name" : item[13],
    "product_price" : int(float(item[17])),
    "quantity" : int(item[16]),
    "shipping_fee" : int(float(item[38])),
    "total_price": 0,
    "paid_price": 0,
    "order_date" : item[22],
    "paid_date" : item[22],
    "shipped_date" : item[23],
    "refunded_date" : "",
    "address": item[43]
  }

  row['product_name'] = row['product_name'].replace("[공식] [hince] 힌스 ", "")
  row['total_price'] = row['product_price'] * row['quantity'] + row['shipping_fee']
  row['paid_price'] = row['product_price'] * row['quantity'] + row['shipping_fee']

  parsed_list_to_export.append(tuple(row.values()))

# execute the query to export data
db.exec_multiple_queries(query.NAVER_STOREFARM_INSERT, parsed_list_to_export)