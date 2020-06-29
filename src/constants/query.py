CAFE24_INSERT =  """INSERT IGNORE INTO luxury.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

WCONCEPT_INSERT =  """INSERT IGNORE INTO luxury.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

NAVER_STOREFARM_INSERT =  """INSERT IGNORE INTO luxury.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate, address)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                  """
