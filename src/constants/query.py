CAFE24_INSERT =  """INSERT IGNORE INTO luxury.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

CAFE24_TWO_INSERT ="""
                    INSERT INTO gangnamapt.hince_orders_history (YYYYMMDD, PAYMENT_SITE, ORDER_NO, ON_OFF_DIFF, COUNTRY_CD, PRD_CD, PRD_NM, CUST_ID, ORDER_STATUS, ORDER_DTTM, PAYMENT_DTTM, DELIV_DTTM, CONFIRM_DTTM, REFUND_DTTM, EXCHANGE_DTTM, RETURN_DTTM, CANCEL_DTTM, PRICE, AMT, TOTAL_ORDER_AMT, SELLER_DUTY_DISCOUNT, TOTAL_DISCOUNT, USE_POINT, DELIV_FEE, TOTAL_PAYMENT_AMT, REFUND_AMT, ZIP_CD, ADDRESS, DELIV_FIRM, INVOICE, PG, CREATE_DTTM, UPDATE_DTTM)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

WCONCEPT_INSERT =  """INSERT IGNORE INTO luxury.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

NAVER_STOREFARM_INSERT =  """INSERT IGNORE INTO luxury.orders(channel, orderNumber, productName, productPrice, quantity, shippingFee, totalPrice, paidPrice, orderDate, paidDate, shippedDate, refundedDate, address)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                  """

###
# create table if not exists hince_orders_history
# (
# 	YYYYMMDD varchar(8) not null comment '기준일자',
# 	PAYMENT_SITE varchar(10) not null comment '결제사이트',
# 	ORDER_NO varchar(20) not null comment '주문번호',
# 	ON_OFF_DIFF varchar(10) not null comment '온오프구분',
# 	COUNTRY_CD varchar(10) not null comment '국가구분',
# 	PRD_CD varchar(20) not null comment '상품코드',
# 	PRD_NM varchar(50) not null comment '상품명',
# 	CUST_ID varchar(20) null comment '고객번호',
# 	ORDER_STATUS varchar(10) null comment '주문상태',
# 	ORDER_DTTM datetime null comment '주문일시',
# 	PAYMENT_DTTM datetime null comment '결제일시',
# 	DELIV_DTTM datetime null comment '배송완료일',
# 	CONFIRM_DTTM datetime null comment '구매확정일',
# 	REFUND_DTTM datetime null comment '환불완료일',
# 	EXCHANGE_DTTM datetime null comment '교환일자',
# 	RETURN_DTTM datetime null comment '반품일자',
# 	CANCEL_DTTM datetime null comment '취소일자',
# 	PRICE int null comment '판매가',
# 	AMT int null comment '수량',
# 	TOTAL_ORDER_AMT int null comment '총주문금액',
# 	SELLER_DUTY_DISCOUNT int null comment '판매자부담할인액',
# 	TOTAL_DISCOUNT int null comment '전체할인액',
# 	USE_POINT int null comment '적립금액',
# 	DELIV_FEE int null comment '총배송비',
# 	TOTAL_PAYMENT_AMT int null comment '총결제금액',
# 	REFUND_AMT int null comment '환불금액',
# 	ZIP_CD varchar(10) null comment '우편번호',
# 	ADDRESS varchar(50) null comment '수령주소',
# 	DELIV_FIRM varchar(20) null comment '택배사',
# 	INVOICE varchar(20) null comment '송장번호',
# 	PG varchar(10) null comment 'PG사',
# 	CREATE_DTTM datetime null comment '생성일자',
# 	UPDATE_DTTM datetime null comment '변경일자'
# );
###