# Python 3.10.1
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
        n = [TicketType[i], TicketTypeOneDay[i], TicketTypeTwoDays[i]]
        Data.append(n)
    
    print("\n", tabulate(Data , headers = ["Ticket type", "One day", "Two days"]), "\n")

    # Reorganised attraction price data into 2D arrays
    Data = []
    for i in range(len(AttractionPrice) - 1):
        n = [AttractionType[i], AttractionPrice[i]]
        Data.append(n)

    print("\n", tabulate(Data, headers = ["Extra attractions", "Cost per person"]), "\n")
    
    # Days reorgs
    Data = []
    for i in range(len(Days) - 1):
        n = [i + 1, Days[i]]
        Data.append(n)

    print("\n", tabulate(Data, headers = ["No", "Days available"]), "\n")

TicketPrices()

def TicketBooking():
    PurchaseTickets = []
    while True:
        PurchaseTickets.append(input("Please enter desired ticket for purchase: ")) 
        Finished = input("Finished? Y/N :")
        if Finished.lower() == "y":
            break
    
    AttractionTickets = []
    while True:
        AttractionTickets.append(input("Please enter desired attractions for purchase: "))
        Finished = input("Finished? Y/N :")
        if Finished.lower() == "y":
            break

TicketBooking()