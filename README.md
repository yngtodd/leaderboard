<h1>Leaderboard<img src='https://github.com/yngtodd/leaderboard/blob/main/img/snek.png' align='right' width='180' height='104'></h1>


A prototype leaderboard for Pilot3.

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

#### Features

Leaderboard comes with a built in command line interface:

```python
python -m leaderboard.cli greet
```
