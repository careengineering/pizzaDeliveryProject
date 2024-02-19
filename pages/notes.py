product_name = st.text_input("Pizza İsmi")
product_price_sm = st.number_input("Small Fiyat")
product_price_md = st.number_input("Medium Fiyat")
product_price_lg = st.number_input("Large Fiyat")
product_ingredients = st.multiselect("İçindekiler", ["Mantar", "Jambon", "Pastırma", "Zeytin",
                                                     "Mozeralla", "Ton Balığı", "Ananas", "Fesleğen",
                                                     "Salam", "Sucuk"])