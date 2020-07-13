from ..util.parse_list_file import *
from ..constants.directory import *
from ..initialization.mysql import *
from ..util.db import *
from ..util.time import *
from ..util.currency import *
from ..constants import query


# load a csv file into list
parsed_list = parse_csv(BROWSER_AUTOMATION_DOWNLOAD + "/" + "cafe24.csv")

# set an empty list for storing results
parsed_list_to_export = []

for item in parsed_list[1:]:

  # align each row according to the table schema
  row = {
    "YYYYMMDD" : get_past_date(1, False),
    "PAYMENT_SITE" : "cafe24",
    "ORDER_NO" : item[0],
    "ON_OFF_DIFF" : 'online',
    "COUNTRY_CD" : 'KR',
    "PRD_CD" : item[2],
    "PRD_NM" : item[4],
    "CUST_ID" : item[5],
    "ORDER_STATUS" : item[7].replace(" ", ""), #todo : parse string 필요
    "ORDER_DTTM" : item[14],
    "PAYMENT_DTTM" : item[15],
    "DELIV_DTTM" : item[16],
    "CONFIRM_DTTM" : "", #todo: 구매 확정일 계산 필요
    "REFUND_DTTM" : "", #todo : 20, 2"", 22중 하나 선택
    "EXCHANGE_DTTM" : "", #todo
    "RETURN_DTTM" : "", #todo
    "CANCEL_DTTM" : "", #todo
    "PRICE" : convertToInt(item[29]),
    "AMT" : convertToInt(item[30]),
    "TOTAL_ORDER_AMT" : convertToInt(item[31]),
    "SELLER_DUTY_DISCOUNT" : None,
    "TOTAL_DISCOUNT" : sum([convertToInt(item[x]) for x in [32, 33, 34, 35, 36, 38, 39, 40, 41]]),
    "USE_POINT" : convertToInt(item[42]),
    "DELIV_FEE" : convertToInt(item[44]),
    "TOTAL_PAYMENT_AMT" : convertToInt(item[45]),
    "REFUND_AMT" : convertToInt(item[46]),
    "ZIP_CD" : item[48],
    "ADDRESS" : item[49],
    "DELIV_FIRM" : None,
    "INVOICE" : item[50],
    "PG" : item[52],
    "CREATE_DTTM" : get_today_datetime(with_hyphen=True),
    "UPDATE_DTTM" : None,
  }

  # make the value of each column 'null' if it does not have any value
  for r in row:
    if row[r] == '':
      row[r] = None

  # for r in row:
  #   print(r, ": ", row[r])
  # break

  parsed_list_to_export.append(tuple(row.values()))

# execute the query to export data
exec_multiple_queries(query.CAFE24_TWO_INSERT, parsed_list_to_export)