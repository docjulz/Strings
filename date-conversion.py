# Date Format Program
# This program will convert a date in 00/00/000
# format into a more readible one


def main():
    # Get date from user
    date_string = input("Enter a date in the following format (00/00/0000): ")

    # Get the index of the date
    month_only = (new_date(date_string)[0])
    day_only = (new_date(date_string)[1])
    year_only = (new_date(date_string)[2])

    # Create a list holding each month
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
             'August', 'September', 'October', 'November', 'December']

    # Isolate the month gased on the index
    month_index = int(month_only)-1

    # change the numeric value of month to a string value
    new_month = month[month_index]
    print("An easier way to read",date_string)
    print("is to change its formating.")
    print('--------------------------------')
    print ("New format is: ", new_month," ", day_only, ", ", year_only, sep='')

# split the month, day and year by creating a list
def new_date(a):
    date_list = a.split('/')
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]
    
    return month,day,year


main()

# Need to create validation for year and format
