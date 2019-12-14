INSERT INTO  tblRegister(ID, PWD, NAME, NUM1, NUM2, EMAIL, 
PHONE, ZIPCODE, ADDRESS, JOB)VALUES('rorod', '1234', '이경미', 
'123456', '1234567', 'rorod@jspstudy.co.kr', '010-5555-7680', '1234', 
'부산 연제구', '프로그래머');

CREATE TABLE tblRegister(
id           VARCHAR(20)  PRIMARY KEY NOT NULL,
pwd         VARCHAR(20) NOT NULL,
name        CHAR(6) NULL,
num1       CHAR(6) NULL,
num2       CHAR(7) NULL,
email       VARCHAR(30) NULL,
phone       VARCHAR(30) NULL,
zipcode     CHAR(5) NULL,
address     VARCHAR(60) NULL,
job         VARCHAR(30) NULL
)collation='utf8_general_ci';