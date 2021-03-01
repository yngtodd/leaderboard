from login import user_login
from submission import submit
from leaderboard import show_leaderboard

from config import (
    banner, load_competition_data
)


def main():
    banner()
    user = user_login()
    data, config = load_competition_data()
    submit(user, data, config)
    show_leaderboard()


if __name__=="__main__":
    main()
