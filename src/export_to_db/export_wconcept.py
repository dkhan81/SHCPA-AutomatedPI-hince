from ..util.parse_list_file import parse_xls
from ..constants import directory
from ..initialization.mysql import *
from ..util import db
from ..constants import query


# load a csv file into list
parsed_list = parse_xls(directory.BROWSER_AUTOMATION_DOWNLOAD + "/" + "wconcept.xlsx")

# set an empty list for storing results
parsed_list_to_export = []


for item in parsed_list[1:]:

  # align each row according to table schema
  row = {
    "channel" : 'wconcept',
    "order_number" : item[5],
    "product_name" : item[12],
    "product_price" : int(float(item[19])),
    "quantity" : int(item[16]),
    "shipping_fee" : int(float(item[20])),
    "total_price": 0,
    "paid_price": 0,
    "order_date" : item[1] + " " + item[2] + ":00",
    "paid_date" : item[1] + " " + item[2] + ":00",
    "shipped_date" : item[3] + " 00:00:00",
    "refunded_date" : "",
  }

  row['total_price'] = row['product_price'] * row['quantity'] + row['shipping_fee']
  row['paid_price'] = row['product_price'] * row['quantity'] + row['shipping_fee']

  parsed_list_to_export.append(tuple(row.values()))

# execute the query to export data
db.exec_multiple_queries(query.WCONCEPT_INSERT, parsed_list_to_export)