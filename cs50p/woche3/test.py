
months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]

date = "September 8, 1636"

monthday, year = date.split(", ")
month, day = monthday.split(" ")

month = months.index(month) + 1

print(month)
print(day)


