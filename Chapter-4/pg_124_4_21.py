y = eval(input('Enter year: (e.g., 2008): '))
m = eval(input('Enter month: 1-12: '))
q = eval(input('Enter the day of the month: 1-31: '))

# January and February are counted as months 13 and 14 of the previous year
if m == 1 or m == 1:
    m += 12
    y -= 1

j = int(y / 100)
k = y % 100

h = (q + ((26 * (m + 1)) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7

if int(h) == 0:
    day = 'Saturday'
elif int(h) == 1:
    day = 'Sunday'
elif int(h) == 2:
    day = 'Monday'
elif int(h) == 3:
    day = 'Tuesday'
elif int(h) == 4:
    day = 'Wednesday'
elif int(h) == 5:
    day = 'Thursday'
else:
    day = 'Friday'

print('Day of the week is', day)

# h = (q + ((26 * (m + 1)) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7
# h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday,
#                          5: Thursday, 6: Friday).
# q is the day of the month.
# m is the month (3: March, 4: April, ..., 12: December).
#  January and February are counted as months 13 and 14 of the previous year.
# j is the century (i.e., year / 100).
# k is the year of the century (i.e., year % 100).
