import streamlit as st
import pandas as pd
import altair as alt
from dateutil.parser import parse
from datetime import datetime

with open("last_accessed_at.txt", "r") as f:
    ts = [[parse(y) for y in x.strip().split("|")] for x in f.readlines()]
data = [[None,]*len(ts), [None,]*len(ts)]
for i, row in enumerate(ts):
    data[0][i] = row[0]
    data[1][i] = row[1]
df = pd.DataFrame(ts, columns=["created_at", "last_accessed_at"])
df = df.reset_index()
#st.write(df)
chart = alt.Chart(df).mark_circle().encode(
    x="created_at:T",
    y="last_accessed_at:T"
)

st.write(chart)

all_apps = df.count()
df_count = df[df['last_accessed_at'] < "2021-1-29 12:00:00 PM"]
old_apps = df_count.count()


st.write("Old means that they have not been accessed at least since the last release (2021-1-29)")
st.write("Old apps:", old_apps)
st.write("Fraction of old apps:", old_apps / all_apps)
