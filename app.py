import streamlit as st
import pandas as pd
import time
from datetime import datetime

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
df=pd.read_csv("Attendance/Attendance"+ date +".csv")        

st.dataframe(df.style.highlight_max(axis=0))
# import streamlit as st
# import pandas as pd
# import time
# from datetime import datetime
# import os

# # Get the current timestamp and format the date
# ts = time.time()
# date = datetime.fromtimestamp(ts).strftime("%d-%m-%y")
# timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# # File path for the attendance CSV
# attendance_file = f"Attendance/Attendance_{date}.csv"

# # Check if the file exists
# if os.path.isfile(attendance_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(attendance_file)
#     # Display the DataFrame with highlighted maximum values
#     st.dataframe(df.style.highlight_max(axis=0))
# else:
#     st.write("No attendance data available for today.")
