days_in_month = int(input("how many days in this month"))
starting_day = input("what day of the week (put 1st 3 letters (capital first letter) of starting letter e.g. Mon = Monday / Thu f= Thursday) in which the month starts")
count = 1

print(f" {count}   ")

print("Mon   Tue   Wed   Thu   Fri   Sat   Sun")
print("---------------------------------------")

if starting_day == "Mon":
    days_in_month_total = days_in_month + 1
    while count != (days_in_month_total):
        for _ in range(days_in_month):
            print(f" {count}", end="    ")
            count += 1
            if days_in_month == 7:
                print('')
