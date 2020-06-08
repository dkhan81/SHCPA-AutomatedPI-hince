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
  # align each row according to table schema
  channel = 'cafe24'
  order_number = item[1]
  product_name = item[6]
  product_price = int(float(item[9]))
  quantity = int(item[8])
  shipping_fee = 0
  total_price = product_price * quantity
  order_date = item[0][0:4] + "-" + item[0][4:6] + "-" + item[0][6:8]

  parsed_list_to_export.append((channel, order_number, product_name, product_price, quantity, shipping_fee, total_price, order_date))

# execute the query to export data
exec_multiple_queries(query.CAFE24_INSERT, parsed_list_to_export)