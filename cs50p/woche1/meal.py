# breakfast 7-8am, 
# lunch 12-1pm, 
# dinner 6-7pm
#if it´s not time to eat, then output nothing
# 24hours time not 12hours as "#:##" or "##:##"
#For instance, whether it´s 7:00, 7:01, 7:59 or 8:00, or anytime between, it´s time for breakfast

def main():
    meal_time = convert(input("What time is it?"))
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")

def convert(meal_time):
    hours, minutes = meal_time.split(":")
    return int(hours) + int(minutes) / 60

main()