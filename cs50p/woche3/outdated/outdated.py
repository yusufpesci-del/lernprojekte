
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December"]
months.index("January")+1

while True:
    try:
        month, day, year = input("Date: ").split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if not 1 <= month <= 12 or not 1 <= day <= 31:
            continue
        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        pass