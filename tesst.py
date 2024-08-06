from datetime import datetime

def check_weekday_or_weekend(year, month, day):
	try:
		# Create a datetime object for the given date
		given_date = datetime(year, month, day)
		
		# Use isoweekday() to get the weekday (Monday is 1 and Sunday is 7)
		day_of_week = given_date.isoweekday() % 7 # Convert Sunday from 7 to 0
		
		# Determine if it's a weekday or a weekend
		if day_of_week < 5:
			day_type = 'weekday'
		else:
			day_type = 'weekend'
		
		# Print the result
		print(f"The day of the week for {given_date.strftime('%Y-%m-%d')} is {day_of_week} ({day_type})")
		
	except ValueError as e:
		print(f"Error: {e}")

# Example usage
year = 2023
month = 12
day = 20

check_weekday_or_weekend(year, month, day)

