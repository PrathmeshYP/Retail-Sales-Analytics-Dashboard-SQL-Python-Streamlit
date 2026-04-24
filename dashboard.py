import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

conn = sqlite3.connect("sales.db")

st.title("📊 Retail Sales Dashboard")

# KPI
kpi_query = """
SELECT 
    SUM(quantity * price) AS revenue,
    COUNT(DISTINCT order_id) AS orders,
    SUM(quantity * price) * 1.0 / COUNT(DISTINCT order_id) AS aov
FROM sales;
"""
kpi = pd.read_sql(kpi_query, conn)

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"₹{int(kpi['revenue'][0]):,}")
col2.metric("Orders", int(kpi['orders'][0]))
col3.metric("AOV", f"₹{int(kpi['aov'][0]):,}")

# Trend
trend_query = """
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY month
ORDER BY month;
"""
df_trend = pd.read_sql(trend_query, conn)

fig = px.line(df_trend, x="month", y="revenue", title="Monthly Revenue")
st.plotly_chart(fig, use_container_width=True)

# Filter
regions = pd.read_sql("SELECT DISTINCT region FROM sales", conn)
selected_region = st.selectbox("Select Region", regions['region'])

region_query = """
SELECT product, SUM(quantity * price) AS revenue
FROM sales
WHERE region = ?
GROUP BY product
ORDER BY revenue DESC;
"""

df_region = pd.read_sql(region_query, conn, params=(selected_region,))

fig2 = px.bar(df_region, x="revenue", y="product", orientation="h",
              title=f"Top Products in {selected_region}")

st.plotly_chart(fig2, use_container_width=True)

conn.close()