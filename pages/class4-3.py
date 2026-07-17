import os
import streamlit as st
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        "蘋果": {"price": 10, "image": "apple.png", "stock": 10},
        "香蕉": {"price": 10, "image": "banana.png", "stock": 10},
        "橘子": {"price": 10, "image": "orange.png", "stock": 10},
        "背景圖片": {"price": 10, "image": "bg.png", "stock": 10},
    }
st.set_page_config(layout="wide")
st.header("購物平台")
cols = st.columns(len(st.session_state.inventory))
for idx, (item_name, item_info) in enumerate(st.session_state.inventory.items()):
    with cols[idx]:
        buy_qty = st.number_input(f"數量 ({item_name})", min_value=0, max_value=item_info["stock"], value=0, key=f"input_{item_name}")
        img_path = os.path.join("image", item_info["image"])
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.image("https://placeholder.com", use_container_width=True)
        st.subheader(item_name)
        st.write(f"價格: {item_info['price']} 元")
        st.write(f"庫存: {item_info['stock']} 件")
        if st.button(f"購買 {item_name}", key=f"btn_{item_name}"):
            if buy_qty > 0:
                st.session_state.inventory[item_name]["stock"] -= buy_qty
                st.success(f"成功購買 {item_name} {buy_qty} 件！")
                st.rerun()
            else:
                st.warning("請先在上方輸入購買數量")
st.markdown("---")
st.header("庫存清單")
selected_item = st.text_input("選擇商品", value="", key="stock_input")
restock_qty = st.number_input("捕貨數量", min_value=0, value=0, step=1, key="stock_qty")
if st.button("確認補貨", key="btn_restock"):
    item_name_cleaned = selected_item.strip()
    if not item_name_cleaned:
        st.error("請輸入商品名稱")
    elif item_name_cleaned not in st.session_state.inventory:
        st.error(f"找不到名為「{item_name_cleaned}」的商品，請確認名稱是否正確")
    elif restock_qty <= 0:
        st.warning("請輸入大於 0 的補貨數量")
    else:
        st.session_state.inventory[item_name_cleaned]["stock"] += restock_qty
        st.success(f"已成功為 {item_name_cleaned} 補貨 {restock_qty} 件！")
        st.rerun()
st.markdown("### 目前商品庫存：")
for item_name, item_info in st.session_state.inventory.items():
    st.write(f"{item_name} {item_info['stock']} 件")