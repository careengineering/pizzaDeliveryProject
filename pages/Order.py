import streamlit as st
import defForSql

products_table = "pizzas"
orders_table = "orders"
database_name = "pizzasdb.sqlite3"

defForSql.createTable(orders_table, database_name,
                      "name TEXT", "address TEXT", "product_name TEXT", "size TEXT", "drink TEXT", "price REAL")
products = defForSql.getTableWithColumns(products_table, database_name, "product_name")

products_list = []

for product in products:
    products_list.append(product[0])

with st.form("siparis", clear_on_submit=True):
    name = st.text_input("İsim Soyisim")
    address = st.text_area("Adre")
    product_name = st.selectbox("Pizza Seç", products_list)
    size = st.selectbox("Boy", ["Small", "Medium", "Large"])
    drink = st.selectbox("İçecek", ["Ayran", "Kola", "Soda", "Ice Tea"])
    order = st.form_submit_button("Siparis Ver")

    if order:
        if size == "Small":
            price = defForSql.getTableWithColumnRow(products_table, database_name,
                                                    "product_price_sm", "product_name", product_name)

        elif size == "Medium":
            price = defForSql.getTableWithColumnRow(products_table, database_name,
                                                    "product_price_md", "product_name", product_name)

        elif size == "Large":
            price = defForSql.getTableWithColumnRow(products_table, database_name,
                                                    "product_price_lg", "product_name", product_name)
        st.write(price)

        drinks = {
            "Ayran": 15.0,
            "Soda": 10.0,
            "Kola": 20.0,
            "Ice Tea": 25.0
        }

        drink_price = drinks.get(drink)
        st.write(drink_price)
        sum = price + drink_price

        st.write(sum)
