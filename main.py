# Python 3.10.1
from ast import Num
from tabulate import tabulate

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

TicketType = ["One adult", "One child", "One senior", "Family ticket (2 adults/senior + 3 children)", "Groups of 6 (per person)"]
TicketTypeOneDay = [20, 12, 16, 60, 15]
TicketTypeTwoDays = [30, 18, 24, 90, 22.50]

AttractionType = ["Lion feeding", "Penguin feeding", "Evening barbeque (Two days only)"]
AttractionPrice = [2.5, 2, 5]

def TicketPrices():
    # Reorganised price data into 2D arrays
    Data = []
    for i in range(len(Days) - 1):
        n = [i + 1, TicketType[i], TicketTypeOneDay[i], TicketTypeTwoDays[i]]
        Data.append(n)
    
    print("\n", tabulate(Data , headers = ["Input number", "Ticket type", "One day", "Two days"]), "\n")

    # Reorganised attraction price data into 2D arrays
    Data = []
    for i in range(len(AttractionPrice)):
        n = [i + 1, AttractionType[i], AttractionPrice[i]]
        Data.append(n)

    print("\n", tabulate(Data, headers = ["Input number", "Extra attractions", "Cost per person"]), "\n")
    
    # Days reorgs
    Data = []
    for i in range(len(Days) - 1):
        n = [i + 1, Days[i]]
        Data.append(n)

    print("\n", tabulate(Data, headers = ["No", "Days available"]), "\n")

TicketPrices()

def TicketBooking():
    NumDays = int(input("Please input the number of days (1/2): "))

    PurchaseTickets = []
    while True:
        DummyVar = []
        DummyVar.append(int(input("Please input the desired ticket type: ")))
        DummyVar.append(int(input("Please input the amount: ")))
        PurchaseTickets.append(DummyVar)
        Finished = str(input("Finished? (y/n): "))
        if Finished.lower() == "y":
            break 

    Total = 0 
    if NumDays == 1:
        for i in range(len(PurchaseTickets)):
            Total = Total + (PurchaseTickets[i][1] * TicketTypeOneDay[PurchaseTickets[i][0] - 1])
            print(Total)

    elif NumDays == 2:
        for i in range(len(PurchaseTickets)):
            Total = Total + (PurchaseTickets[i][1] * TicketTypeTwoDays[PurchaseTickets[i][0] - 1])
            print(Total)

    

            
TicketBooking()
