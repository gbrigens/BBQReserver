# BBQReserver

The BBQ Reservation is a bot to replace the current system which is just a google form, which allows anyone to make modification to the spread sheet. The bot allows to avoid conflict or some else delete your reservation. The bot has this features:
1. Create reservation.
2. Cancel reservation.
3. View reservation.
4. Subcribe to waitinglist if the day and time you were planning to book has already been booked.
5. Notification : For example when you have subscribed to waiting list and the day and time is free you will be notify and you can book.

## How to install
### Requrements:
- git module
- Python 3.5 or higher
- Python virtual environment module venv

### Steps:
1) Open terminal (or command line on Windows) and clone the repository
git clone `https://github.com/gbrigens/BBQReserver.git`
2) Open the `src` directory
`cd src`
3) Create python virtual environment using venv module to install dependencies
`python3 -m venv env`
4) Activate virtual environment
On Linux: `source env/bin/activate`
On Windows: `env/scripts/activate.bat`
5) Install dependencies on requirements file `pip install -r requirements`
5) run bot `python app.py`
6) Find this bot to test it: `@testthisagain_bot`
7) If you cannot run the bot locally, you can test the bot already running: `@InnoBBQbot`

## How to test
All tests are in `/src/tests` directory, to run the tests [check test readme file](https://github.com/gbrigens/BBQReserver/blob/master/src/tests/readme.md)

# Short Video of how it works
[<img src="https://www.luceysgoodfood.com/wp-content/uploads/2016/10/bbq_meats.jpg" height=300, width=450>](https://youtu.be/8kLkf7Gp8ZI)

# Screenshots of the bot

## Start screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/start.jpg" height=600>

## Welcome screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/welcome.jpg" height=600>

## Reserve and choose month screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/choosemonth.jpg" height=600>

## Choose day screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/chooseday.jpg" height=600>

## Choose time screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/chooseday.jpg" height=600>

## Success screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/reservesuccessful.jpg" height=600>


## View reservation screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/viewreservation.jpg" height=600>

## Cancel screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/cancelresavetion.jpg" height=600>


## Cancel success screen
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/reservationcancelsuccessful.jpg" height=600>

## Subscribe to waitinglist
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/subscribetowaitlist.jpg" height=600>

## Notification of canceled date of intrest
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/notificationforfreespot.jpg" height=600>

## Notification reminder
<img src="https://github.com/gbrigens/BBQReserver/blob/master/screenshot/reminder.png" height=600>



