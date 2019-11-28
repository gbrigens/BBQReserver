# Testing

## Description
For usecase testing purposes, pytest module is used. 
To simulate telegram bot, ptbtest mock bot is used

There are 4 test files used to test 9 use cases scenarios based on testcase matricies
Bot functions checking:
Create reservation - test_create_reservation.py
View reservation - test_view_reservation.py
Cancel reservation - test_cancel_reservation.py
Subscribe to waiting list - test_subscribe.py
All tests passed

## Prerequisites
- virtualenv module
- pytest module

## Steps to run tests:
1. Install app using steps 1-5 on [Readme.md file](https://github.com/gbrigens/BBQReserver#steps)
2. Open the `tests` directory:
`$> cd tests`
3. Run each test file individually using command prompt:
`$> pytest test_create_reservation.py`
