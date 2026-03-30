import sqlite3
import pandas as pd

# STEP 1: Connect
conn = sqlite3.connect('data.sqlite')

# STEP 2
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees;
""", conn)

# STEP 3
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
ORDER BY employeeNumber DESC;
""", conn)

# STEP 4
df_alias = pd.read_sql("""
SELECT employeeNumber AS ID, lastName
FROM employees;
""", conn)

# STEP 5
df_executive = pd.read_sql("""
SELECT employeeNumber, lastName,
CASE 
    WHEN employeeNumber > 1500 THEN 'Executive'
    ELSE 'Not Executive'
END AS role
FROM employees;
""", conn)

# STEP 6
df_name_length = pd.read_sql("""
SELECT lastName,
LENGTH(lastName) AS name_length
FROM employees;
""", conn)

# STEP 7
df_short_title = pd.read_sql("""
SELECT jobTitle,
SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees;
""", conn)

# STEP 8
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(quantityOrdered * priceEach)) AS total_price
FROM orderdetails;
""", conn).iloc[:, 0]

# STEP 9
df_day_month_year = pd.read_sql("""
SELECT 
'06' AS day,
'01' AS month,
'2000' AS year
FROM employees;
""", conn)