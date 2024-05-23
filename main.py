import json
import pandas as pd
import streamlit as st
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient


# Load tokens from JSON file
with open("hero_tokens/act1.json") as f:
    tokens_act1 = json.load(f)
with open("hero_tokens/act2.json") as f:
    tokens_act2 = json.load(f)


@st.cache_resource
def get_heroes_data():
    client = MongoClient(st.secrets["uri"], server_api=ServerApi("1"))
    return pd.DataFrame(client.crownfall.heroes.find())


heroes = get_heroes_data()

st.title("Dota 2 Crownfall Tokens Helper")
st.write("This app helps to filter heroes by their tokens and recommended position.")

act1, act2 = st.tabs(["Act 1 - Midgate", "Act 2 - Druud"])


def token_selector(tokens: list[str], act: int):
    selected_tokens = st.multiselect("Select tokens", options=tokens)
    token_list = ["token1", "token2", "token3"]
    token_list = [f"{act}{token}" for token in token_list]
    result = heroes[heroes[token_list].isin(selected_tokens).sum(axis=1) >= 2]

    cols = st.columns(5)

    for i in range(1, 6):
        with cols[i - 1]:
            st.subheader(f"Position {i}")
            names = result[result["position"] == i]["name"].tolist()
            for name in names:
                st.write(name)


with act1:
    token_selector(tokens_act1, 1)

with act2:
    token_selector(tokens_act2, 2)
