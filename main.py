import streamlit as st

# Function to convert American to Decimal
def to_decimal(american):
    if american > 0:
        return (american / 100) + 1
    return (100 / abs(american)) + 1

# Page Config & Styling
st.set_page_config(page_title="Hedgley", page_icon="📈")

# Custom CSS for a "Sportsbook" feel
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🦔 Hedgley The Hedging Calculator")
st.write("Put your current wager amount and the odds. Then type the odds for the bet you're using to hedge.")

st.divider()

# Input Section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Existing bet")
    w1 = st.number_input("Original Wager ($)", value=100.0, step=10.0)
    a1 = st.number_input("Original Odds (American)", value=250, help="e.g., +250 or -110")

with col2:
    st.subheader("Hedge opportunity")
    a2 = st.number_input("Hedge Odds (American)", value=-150, help="The current market odds for the opposing side")

# Backend Logic
d1 = to_decimal(a1)
d2 = to_decimal(a2)

# Goal: Payout of Hedge (w2 * d2) must equal Payout of Original (w1 * d1)
total_payout = w1 * d1
w2 = total_payout / d2
total_invested = w1 + w2
net_profit = total_payout - total_invested
roi = (net_profit / total_invested) * 100

st.divider()

# Results Section
st.subheader("Strategy Summary")
res_col1, res_col2, res_col3 = st.columns(3)

res_col1.metric("Hedge Wager", f"${w2:.2f}")
res_col2.metric("Net Profit", f"${net_profit:.2f}")
res_col3.metric("ROI", f"{roi:.2f}%")

if net_profit > 0:
	st.success(f"✅ Cash it! You've been #HedgleyBlessed 🦔")
else:
    st.warning("⚠️😡 Spines out! Based on your existing bet, the market's current odds won't help you guarantee a profit with a hedge.")

# Visualizing the Outcomes
with st.expander("See Outcome Breakdown"):
    st.write(f"**Outcome A (Original Wins):** You receive ${total_payout:.2f} minus ${total_invested:.2f} total cost.")
    st.write(f"**Outcome B (Hedge Wins):** You receive ${w2 * d2:.2f} minus ${total_invested:.2f} total cost.")