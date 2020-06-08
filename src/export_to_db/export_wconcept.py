from ..util.parse_list_file import *
from ..constants.directory import *
from ..initialization.mysql import *
from ..util.db import *
from ..constants import query


# load a csv file into list
parsed_list = parse_xls(BROWSER_AUTOMATION_DOWNLOAD + "/" + "wconcept.xlsx")

# set an empty list for storing results
parsed_list_to_export = []


for item in parsed_list[1:]:
  # align each row according to table schema
  channel = 'wconcept'
  order_number = item[5]
  product_name = item[12]
  product_price = int(float(item[19]))
  quantity = int(item[16])
  shipping_fee = item[20]
  total_price = product_price * quantity
  order_date = item[1]

  parsed_list_to_export.append((channel, order_number, product_name, product_price, quantity, shipping_fee, total_price, order_date))

for i in parsed_list_to_export:
  print(i)
# execute the query to export data
exec_multiple_queries(query.WCONCEPT_INSERT, parsed_list_to_export)