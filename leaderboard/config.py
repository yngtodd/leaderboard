import os
import toml

import pandas as pd
import streamlit as st


def banner():
    st.title("Pilot3 Leaderboard")


def load_config():
    files = os.listdir("config")

    if "config.toml" not in files:
        st.sidebar.text("Admin please add competition data.")
    else:
        with open("config/config.toml") as f:
            config = toml.load(f)

        competition = config['competition']
        metric = config['metric']
        idx = config['index']
        target = config['target']

        st.sidebar.subheader("Competition Details")

        st.sidebar.info(
            f"Type: {competition} "
            f"Metric: {metric} "
            f"Index column: {idx} "
            f"Target column: {target}"
        )

        return config


def load_competition_data():
    files = os.listdir("config")

    if "data.csv" not in files:
        st.sidebar.text("Admin please add competition data.")
    else:
        data = pd.read_csv(f"config/data.csv")

        return data
