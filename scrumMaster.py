from datetime import datetime, timedelta

sprin_start = datetime(2025, 1, 6)
sprint_length_days = 14

Sprint_end = sprin_start + timedelta(days=sprint_length_days)

today = datetime.now()
days_remaining = (Sprint_end - today).days

if days_remaining > 0:
    print(f"There are {days_remaining} days left in the sprint!")
else:
    print("The sprint has ended. Timefor a retrospective")
    