from login import user_login
from config import (
    banner, load_competition_data
)


def main():
    banner()
    user_login()
    load_competition_data()



if __name__=="__main__":
    main()
