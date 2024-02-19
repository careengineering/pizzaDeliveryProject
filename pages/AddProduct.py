import streamlit as st
import defForSql

products_table = "pizzas"
database_name = "pizzasdb.sqlite3"

defForSql.createTable(products_table, database_name,
                      "product_name TEXT", "product_price_sm REAL", "product_price_md REAL",
                      "product_price_lg REAL", "product_ingredients TEXT", "product_picture TEXT")

st.header("Pizza Ekle")

with st.form("addpizza", clear_on_submit=True):  # pizza eklendikten sonra alanları sıfırlar
    product_name = st.text_input("Pizza İsmi")
    product_price_sm = st.number_input("Small Fiyat")
    product_price_md = st.number_input("Medium Fiyat")
    product_price_lg = st.number_input("Large Fiyat")
    product_ingredients = st.multiselect("İçindekiler", ["Mantar", "Jambon", "Pastırma", "Zeytin",
                                                         "Mozeralla", "Ton Balığı", "Ananas", "Fesleğen",
                                                         "Salam", "Sucuk"])

    product_picture = st.file_uploader("Pizza resmi ekleyiniz")

    btn_add_product = st.form_submit_button("Pizza Ekle")

    if btn_add_product:
        product_ingredients = ", ".join(product_ingredients)

        product_picture_url = "img/" + product_picture.name

        open(product_picture_url, "wb").write(product_picture.read())

        defForSql.insertTable(products_table, database_name, product_name, product_price_sm, product_price_md,
                              product_price_lg, product_ingredients, product_picture_url)

        st.success(f"{product_name} isimli pizza başarıyla eklendi")
