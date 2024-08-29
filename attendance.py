import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Initialize session state
if 'attendance' not in st.session_state:
    st.session_state.attendance = {}

if 'employees' not in st.session_state:
    st.session_state.employees = set()

# App title
st.title("Attendance Management App")

# Add new employee
new_employee = st.text_input("Add new employee")
if st.button("Add Employee"):
    if new_employee and new_employee not in st.session_state.employees:
        st.session_state.employees.add(new_employee)
        st.success(f"Added {new_employee} to the employee list.")
    elif new_employee in st.session_state.employees:
        st.warning(f"{new_employee} is already in the employee list.")
    else:
        st.warning("Please enter an employee name.")

# Display current employee list
st.subheader("Current Employees")
st.write(", ".join(sorted(st.session_state.employees)))

# Date selection
selected_date = st.date_input("Select Date", datetime.now().date())

# Attendance input
st.subheader("Attendance Input")
for employee in sorted(st.session_state.employees):
    status = st.selectbox(
        f"Status for {employee}",
        ("", "In Office", "On Leave", "Travel", "WFH"),
        key=f"{employee}_{selected_date}"
    )
    if status:
        if selected_date not in st.session_state.attendance:
            st.session_state.attendance[selected_date] = {}
        st.session_state.attendance[selected_date][employee] = status

# Submit attendance
if st.button("Submit Attendance"):
    if selected_date in st.session_state.attendance:
        if len(st.session_state.attendance[selected_date]) == len(st.session_state.employees):
            st.success("Attendance submitted successfully for all employees.")
        else:
            missing = set(st.session_state.employees) - set(st.session_state.attendance[selected_date].keys())
            st.warning(f"Attendance not submitted for: {', '.join(missing)}")
    else:
        st.warning("No attendance data entered for this date.")

# Attendance summary
st.subheader("Attendance Summary")
summary_date = st.date_input("Select Date for Summary", datetime.now().date())

if summary_date in st.session_state.attendance:
    summary = {
        "In Office": 0,
        "On Leave": 0,
        "Travel": 0,
        "WFH": 0
    }
    for status in st.session_state.attendance[summary_date].values():
        summary[status] += 1
    
    st.write(f"Summary for {summary_date}:")
    for status, count in summary.items():
        st.write(f"{status}: {count}")
else:
    st.write("No attendance data available for the selected date.")

# Display full attendance record
st.subheader("Full Attendance Record")
if st.session_state.attendance:
    data = []
    for date, records in st.session_state.attendance.items():
        for employee, status in records.items():
            data.append({"Date": date, "Employee": employee, "Status": status})
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.write("No attendance records available.")
