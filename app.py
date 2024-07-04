import streamlit as st

st.set_page_config(
    page_title="Investing in Real Estate vs Stocks",
    layout="wide",
    page_icon="💸"
)

st.title("Investing in Real Estate vs Stocks")



st.write("## Stocks")
col1, col2, col3, col4 = st.columns(4)
stock_initial_investment = col1.number_input(label = "Initial Investment", min_value = 0, step = 10000, key = "stocks_initial_investment")
stock_avg_growth = col2.number_input(label = "Average Annual Growth Rate (%)", step = 0.1, key = "stocks_avg_growth_rate", )
stock_horizon = col3.number_input(label = "Investment Horizon (in years)", min_value = 0, step = 1, key="stocks_investment_horizon")
stock_withdrawl_tax = col4.number_input(label = "Withdrawl Tax (%)", min_value = 0, step = 1, key="percent_tax_withdrawl")

st.write("## Real Estate")
col1, col2, col3, col4, col5 = st.columns(5)
real_estate_value = col1.number_input(label = "Value", min_value = 0, step = 10000, key = "real_estate_initial_investment")
real_estate_deposit = col2.number_input(label="Deposit", step = 10000, key = "real_estate_deposit")
real_estate_growth = col3.number_input(label = "Average Annual Growth Rate (%)", step = 0.1, key = "real_estate_avg_growth_rate" )
real_estate_horizon = col4.number_input(label = "Investment Horizon (in years)", min_value = 0, step = 1, key = "real_estate_investment_horizon")
real_estate_maintenence = col5.number_input(label = "Maintenance Costs (per year)", min_value = 0, step = 100, key = "maintenance_cost")


# Calculate stock price increase
# stock_avg_growth / 100
# stock_withdrawl_tax / 100
stock_price_before_tax = stock_initial_investment * ((1 + (stock_avg_growth/100)) ** stock_horizon)
tax_amount = stock_price_before_tax * (stock_withdrawl_tax/100)
stock_price_after_tax = stock_price_before_tax - tax_amount

st.write("### Stock Value")
col1, col2, col3 = st.columns(3)
col1.metric(label = "Before Tax", value = f"${stock_price_before_tax:,.0f}")
col2.metric(label = "Tax Amount", value = f"${tax_amount:,.0f}")
col3.metric(label = "After Tax", value = f"${stock_price_after_tax:,.0f}")

