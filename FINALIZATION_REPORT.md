# Finalization report

## Newly Implemented Usecase
- We implemented request confirmation (ID: RC-10). The bot sends requests to a user to confirm upcoming reservation.
- We implemented the waiting list feature (ID: NR-21). Users who subscribe to be on a waiting list for a particular day when slots are filled, get a notification when a user cancels their reservation for that day.
- We added the notification functionality which was absent in the MVP (ID: SN-20). With this new features, users receive a notification 12 hours prior to their reservation whether they would still be available or not and users on the waiting list also recieve a notification.

## Modifications
- Changed hardcode values to dynamic values for month, days in a month and time slot
- Create Reservation and Cancel Reservation were completely rewritten due to the logical inconsistencies and defect
- We made the bot persistent which means that the user operation would not be affected if the bot restarts
- We added navigation buttons for back and cancel 
- We fixed other minor bugs discovered

## Changes to usecase based on client request
- We removed the 3 reservation  for a week and 12 reservations for a month in the usecase 
- We allowed users to pick any day within two months ahead based as well to not limit the user to just the present day, tomorrow, and the day after tomorrow



