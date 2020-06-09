CAFE24_INSERT =  """INSERT INTO shcpa_test.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

WCONCEPT_INSERT =  """INSERT INTO shcpa_test.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
