<h1>Leaderboard<img src='https://github.com/yngtodd/leaderboard/blob/main/img/snek.png' align='right' width='180' height='104'></h1>


**Note**: This project is an alpha phase, proof of concept leaderboard! There are no 
guard rails here.


### Concepts

The leaderboard is modeled after those found on Kaggle competitions. It holds onto a 
fixed test set where the labels are unknown to users. This is stored as a `.csv` file 
with a unique index column and a label column. Separate from this API, users have 
access to the test data upon which their trained models can make predictions. This is 
important to note, the leaderboard does not store any of the test data! Only the labels 
and indices in the test set are stored, and so this can be used inside and outside of the 
enclave.

Predictions should be saved as a `.csv` file that matches the one stored in the leaderboard.
Typically, leaderboard admins provide a sample submission with random predictions so 
that users can inspect the shape of the expected submission and check that the index
column entries match those of the test set they are predicting on. 


### Current Design

The leaderboard runs locally. The test set labels and all submissions are stored on the
file system as `.csv` files, and there is no authentication of users. This means anyone can
make a submission on anyone else's name (see what I mean by no guard rails?). This can
be resolved by using a database and user authentication on the website. Beyond this alpha
proof of concept, this would be necessary.

Binary classification is currently supported. Adding multitask classification would be a simple
addition with the caveat that we would need to decide how to compare two models when they differ
in performance across the tasks.


### Next Steps

Setting up a simple database like `sqlite` and user authentication would mean that we could 
host this site via GitHub or GitLab.


### Usage

```
streamlit run leaderboard/app.py
```

#### Features

Leaderboard comes with a built in command line interface:

```python
python -m leaderboard.cli greet
```
