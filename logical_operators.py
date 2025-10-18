#logical operators = evaluate multiple conditions(or, and, not)

#   or = at least one condition must be true
#   and = both the conditions need to be true
#   not = inverts the condition (not False, not True)

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is sunny🌞")
elif temp <= 0 and is_sunny:
    print("It is Cold outside 🥶")
    print("It is sunny🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm outside 😊")
    print("It is sunny🌞")

elif temp >= 28 and not is_sunny:
    print("It is Hot outside 🥵")
    print("It is cloudy☁️")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside 🥶")
    print("It is cloudy☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm outside 😊")
    print("It is cloudy☁️")

