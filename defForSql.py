import sqlite3


def createTable(table_name, database_name, *columns):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    columns = str(columns)
    columns = columns.replace('"', '')
    columns = columns.replace("'", "")
    sql_command = f"CREATE TABLE IF NOT EXISTS {table_name} {columns}"
    c.execute(sql_command)
    conn.commit()


def insertTable(table_name, database_name, *datas):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    mock_values = ["?"] * len(datas)
    mock_values = ",".join(mock_values)
    sql_command = f"INSERT INTO {table_name} VALUES ({mock_values})"
    c.execute(sql_command, datas)
    conn.commit()


def getTable(table_name, database_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    sql_command = f"SELECT * FROM {table_name}"
    c.execute(sql_command)
    return c.fetchall()


def getTableWithColumns(table_name, database_name, *columns):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    columns = ",".join(columns)
    sql_command = f"SELECT {columns} FROM {table_name}"
    c.execute(sql_command)
    return c.fetchall()


def getTableWithColumnRow(table_name, database_name, price_column, product_name_column, row_value):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    sql_command = f"SELECT {price_column} FROM {table_name} WHERE {product_name_column}={row_value}"
    c.execute(sql_command)
    price = c.fetchone()
    return price
