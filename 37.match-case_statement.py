# Match- case statement(switch): An altenative to using many 'elif' statements
#                                execute some code if a  value matches a  'case'
#                                Benefits: cleaner and syntax is more readable


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "It is Invalidy"
print(day_of_week(2))


def is_weekemd(day):
    match day:
        case "Sunday":
            return "It is Sunday"
        case "Monday":
            return "It is Monday"
        case "Tuesday":
            return "It is Tuesday"
        case "Wednesday":
            return "It is Wednesday"
        case "Thursday":
            return "It is Thursday"
        case "Friday":
            return "It is Friday"
        case "Saturday":
            return "It is Saturday"
        case _:
            return "It is Invalid"
print(is_weekemd("Sunday"))