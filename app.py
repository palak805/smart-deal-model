import streamlit as st
import pandas as pd

st.set_page_config(
    
    page_title="Smart Deal Model",
    page_icon="🛍️",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
data = pd.read_csv("products.csv")

# -------------------------
# Deal Score Calculation
# -------------------------
data["Deal_Score"] = (
    data["rating"] * 20
    + data["discount"] * 2
    + data["revie ws"] / 1000
    - data["price"] / 10000
)

# -------------------------
# Header
# -------------------------
st.title("🛍️ Smart Deal Model")
st.markdown(
    "### Compare prices, ratings and discounts to find the best deal."
)

st.divider()

# -------------------------
# Dashboard Statistics
# -------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Products",
        data["product_name"].nunique()
    )

with col2:
    st.metric(
        "Listings",
        len(data)
    )

with col3:
    st.metric(
        "Websites",
        data["website"].nunique()
    )

with col4:
    st.metric(
        "Categories",
        data["category"].nunique()
    )

st.divider()

# -------------------------
# Product Selection
# -------------------------
st.subheader("🔎 Find the Best Deal")

product_list = sorted(data["product_name"].unique())

selected_product = st.selectbox(
    "Select a product",
    product_list
)

product_data = data[
    data["product_name"] == selected_product
].copy()

product_data = product_data.sort_values(
    "Deal_Score",
    ascending=False
)

# -------------------------
# Best Deal
# -------------------------
best_deal = product_data.iloc[0]

st.subheader("🏆 Best Deal Recommendation")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Best Website",
        best_deal["website"]
    )

with c2:
    st.metric(
        "Best Price",
        f"₹{best_deal['price']:,.0f}"
    )

with c3:
    st.metric(
        "Rating",
        f"{best_deal['rating']} ⭐"
    )

with c4:
    st.metric(
        "Deal Score",
        f"{best_deal['Deal_Score']:.2f}"
    )

st.success(
    f"🏆 Best deal for **{selected_product}** is available on "
    f"**{best_deal['website']}**."
)

st.divider()

# -------------------------
# Website Comparison
# -------------------------
st.subheader("📊 Website Comparison")

comparison = product_data[
    [
        "website",
        "price",
        "rating",
        "revie ws",
        "discount",
        "delivery_days",
        "Deal_Score"
    ]
].copy()

comparison.columns = [
    "Website",
    "Price (₹)",
    "Rating",
    "Reviews",
    "Discount (%)",
    "Delivery (Days)",
    "Deal Score"
]

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

# -------------------------
# Price Chart
# -------------------------
st.subheader("💰 Price Comparison")

price_chart = product_data.set_index("website")["price"]

st.bar_chart(price_chart)

# -------------------------
# Deal Score Chart
# -------------------------
st.subheader("⭐ Deal Score Comparison")

score_chart = product_data.set_index("website")["Deal_Score"]

st.bar_chart(score_chart)

# -------------------------
# Complete Dataset
# -------------------------
with st.expander("📦 View Complete Dataset"):

    st.write(
        f"Showing **{len(data)} listings** "
        f"for **{data['product_name'].nunique()} products**."
    )

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

# -------------------------
# Footer
# -------------------------
st.divider()

st.caption(
    "Smart Deal Model | Python • Pandas • Streamlit | "
    "Machine Learning Project"
)