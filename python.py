import datetime
yourBirthYear=int(input("Give your Birth Year:"))
yourBirthMonth=int(input("Give your Birth Month:"))
yourBirthDay=int(input("Give your Birth Date:"))

years=datetime.datetime.now().year - yourBirthYear
months=datetime.datetime.now().month - yourBirthMonth
days=datetime.datetime.now().day - yourBirthDay

print("You are {} Year {} Month and {} Day old".format(years,months,days))
