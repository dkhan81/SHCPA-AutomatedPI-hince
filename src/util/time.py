from datetime import datetime, timedelta

def get_today_date(with_hyphen = True):
  today = datetime.now()
  
  if with_hyphen:
    return today.strftime("%Y-%m-%d")
  else:
    return today.strftime("%Y%m%d")

def get_today_datetime(with_hyphen = True):
  today = datetime.now()
  
  if with_hyphen:
    return today.strftime("%Y-%m-%d %H:%M:%S")
  else:
    return today.strftime("%Y%m%d %H:%M:%S")

def get_past_date(backto = 1, with_hyphen = True):
  past = datetime.now() - timedelta(days = backto)

  if with_hyphen:
    return past.strftime("%Y-%m-%d")
  else:
    return past.strftime("%Y%m%d")
  
