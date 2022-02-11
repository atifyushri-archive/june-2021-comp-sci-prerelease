# Python 3.10.1
from tabulate import tabulate

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

TicketType = ["One adult", "One child", "One senior", "Family ticket (2 adults/senior + 3 children)", "Groups of 6 (per person)"]
TicketTypeOneDay = [20, 12, 16, 60, 15]
TicketTypeTwoDays = [30, 18, 24, 90, 22.50]

def TicketPrices():
    Data = []
    for i in range(len(Days) - 1):
        n = [TicketType[i], TicketTypeOneDay[i], TicketTypeTwoDays[i]]
        Data.append(n)
    
    print("\n", tabulate(Data , headers = ["Ticket type", "One day", "Two days"]), "\n")

TicketPrices()