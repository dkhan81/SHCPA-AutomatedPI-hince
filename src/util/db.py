from ..initialization.mysql import mysqlInstance

def exec_query(query_str, input_param=""):
  try:
    cursor = mysqlInstance.cursor()
    cursor.execute(query_str, input_param)

    return cursor.fetchall()
  except Exception as err:
    print(err)
    pass

def exec_multiple_queries(query_str, input_params=""):
  try:
    cursor = mysqlInstance.cursor()
    cursor.executemany(query_str, input_params)

    return cursor.fetchall()
  except Exception as err:
    print(err)
    pass