import streamlit as st
import defForSql

st.title("Katalog")

products_table = "pizzas"
database_name = "pizzasdb.sqlite3"

pizzas=defForSql.getTable(products_table,database_name)

for pizza in pizzas:

    col1,col2,col3 = st.columns(3)

    with col1:
        st.image(pizza[5])

    with col2:
        st.subheader(pizza[0])
        st.write(pizza[4])

    with col3:
        st.write("Small", pizza[1]," TL")
        st.write("Medium", pizza[2], " TL")
        st.write("Large", pizza[3], " TL")