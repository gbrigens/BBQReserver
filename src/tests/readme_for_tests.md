For usecase testing purposes, pytest module is used. 
To simulate telegram bot, ptbtest mock bot is used

There are 4 test files used to test 9 use cases scenarios based on testcase matricies
Bot functions checking:
Create reservation - test_create_reservation.py
View reservation - test_view_reservation.py
Cancel reservation - test_cancel_reservation.py
Subscribe to waiting list - test_ubscribe.py

To run tests:
1. Build virtual environment with name "env"
2. Install dependencies from requirements file
3. Run each test file individually using command prompt:
$>pytest test_create_reservation.py

All tests passed