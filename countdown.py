import datetime

def countdown(start_date, end_date):
  """Calculates the amount of time between two dates.

  Args:
    start_date: The start date.
    end_date: The end date.

  Returns:
    The amount of time between the two dates, in days.
  """

  start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
  end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")

  difference = end_datetime - start_datetime

  return difference.days

def main():
  start_date = "2023-06-24"
  end_date = "2023-07-01"

  days_until_event = countdown(start_date, end_date)

  print(f"There are {days_until_event} days until the event.")

if __name__ == "__main__":
  main()
