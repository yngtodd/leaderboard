import pandas as pd

from datetime import datetime


def get_leaderboard(greater_is_better=True):
    """Get the current leaderboard

    Args:
        greater_is_better: determines whether scores
        should be sorted in ascending or descending order.
        If the best score is something to be maximized, like
        accuracy, this should be True. Otherwise, the better
        models minimize their score.
    """
    board = pd.read_csv("leaderboard.csv", header=None)
    board.columns = ["Username", "Score", "Submission Time"]
    board["counter"] = 1

    board = board.groupby("Username").agg(
        {"Score": "max", "counter": "count", "Submission Time": "max"}
    )

    board = board.sort_values("Score", ascending=not greater_is_better)

    board = board.reset_index()
    board.columns = ["Username", "Score", "Entries", "Last"]

    board["Last"] = board["Last"].map(
        lambda x: relative_time(datetime.now() - datetime.strptime(x, "%Y%m%d_%H%M%S"))
    )

    return board


def relative_time(time_diff):
    """Get the relative time between submissions

    Args:
        time_diff: the difference between two datetime
        times.
    """
    days, seconds = time_diff.days, time_diff.senconds

    if days > 0:
        return f"{days}d"
    else:
        hours = time_diff.seconds // 3600
        mins = time_diff.seconds // 60
        if hours > 0:
            return f"{hours}h"
        elif minutes > 0:
            return f"{mins}m"
        else:
            return f"{seconds}s"


