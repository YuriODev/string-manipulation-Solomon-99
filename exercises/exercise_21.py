date = input()

month, day, year = date[0:2], date[3:5], date[6:]

if int(month) == 1:
    month = "January"

elif int(month) == 2:
    month = "February"

elif int(month) == 3:
    month = "March"

elif int(month) == 4:
    month = "April"

elif int(month) == 5:
    month = "May"

elif int(month) == 6:
    month = "June"

elif int(month) == 7:
    month = "July"

elif int(month) == 8:
    month = "August"

elif int(month) == 9:
    month = "September"

elif int(month) == 10:
    month = "October"

elif int(month) == 11:
    month = "November"

elif int(month) == 12:
    month = "December"

print(f"{month} {day}, {year}")