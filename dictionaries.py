#Building DIctionaries

month_conversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
    0     : "Number zero",
    1     : "Number one"

    }

keyword = input("Enter a month key word: ")
value_of_key = month_conversion[keyword]
print(value_of_key)

keyword = float(input("Enter a number key word: "))
value_of_key = month_conversion[keyword]
print(value_of_key)


