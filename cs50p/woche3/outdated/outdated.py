
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December"]

while True:
    try:
        date = input("Date: ").strip().title()
        if "/" in date:
            month, day, year = date.split("/")
        else:
            monthday, year = date.split(", ")
            month, day = monthday.split(" ")
            month = months.index(month) + 1
        month = int(month)
        day = int(day)
        year = int(year)

        if not 1 <= month <= 12 or not 1 <= day <= 31:
            continue

        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        pass