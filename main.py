# Python 3.10.1
from random import randint
import numpy
from tabulate import tabulate

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

TicketType = ["One adult", "One child", "One senior", "Family ticket (2 adults/senior + 3 children)", "Groups of 6 (per person)"]
TicketTypeOneDay = [20, 12, 16, 60, 15]
TicketTypeTwoDays = [30, 18, 24, 90, 22.50]

AttractionType = ["Lion feeding", "Penguin feeding", "Evening barbeque (Two days only)"]
AttractionPrice = [2.5, 2, 5]

def TicketPrices():
    # Reorganised price data into 2D arrays
    Data = []
    for i in range(5):
        n = [i + 1, TicketType[i], TicketTypeOneDay[i], TicketTypeTwoDays[i]]
        Data.append(n)
    
    print("\n", tabulate(Data , headers = ["Input number", "Ticket type", "One day", "Two days"]), "\n")

    # Reorganised attraction price data into 2D arrays
    Data = []
    for i in range(len(AttractionType)):
        n = [i + 1, AttractionType[i], AttractionPrice[i]]
        Data.append(n)

    print("\n", tabulate(Data, headers = ["Input number", "Extra attractions", "Cost per person"]), "\n")
    
    # Days reorgs
    Data = []
    for i in range(len(Days)):
        n = [i + 1, Days[i]]
        Data.append(n)

    print("\n", tabulate(Data, headers = ["No", "Days available"]), "\n")

TicketPrices()

def TicketBooking():
    NumDays = int(input("Please input the number of days (1/2): "))

    AttractionTickets = []

    # Gets inputs from user
    while True:
        Adults = int(input("Please input the number of adults: "))
        Children = int(input("Please input the number of children: "))
        Elders = int(input("Please input the number of elders: "))
        if Children < 2 * Adults:
            break
        else:
            print("Not enough adults for children. Please retry.")

    Total = 0
    SixOrMoreTotal = 0
    FamilyTotal = 0
    NormalTotal = 0 

    # One-day prices
    if NumDays == 1:
        UsedListPrices = TicketTypeOneDay
    if NumDays == 2:
        UsedListPrices = TicketTypeTwoDays
    
    # Calculate "normal" ticket prices
    NormalTotal = Adults * UsedListPrices[0] + Children * UsedListPrices[1] + Elders * UsedListPrices[2]

    # Family of 2 adults/elders and 3 children (perfect family ticket type)
    if (Adults and Elders > 2) and (Children >= 3) and ((Adults + Elders) % 2 == 0) and (Children % 3 == 0):
        FamilyTotal = ((Adults + Elders + Children) / 5) * UsedListPrices[3] 

    # Family of >2 adults/elders or >3 children (imperfect family ticket type)  
    if (((Adults + Elders) % 2) != 0) or (Children % 3 != 0):
        Zeroer = lambda a: int(abs(a) + a)/2 # Lambda function returns a zero if number is negative

        # Finds the perfect number of tickets through floor division
        NumberOfPerfectTickets = 0
        if (Adults + Elders) // 2 < Children // 3:
            NumberOfPerfectTickets = int((Adults + Elders) // 2)
        else:
            NumberOfPerfectTickets = int(Children // 3)

        # Add perfect number of tickets with imperfect/standalone tickets
        # Zeroer zeroes negative values, eg. if no of elders - perfect tickets < 0, value returned is 0
        FamilyTotal = (NumberOfPerfectTickets * UsedListPrices[3]) + (Zeroer(Adults - (NumberOfPerfectTickets * 2)) * UsedListPrices[0]) + (Zeroer(Children - (NumberOfPerfectTickets * 3)) * UsedListPrices[1]) + (Zeroer(Elders - (NumberOfPerfectTickets * 2)) * UsedListPrices[2])

    # Group of six for 1 day
    if Adults + Elders + Children >= 6:
        SixOrMoreTotal = SixOrMoreTotal + (UsedListPrices[4] * (Adults + Elders + Children))

    # Codeblock for getting the best prices
    ArrayOfPrices = numpy.array([NormalTotal, FamilyTotal, SixOrMoreTotal])
    ArrayOfPrices.sort()
    ArrayOfPrices = ArrayOfPrices[ArrayOfPrices != 0]
    Total = ArrayOfPrices.min()

    # Function for attraction prices calculator 
    while True:
        AttractionsBool = input("Extra attractions? (y/n): ")
        if AttractionsBool.lower() == "n":
            break

        # Creates a 2D array of desired tickets for looping and calculating
        DummyVar = []
        DummyVar.append(int(input("Please input the desired attraction tickets: ")))
        DummyVar.append(int(input("Please input the amount wanted: ")))
        AttractionTickets.append(DummyVar)
        Finished = str(input("Finished? (y/n): "))
        if Finished.lower() == "y":
            break 
    
    AttractionTotal = 0
    # Tallies the total number of wanted attraction tickets
    if AttractionsBool == "y":
        for i in range(len(AttractionTickets)):
            AttractionTotal = AttractionTotal + (AttractionTickets[i][1] * AttractionPrice[AttractionTickets[i][0] - 1])
    
    BookingTotal = Total + AttractionTotal
    UniqueID = randint(000000, 999999)
    print("Your order ID is %s with a total of $%s." % (UniqueID, BookingTotal))

TicketBooking()