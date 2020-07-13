from ..util.parse_list_file import *
from ..constants.directory import *
from ..initialization.mysql import *
from ..util.db import *
from ..constants import query


# load a csv file into list
parsed_list = parse_csv(BROWSER_AUTOMATION_DOWNLOAD + "/" + "cafe24.csv")

# set an empty list for storing results
parsed_list_to_export = []

for item in parsed_list[1:]:
  if item[14] == '판매가':
    continue

    # align each row according to the table schema
  row = {
    "channel" : 'cafe24',
    "order_number" : item[0],
    "product_name" : item[13],
    "product_price" : int(float(item[14])),
    "quantity" : int(item[15]),
    "shipping_fee" : int(float(item[18])),
    "total_price" : int(float(item[16])),
    "paid_price" : int(float(item[22])),
    "order_date" : item[3],
    "paid_date" : item[4],
    "shipped_date" : item[5],
    "refunded_date" : item[6],
    "address": item[24],
  }


  parsed_list_to_export.append(tuple(row.values()))

# execute the query to export data
exec_multiple_queries(query.CAFE24_INSERT, parsed_list_to_export)