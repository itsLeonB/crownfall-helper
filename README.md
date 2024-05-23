# Dota 2 Crownfall Tokens Helper

This app helps to filter heroes based on needed Crownfall tokens.

## Available Features

- [x] Return Heroes based on token
- [x] Return recommended hero position
- [ ] Optimize heroes based on needed and unused token quantity

## Prerequisites

This project is built using:

- Python
- Streamlit
- MongoDB
- Pandas

## Local Deployment

1. Clone the project

2. Install dependencies

   ```sh
   pip install -r requirements
   ```

3. Make a new directory `.streamlit` and move `secrets.example.toml` there

4. Rename the file to `secrets.toml`, and edit the values inside to your own values

5. Start the server:

   ```sh
   streamlit run main.py
   ```
