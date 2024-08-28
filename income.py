import streamlit as st

# Set the title of the app
st.title("Income Classification")

# Add a detailed description
st.markdown("""
This application helps you determine your income classification based on the amount you input. 
The classification categories are as follows:
- **High income**: More than $8000
- **Medium high income**: Between $4000 and $8000
- **Medium income**: Between $2000 and $4000
- **Medium low income**: Between $1000 and $2000
- **Low income**: $1000 or less

Simply enter your income in the input box below or select a predefined income range to see which category you fall into.
""")

# Dropdown menu for predefined income ranges
options = [
    "Select an income range",
    "Less than $1000",
    "$1000 - $2000",
    "$2000 - $4000",
    "$4000 - $8000",
    "More than $8000"
]
selected_option = st.selectbox("Select a predefined income range", options)

# Input for the income
if selected_option == "Select an income range":
    income = st.number_input("Enter your income", step=1)
else:
    # Extract income value from the selected option
    if selected_option == "Less than $1000":
        income = 999
    elif selected_option == "$1000 - $2000":
        income = (1000 + 2000) / 2
    elif selected_option == "$2000 - $4000":
        income = (2000 + 4000) / 2
    elif selected_option == "$4000 - $8000":
        income = (4000 + 8000) / 2
    elif selected_option == "More than $8000":
        income = 8001

# Determine the income classification
if income > 8000:
    result = "High income"
elif income > 4000:
    result = "Medium high income"
elif income > 2000:
    result = "Medium income"
elif income > 1000:
    result = "Medium low income"
else:
    result = "Low income"

# Display the result
st.write(f"**Your income classification is:** {result}")

# Add average salary for Singapore
st.markdown("""
### Average Salary Information

The average salary in Singapore is approximately **SGD $4,800 per month**. This figure provides a reference point for comparing your income classification.
""")

# Add some custom styling to ensure consistent font sizes
st.markdown("""
<style>
    .css-1d391kg { font-size: 16px; }
    .css-2tr6yl { font-size: 16px; }
</style>
""", unsafe_allow_html=True)
