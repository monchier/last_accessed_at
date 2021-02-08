import streamlit as st
import pandas as pd
import altair as alt
from dateutil.parser import parse
import datetime

one_week_ago = datetime.date.today() - datetime.timedelta(days=7)

with open("last_accessed_at.txt", "r") as f:
    ts = [[parse(y) for y in x.strip().split("|")] for x in f.readlines()]
data = [[None,]*len(ts), [None,]*len(ts)]
for i, row in enumerate(ts):
    data[0][i] = row[0]
    data[1][i] = row[1]
df = pd.DataFrame(ts, columns=["created_at", "last_accessed_at"])
df = df.reset_index()
#st.write(df)
line = alt.Chart(pd.DataFrame({'y': [str(one_week_ago)]})).mark_rule().encode(y='y:T')
chart = alt.Chart(df).mark_circle().encode(
    x="created_at:T",
    y="last_accessed_at:T"
)

st.altair_chart(chart + line, use_container_width=True)

all_apps = df.count()
#df_count = df[df['last_accessed_at'] < "2021-1-29 12:00:00 PM"]
df_count = df[df['last_accessed_at'] < str(one_week_ago)]
old_apps = df_count.count()


st.write(f"Old means that they have not been accessed for a week ({one_week_ago})")
st.write("Old apps:", old_apps)
st.write("Fraction of old apps:", old_apps / all_apps)
