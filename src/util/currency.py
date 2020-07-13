# string 타입으로 들어온 소숫점이 포함된 숫자를 int로 변환

def convertToInt(price):
  if not price:
    return 0
  else:
    return int(float(price))