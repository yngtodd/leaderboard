from login import user_login
from submission import submit
from leaderboard import show_leaderboard

from config import (
    banner, load_competition_data, load_config
)


def main():
    banner()
    user = user_login()
    config = load_config()
    data = load_competition_data()
    submit(user, data, config)
    show_leaderboard()


if __name__=="__main__":
    main()
