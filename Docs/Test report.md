##
# Test Report



- Work done in this iteration:

1. Derived test cases from use cases
  1. Identified decision points in each use case
  2. Created a decision trees for each use case
  3. Created a test case for each path
2. Fixed the found defects:
  1. Restricted reservations for past dates
  2. Fixed bug with repeated error message
  3. Added button &quot;Report violation&quot;
3. [Documented the final solution](https://github.com/gbrigens/BBQReserver/blob/master/Docs/User%20Documentation.pdf) for the product owner

- [Use cases with annotated decision points](https://github.com/gbrigens/BBQReserver/blob/master/Docs/Use%20cases.md)
- Test cases with execution results
  - Create reservation
  - Cancel reservation
  - View reservation
  - Test case values
- Test case matrices
- Interaction test cases matrices

## [Instruction to run tests](https://github.com/gbrigens/BBQReserver/blob/master/src/tests/readme.md)


**Test cases with execution results**

**Use Case:** [Create reservation](https://github.com/gbrigens/BBQReserver/blob/master/Docs/Use%20cases.md#create-reservation)

**Test :** [Create reservation](https://github.com/gbrigens/BBQReserver/blob/master/src/tests/test_create_reservation.py)

**Decision tree**

 <img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/test_decision_tree1.png">

| **Test Case name:** | Create reservation - **success** |
| --- | --- |
| **Test ID:** | **TC-01** |
| **Test suite:** | **Create Reservation** |
| **Priority:** | High |
| **Setup:** | John Doe has a reservation Intent for 25th November 10 AM. |
| **Teardown:** | Remove the confirmed reservation for John Doe from the system. |
| **Step** | **Description** | **Result** | **Problem** |
| **TC-01-A1** | John Doe  selects option to create new reservation | **Pass** |   |
| **TC-01-S2** | Telegram bot responds by providing a list of months from November to December. | **Pass** |   |
| **TC-01-A3** | John Doe responds by selecting November | **Pass** |   |
| **TC-01-S4** | The telegram bot in turn provides a list of days from 24th to 30th for the remaining days of November so John Doe can select. | **Pass** |   |
| **TC-01-A5** | John Doe selects 25th from the list | **Pass** |   |
| **TC-01-S6** | The telegram bot presents John Doe with the list of clock time from 8 AM to 10 PM in the interval of 2 hours for the 25th of November. | **Warning** | This serves as a warning as it is possible that John Doe already made a reservation on this day. |
| **TC-01-A7** | John Doe selects 10:00 AM from the list. | **Pass** |   |
| **TC-01-S8** | The telegram bot display the message&quot;Time 2019-11-25 10:00 Reserved Successfully&quot; | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | E. Timoshchuk |
| **Date Complete:** | 25th November 2019 |



| **Test Case name:** | Create Reservation - **failure** |
| --- | --- |
| **Test ID:** | **TC-02** |
| **Test suite:** | **Create Reservation** |
| **Priority:** | High |
| **Setup:** | John Doe has a reservation intent for 25th November which he has already booked a slot for. |
| **Teardown:** | Bot returns to main menu. |
| **Step** | **Description** | **Result** | **Problem ID** |
| **TC-02-A1** | John Doe  selects option to create new reservation. | **Pass** |   |
| **TC-02-S2** | Telegram bot responds by providing a list of months from November to December. | **Pass** |   |
| **TC-02-A3** | John Doe responds by selecting November. | **Pass** |   |
| **TC-02-S4** | The telegram bot in turn provides a list of days from 24th to 30th for the remaining days of November so John Doe can select. | **Pass** |   |
| **TC-02-A5** | John Doe selects 25th from the list. | **Pass** |   |
| **TC-02-S6** | The telegram bot presents John Doe with the list of clock time from 8 AM to 10 PM in the interval of 2 hours for the 25th of November. | **Warning** | This serves as a warning as it is possible that John Doe already made a reservation on this day. |
| **TC-02-S7** | The telegram bot display the message&quot;You already have reservation on 2019-11-25, you should cancel previous reservation if you want to change.&quot; | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | S. Kuznetsov |
| **Date Complete:** | 25th November 2019 |



| **Test Case name:** | Create Reservation - **failure** |
| --- | --- |
| **Test ID:** | **TC-03** |
| **Test suite:** | **Create Reservation** |
| **Priority:** |   |
| **Setup:** | John Doe has a reservation intent for 25th November which he has already booked a slot for. |
| **Teardown:** | Bot returns to main menu. |
| **Step** | **Description** | **Result** | **Problem** |
| **TC-03-A1** | John Doe  selects option to create new reservation. | **Pass** |   |
| **TC-03-S2** | Telegram bot responds by providing a list of months from November to December. | **Pass** |   |
| **TC-03-A3** | John Doe responds by selecting November. | **Pass** |   |
| **TC-03-S4** | The telegram bot in turn provides a list of days from 24th to 30th for the remaining days of November so John Doe can select. | **Pass** |   |
| **TC-03-A5** | John Doe selects 25th from the list. | **Warning** | This serves as a warning as it is possible that John Doe already made a reservation on this day. |
| **TC-03-S6** | The bot notices there are no slots for 25th December so it present option to John Doe to subscribe to waiting list. | **Pass** |   |
| **TC-03-A7** | John Doe selects the Subscribe option. | **Pass** |   |
| **TC-03-S8** | Bot subscribes John Doe to waiting list so as to notify him if there is any slot made available for 25th December. | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | E. Timoshchuk |
| **Date Complete:** | 25th November 2019 |

**Use Case:** [Cancel reservation](https://github.com/gbrigens/BBQReserver/blob/master/Docs/Use%20cases.md#cancel-reservation)

**Test:** [Cancel reservation](https://github.com/gbrigens/BBQReserver/blob/master/src/tests/test_cancel_reservation.py)

**Decision tree**

<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/test_decision_tree2.png">

| **Test Case name:** | Cancel Reservation - **Success** |
| --- | --- |
| **Test ID:** | **TC-04** |
| **Test suite:** | **Cancel Reservation** |
| **Priority:** | High |
| **Setup:** | John Doe has a reservation booked for 25th November 10 AM |
| **Teardown:** | Remove Reservation for John Doe from the system |
| **Step** | **Description** | **Result** | **Problem ID** |
| **TC-04-A1** | John Doe selects option to cancel reservation. | **Pass** |   |
| **TC-04-S2** | The telegram bot presents John Doe with a list of his reservation as this:&quot; ID:12 Time: 2019-11-25 10:00&quot;And presents him with option to &quot;12&quot; as the id of the reservation he wants to cancel | **Pass** |   |
| **TC-04-A3** | John Doe selects the id 12. | **Pass** |   |
| **TC-04-S4** | Telegram bot displays &quot;Reservation Successfully Cancelled&quot; | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | Z. Usmonov |
| **Date Complete:** | 25th November 2019 |

| **Test Case name:** | Cancel Reservation Failure |
| --- | --- |
| **Test ID:** | **TC-05** |
| **Test suite:** | **Cancel Reservation** |
| **Priority:** | high |
| **Setup:** | John Doe has not booked any Reservation in the past. |
| **Teardown:** | Telegram bot returns to Home menu |
| **Step** | **Description** | **Result** | **Problem ID** |
| **TC-05-A1** | John Doe selects option to cancel reservation. | **Pass** |   |
| **TC-05-S2** | Telegram bot displays the message &quot;You have not made any reservation&quot; | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | S. Kuznetsov |
| **Date Complete:** | 25th November 2019 |

**Use Case:** [View reservation](https://github.com/gbrigens/BBQReserver/blob/master/Docs/Use%20cases.md#view-reservation)

**Test:** [View](https://github.com/gbrigens/BBQReserver/blob/master/src/tests/test_view_reservation.py)[reservation](https://github.com/gbrigens/BBQReserver/blob/master/src/tests/test_view_reservation.py)

**Decision tree**

 <img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/test_decision_tree3.png">

| **Test Case name:** | View Reservation Successful |
| --- | --- |
| **Test ID:** | **TC-06** |
| **Test suite:** | **View Reservation** |
| **Priority:** | High |
| **Setup:** | John Doe has made two reservations for 25th November and 1 December previously. |
| **Teardown:** | Telegram bot returns to the home menu. |
| **Step** | **Description** | **Result** | **Problem ID** |
| **TC-06-A1** | John Doe selects the option to view existing reservations. | **Pass** |   |
| **TC-06-S2** | The telegram bot displays the message &quot;You have made the following reservations ID:12 Time:2019-11-25 10:00ID:14 Time:2019-12-1 18:00&quot; | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | E. Timoshchuk |
| **Date Complete:** | 25th November 2019 |



| **Test Case name:** | View Reservation Failure |
| --- | --- |
| **Test ID:** | **TC-07** |
| **Test suite:** | **View Reservation** |
| **Priority:** | Medium |
| **Setup:** | John Doe has made no reservation from the system |
| **Teardown:** | Telegram bot returns to home menu |
| **Step** | **Description** | **Result** | **Problem ID** |
| **TC-07-A1** | John Doe selects option to view existing reservation | **Pass** |   |
| **TC-07-S2** | Telegram bot displays the message &quot; You have not made any reservations yet&quot; | **Pass** |   |
| **Status:** | Pass |
| **Tester:** | Z. Usmonov |
| **Date Complete:** | 25th November 2019 |



**Test case values**

| **TC-01** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to create reservations | 🖊 Reserve | Select month | Select month |
| Select month | November | Select day | Select day |
| Select day | 25 | Select hour | Select hour |
| Select hour | 10:00 | Reservation created successfully | Reservation created successfully |

| **TC-02** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to create reservations | 🖊 Reserve | Select month | Select month |
| Select month | November | Select day | Select day |
| Select day | 25 | Select hour | Select hour |
| Select hour | 10:00 | Reservation created successfully | &#39;You already have reservation on 2019-11-25, you should cancel previous reservation if you want to change.&#39; |

|   **TC-03** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to create reservations | **🖊 Reserve** | Select month | Select month |
| Select month | November | Select day | Select day |
| Select day | 25 | Select hour | Select hour |
| Select hour | 10:00 | Reservation created successfully | &#39;Bot subscribes John Doe to waiting list so as to notify him is there is any slot made available for 25th December.&#39; |

|   **TC-04** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to cancel reservations | **🗑 Cancel reservation** | Choose the reservation ID you want to cancel: | Choose the reservation ID you want to cancel: |
| Select Reservation Id to cancel | 12 | Reservation successfully cancelled | Reservation successfully cancelled |

|   **TC-05** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to cancel reservations | **🗑 Cancel reservation** | Choose the reservation ID you want to cancel: | You have not made any  reservations yet |

|   **TC-06** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to view reservations | **📖 View reservations** | The telegram bot displays the message &quot; You have made the following reservations ID:12 Time:2019-11-25 10:00ID:14 Time:2019-12-1 18:00&quot; | The telegram bot displays the message &quot; You have made the following reservations ID:12 Time:2019-11-25 10:00ID:14 Time:2019-12-1 18:00&quot; |

|   **TC-07** | **Value** | **Expected results** | **Obtained results** |
| --- | --- | --- | --- |
| Select command to view reservations | **📖 View reservations** | The telegram bot displays the message &quot; You have made the following reservations ID:12 Time:2019-11-25 10:00ID:14 Time:2019-12-1 18:00&quot; | Telegram bot displays the message &quot; You have not made any reservations yet&quot; |



**Test case matrices**

|   | **TC01** | **TC02** | **TC03** | **TC04** | **TC04** | **TC05** | **TC06** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Reserve command** | **🖊 Reserve** | **🖊 Reserve** | **🖊 Reserve** | **🖊 Reserve** |   |   |   |
| **View reservation command** |   |   |   | ** ** |    |   | **📖 View reservations** |
| **Cancel reservation command** |   |   |   |   | **🗑 Cancel reservation** | **🗑 Cancel reservation** |   |
| **Month** | **Correct** | **Correct** | **Correct** | **Incorrect** |   |   |   |
| **Date** | **Correct** | **Correct** | **Incorrect** |   |   |   |   |
| **Hour** | **Correct** | **Incorrect** |   |   |   |   |   |
| **Reservation Id** |   |   |   |   | **Correct** | **Incorrect** |   |

**Test case interaction matrices**

|   | **Create reservation** | **Cancel reservation** | **View reservation** | **Delete Data** | **Send message** | **Request confirmation** | **Send list of reservations** | **Update the database** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Create reservation** |   | RC - Cancel reservation after creation | RC - View reservation after creation |   |   |   |   |   |
| **Cancel reservation** |   |   | RD-List of reservations |   |   |   |   |   |
| **View reservation** |   | RD - view reservation |   |   |   |   |   | RC-Read or identify user id |
| **Delete Data** |   |   |   |   |   |   |   |   |
| **Send message** |   |   |   |   |   |   |   |   |
| **Request confirmation** |   | RD-Delete user reservation |   |   |   |   |   |   |
| **Send list of reservations** |   |   |   |   |   |   |   |   |
| **Update the database** |   |   |   |   |   |   |   |   |