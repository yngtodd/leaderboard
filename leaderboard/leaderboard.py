import os

import numpy as np
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff

from datetime import datetime


def show_leaderboard():
    if not os.path.isfile('leaderboard.csv'):
        st.text("No submissions yet")
    else:
        board, density = get_leaderboard()

        st.dataframe(
            board.style.highlight_max(axis=0)
        )

        st.plotly_chart(density, use_container_width=True)


def get_leaderboard(greater_is_better=True):
    """Get the current leaderboard

    Args:
        greater_is_better: determines whether scores
        should be sorted in ascending or descending order.
        If the best score is something to be maximized, like
        accuracy, this should be True. Otherwise, the better
        models minimize their score.
    """
    try:
        board = pd.read_csv("leaderboard.csv", header=None)
    except:
        board = pd.DataFrame()

    board.columns = ["Username", "Score", "Submission Time"]
    board["counter"] = 1

    density_fig = score_density(board)

    board = board.groupby("Username").agg(
        {"Score": "max", "counter": "count", "Submission Time": "max"}
    )

    board = board.sort_values("Score", ascending=not greater_is_better)

    board = board.reset_index()
    board.columns = ["Username", "Score", "Entries", "Last"]

    board["Last"] = board["Last"].map(
        lambda x: relative_time(datetime.now() - datetime.strptime(x, "%Y%m%d_%H%M%S"))
    )

    return board, density_fig


def score_density(leaderboard):
    """Create a density esitmate figure for each user

    It will be useful to keep track of how much each user's score's
    vary over time. This will give us a density estimate for each
    user's scores.
    """
    board = leaderboard.drop(['Submission Time', 'counter'], axis=1)
    user_data = [x for _, x in board.groupby('Username')]

    users = []
    scores = []
    for user in user_data:
        if check_density_ok(user):
            users.append(
                user["Username"].iloc[0]
            )

            scores.append(
                user["Score"]
            )

    fig = ff.create_distplot(
        scores, users
    )

    return fig


def is_unique(scores):
    """Check if all scores are the same

    If all the scores are the same, then our density
    estimate for that user's scores will fail. This
    adds a check to see if we should include a user's
    scores in the density estimate.
    """
    scores = scores.to_numpy()
    return (scores[0] == scores).all()


def check_density_ok(user_data):
    """Make sure we can plot a density estimate

    Two conditions are needed to plot a user's score
    density estimate: there must be more than one
    submission and not all submission scores can be the
    same. This is a helper function to check those two
    conditions.
    """
    more_than_one_score = len(user_data["Score"]) > 1
    unique = is_unique(user_data["Score"])
    return more_than_one_score and not unique


def relative_time(time_diff):
    """Get the relative time between submissions

    Args:
        time_diff: the difference between two datetime
        times.
    """
    days, seconds = time_diff.days, time_diff.seconds

    if days > 0:
        return f"{days}d"
    else:
        hours = time_diff.seconds // 3600
        minutes = time_diff.seconds // 60
        if hours > 0:
            return f"{hours}h"
        elif minutes > 0:
            return f"{minutes}m"
        else:
            return f"{seconds}s"
