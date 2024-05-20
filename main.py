import pandas as pd
import streamlit as st
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient


@st.cache_resource
def init_connection():
    return MongoClient(st.secrets["uri"], server_api=ServerApi("1"))


client = init_connection()
heroes = pd.DataFrame(client.crownfall.heroes.find())

tokens = [
    "jumping",
    "running",
    "floating",
    "walking",
    "ranged",
    "slithering",
    "crawling",
    "disabler",
    "teleportation",
    "flying",
    "mounted",
    "melee",
    "durable",
    "nuker",
    "initiator",
    "escape",
    "pusher",
    "healer",
]

st.title("Dota 2 Crownfall Tokens Helper")
st.write("This app helps to filter heroes by their tokens and recommended position.")
st.divider()

# Create a multiselect widget for tokens
selected_tokens = st.multiselect("Select tokens", options=tokens)

# Filter dataframe rows where at least two tokens match
result = heroes[
    heroes[["token1", "token2", "token3"]].isin(selected_tokens).sum(axis=1) >= 2
]

cols = st.columns(5)

for i in range(1, 6):
    with cols[i - 1]:
        st.subheader(f"Position {i}")
        names = result[result["position"] == i]["name"].tolist()
        for name in names:
            st.write(name)
