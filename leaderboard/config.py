import os
import json
import toml

import pandas as pd
import streamlit as st


def banner():
    st.title("Pilot3 Leaderboard")


def load_competition_data():
    files = os.listdir("competition")

    if "data.csv" not in files or "config.json" not in files:
        st.sidebar.text("Admin please add competition data.")
    else:
        data = pd.read_csv("competition/data.csv")
        with open("competition/config.toml") as f:
            config = toml.load(f)

        competition = config['competition_type']
        metric = config['metric_type']
        idx = config['index']
        target = config['target']

        st.sidebar.subheader("Competition Details")
        #st.balloons()

        st.sidebar.info(
            f"Type: {competition} "
            f"Metric: {metric} "
            f"Index column: {idx} "
            f"Target column: {target}"
        )

        return data, config


