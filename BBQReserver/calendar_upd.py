#
#
# from datetime import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# sched = BlockingScheduler()
#
# sched.start()
#
# DEF_MONTHS = [['January', 'February', 'March'],
#               ['April', 'May', 'June'],
#               ['July', 'August', 'September'],
#               ['October', 'November', 'December']]
#
# DEF_DAYS = [['1', '2', '3', '4', '5', '6', '7'],
#             ['8', '9', '10', '11', '12', '13', '14'],
#             ['15', '16', '17', '18', '19', '20', '21'],
#             ['22', '23', '24', '25', '26', '27', '28'],
#             ['29', '30', '31']]
#
# MONTHS = []
# DAYS = []
#
#
# def change_calendar():
#     today = datetime.today()
#     MONTHS = DEF_MONTHS
#     i = 0
#     while i < int(today.month) / 3:
#         MONTHS.pop(0)
#         i += 1
#     i = 0
#     while i < int(today.month - 1) % 3:
#         MONTHS[0].pop(0)
#         i += 1
#     DAYS = DEF_DAYS
#     while i < int(today.day) / 7:
#         DAYS.pop(0)
#         i += 1
#     while int(today.day) < int(DAYS[0]):
#         MONTHS[0].pop(0)
#     tomorrow = datetime.today()+ datetime.timedelta(days=1)
#     tomorrow.hour = 0
#     tomorrow.minute = 0
#     tomorrow.second = 0
#     sched.add_job(change_calendar(), next_run_time=tomorrow)
#
# change_calendar()