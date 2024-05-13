import streamlit as st
import pandas as pd
import json

# Load tokens from JSON file
with open('tokens.json') as f:
    tokens = json.load(f)

# Load data from CSV file
data = pd.read_csv('data.csv')

# Create a multiselect widget for tokens
selected_tokens = st.multiselect('Select tokens', options=tokens)

# Filter dataframe rows where at least two tokens match
result = data[data[['token1', 'token2', 'token3']].isin(selected_tokens).sum(axis=1) >= 2]

# Display the names as a list
st.write(result['name'].tolist())