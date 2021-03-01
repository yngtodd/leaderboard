import pandas as pd
import streamlit as st

from pathlib import Path
from datetime import datetime

from sklearn.metrics import (
    accuracy_score, auc, f1_score, precision_score, recall_score
)


SCORE_FUNCTIONS = {
    "Accuracy": accuracy_score,
    "Precision": precision_score,
    "Recall": recall_score,
    "Auc": auc,
    "F1": f1_score,
}


def submit(username, data, config):
    uploaded_file = st.file_uploader(
        "Upload Submission CSV File", type="csv"
    )

    if st.button("Submit"):
        if uploaded_file is None:
            st.text("Please upload your predictions to submitted.")
        else:
            submission = pd.read_csv(uploaded_file)
            submission_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            submission_file = f"{username}_{submission_time}.csv"
            path = Path(config["submission_directory"]).joinpath(submission_file)

            idx, target = config["index"], config["target"]
            submission[[idx, target]].to_csv(path, index=False)

            score = compute_score(submission, data, config)
            update_leaderboard(username, score, submission_time)


def compute_score(submission, data, config):
    """"""
    idx = config["index"]
    target = config["target"]
    metric = SCORE_FUNCTIONS[config["metric"]]

    data = data.merge(submission, how="left", on=idx)

    score = metric(
        data[f"{target}_x"], data[f"{target}_y"]
    )

    st.balloons()
    st.info(f"Your submission score: {score:.5f}")

    return score


def update_leaderboard(username, score, submission_time):
    with open("leaderboard.csv", "a+") as f:
        f.write(f"{username},{score},{submission_time}\n")
