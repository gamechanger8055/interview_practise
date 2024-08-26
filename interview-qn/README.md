
# Interview Qn (stage 2)

## Introduction
This project describes a real usecase we have in the SPM team, albeit simplified: Parsing changelogs.

In this folder you will find code to run a script such that we can pull change log data from a cloud provider and transform them into useful, in-memory representations.

We ultimately want
1. The type of activity that occurred
2. A snapshot of the latest attributes belonging to the target resource
3. Timestamp of the target resource

## Prerequisites
- Python > 3.8 set up
- venv installed

### File structure
```bash
src
  | lib
    | clients.py
    | entities.py
    | parsers.py
  | tests
    | lib
      | clients_test.py
      | parsers_test.py
  | main.py
```


## Setup

1. Activate venv

In current directory:
```
python -m venv .
source ./bin/activate
pip install -r requirements.txt
```

2. Tests
In current directory:
```
cd src
pytest
```
If pytest fails, run 
```
export PYTHONPATH=.
```
and run the command again.

3. Running the script
```
# while in src
python main.py
```
Before the interview start, you would see something like
```
Traceback (most recent call last):
  File "main.py", line 23, in <module>
    assert activity_logs is not None
AssertionError
```
This is ok. No further action is required.


## Post Interview
```
deactivate
```
