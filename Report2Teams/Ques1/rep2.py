
import time
import schedule
from plyer import notification


def send_break_alert(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )
    except Exception as error:
        print(f"Notification error: {error}")


def hydration_alert():
    send_break_alert(
        "Hydration Alert",
        "Drink some water and stay hydrated!"
    )


def posture_alert():
    send_break_alert(
        "Posture Check",
        "Sit straight and relax your shoulders."
    )


def main():
    schedule.every(10).seconds.do(hydration_alert)
    schedule.every(20).seconds.do(posture_alert)

    print("Ergonomic Reminder Utility is running.")
    print("Hydration reminder: every 10 seconds (testing).")
    print("Posture reminder: every 20 seconds.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nReminder utility stopped safely. Take care!")


if __name__ == "__main__":
    main()