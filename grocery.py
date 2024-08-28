import streamlit as st

# Define the grocery function
def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return disc_amt, tax

# Set the title of the app
st.title("Grocery Discount and Tax Calculator")

# Add a description
st.markdown("""
This app calculates the discount and tax for your grocery order based on the amount you enter. 
- **Discount**: 25% if the order amount is more than $200
- **Tax**: 7% on the amount after applying the discount

Enter your order amount below to get the discount and tax information.
""")

# Input for the order value
order_value = st.number_input("Enter your order value", min_value=0.0, format="%.2f")

# Calculate discount and tax
disc_amt, tax = grocery(order_value)

# Display the results
st.write(f"**Discount Amount:** ${disc_amt:.2f}")
st.write(f"**Tax Amount:** ${tax:.2f}")
