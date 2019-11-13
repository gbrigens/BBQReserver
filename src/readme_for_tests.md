For unit testing purposes, pytest module is used. 
To simulate telegram bot, ptbtest mock bot is used

There are 5 test files used to test 9 use cases and bot functions which are the following:
Bot functions checking:
Create reservation - test2_create_reservation.py
	Choose reservation menu
	Choose month
	Choose day
	Choose slot
View reservation - test3_view_reservation.py
Cancel reservation - test4_cancel_reservation.py

Database functions checking:
Update the User table - test1_create_user.py
Create reservation row - test2_create_reservation.py
Delete reservation row - test5_delete_reservation.py

To run tests:
1. Build virtual environment
2. Install dependencies from requirements.txt file
3. Run each test file individually using command prompt:
$>pytest test3_create_reservation.py


Using tests some bugs identified:
- You can choose day 31 for november, however it isn't saved to database
- Some usecases are not implemented
