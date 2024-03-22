from plyer import notification
import time

while True:
    print("Attempting to show notification...")  # Debugging message
    notification.notify(
        title='REMINDER- 100DaysOfCode',
        message='Did you do your Code Sessions Today?',
        app_name='DAILY WORK REMINDER',
        timeout=20
    )
    time.sleep(28800)

