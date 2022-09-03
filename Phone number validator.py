from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier
from phonenumbers import timezone


def isPhoneNumber(number):
    rslt = []
    phonenumber = phonenumbers.parse(number)
    if phonenumbers.is_valid_number(phonenumber):
        description = geocoder.description_for_number(phonenumber, "en")
        name = carrier.name_for_number(phonenumber, "en")
        time = timezone.time_zones_for_number(phonenumber)
        rslt.append(description)
        rslt.append(name)
        rslt.append(time[0])
        return rslt

    else:
        return False

run = True


def quitprogram():
    global run
    choice = input("Enter (q) to quit or any key to continue: ")
    if choice.lower() == "q":
        run = False
        print("Good Bye..")
        input()

while run:
    try:
        number = input("Enter Phone Number With Country Code\n")
        rslt = isPhoneNumber(number)

        if rslt:
            [country, provider, time] = rslt

            print("Country :", country)
            print("Carrier :", provider)
            print("Timezone :", time)
            print()

            quitprogram()


        else:
            print("Invalid Phone Number!")

            quitprogram()

    except:
        print("Invalid Phone Number!")

        quitprogram()
