import streamlit as st
import pandas as pd

st.set_page_config(page_title="VMA App", page_icon="📊", layout="wide")

st.title("📊 VMA - Value Market Analysis")
st.markdown("**Welcome Owner! Your app is LIVE!**")

# Sidebar
st.sidebar.header("Controls")
symbol = st.sidebar.text_input("Stock Symbol", "AAPL")
period = st.sidebar.selectbox("Period", ["1M", "3M", "6M", "1Y"])

# Main
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Price", "$185.20", "+2.3%")
with col2:
    st.metric("Value Score", "8.5/10", "+0.5")
with col3:
    st.metric("Market Cap", "$2.8T", "↑")

st.divider()

st.subheader(f"Analysis for {symbol} - {period}")

data = {
    "Metric": ["P/E Ratio", "ROE", "Debt/Equity", "Dividend Yield", "Growth"],
    "Value": [28.5, "26%", "1.2", "0.5%", "15%"],
    "Status": ["✅ Good", "✅ Excellent", "⚠️ Medium", "❌ Low", "✅ High"]
}
df = pd.DataFrame(data)
st.table(df)

st.bar_chart({"Value": [28, 26, 12, 5, 15]})

st.success("✅ VMA Analysis Complete!")

if st.button("Generate Report"):
    st.balloons()
    st.write("📄 Report Generated for " + symbol)
