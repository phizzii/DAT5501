from pyparsing import col

days_in_month = int(input("how many days in this month"))
starting_day = input("what day of the week (put 1st 3 letters (capital first letter) of starting letter e.g. Mon = Monday / Thu f= Thursday) in which the month starts")
col_width = 5

weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

print(''.join(w.center(col_width) for w in weekdays))
print('-' * (col_width * 7))

start_index = weekdays.index(starting_day)

print(' ' * (col_width * start_index), end='')

day = 1 # as count instead
day_of_the_week = start_index

while day <= days_in_month:
    print(f"{day:>{col_width}}", end='')
    day += 1
    day_of_the_week += 1

    if day_of_the_week % 7 == 0:
        print()
        day_of_the_week = 0

print()




#if starting_day == "Mon":
 #   days_in_month_total = days_in_month + 1
  #  while count != (days_in_month_total):
   #     for _ in range(days_in_month):
    #        print(f" {count}", end="    ")
     #       count += 1
      #      if days_in_month == 7:
       #         print('')