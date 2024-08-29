import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Initialize session state variables
if 'employees' not in st.session_state:
    st.session_state.employees = []
if 'attendance' not in st.session_state:
    st.session_state.attendance = {}

def add_employee():
    new_employee = st.session_state.new_employee.strip()
    if new_employee and new_employee not in st.session_state.employees:
        st.session_state.employees.append(new_employee)
        st.session_state.new_employee = ""

def record_attendance():
    date = st.session_state.date
    for employee in st.session_state.employees:
        status = st.session_state[f'status_{employee}']
        if date not in st.session_state.attendance:
            st.session_state.attendance[date] = {}
        st.session_state.attendance[date][employee] = status

def get_summary(date):
    if date in st.session_state.attendance:
        summary = {'In Office': 0, 'On Leave': 0, 'Travel': 0, 'WFH': 0}
        for status in st.session_state.attendance[date].values():
            summary[status] += 1
        return summary
    return None

st.title("Attendance Management System")

# Add employee section
st.header("Add Employees")
st.text_input("Enter employee name", key="new_employee")
st.button("Add Employee", on_click=add_employee)

# Display current employees
st.write("Current Employees:", ", ".join(st.session_state.employees))

# Record attendance section
st.header("Record Attendance")
st.date_input("Select Date", key="date")

for employee in st.session_state.employees:
    st.selectbox(
        f"Status for {employee}",
        ["In Office", "On Leave", "Travel", "WFH"],
        key=f'status_{employee}'
    )

st.button("Record Attendance", on_click=record_attendance)

# Summary section
st.header("Attendance Summary")
summary_date = st.date_input("Select Date for Summary")
summary = get_summary(summary_date)

if summary:
    st.write(f"Summary for {summary_date}:")
    for status, count in summary.items():
        st.write(f"{status}: {count}")
else:
    st.write("No attendance data for the selected date.")

# Display full attendance record
st.header("Full Attendance Record")
if st.session_state.attendance:
    df = pd.DataFrame.from_dict({(i,j): st.session_state.attendance[i][j] 
                                 for i in st.session_state.attendance.keys() 
                                 for j in st.session_state.attendance[i].keys()},
                                 orient='index', columns=['Status'])
    df.index.names = ['Date', 'Employee']
    df = df.reset_index()
    st.dataframe(df)
else:
    st.write("No attendance records yet.")
Last edited just now
