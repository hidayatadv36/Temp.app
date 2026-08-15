
import streamlit as st

normal_temp = 90
high_temp = 100
very_high_temp = 103

temp = st.number_input("Enter temperature", value=106)

if temp <= normal_temp:
    st.success("Temp is normal")
elif temp >= very_high_temp:
    st.error("Temp is extremely high")
elif temp >= high_temp:
    st.warning("Temp is high")
else:
    st.warning("Warning")
