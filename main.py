# Python 3.10.1

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

TicketType = ["One adult", "One child", "One senior", "Family ticket", "Groups of six (per person)"]
TicketTypeOneDay = [20, 12, 16, 60, 15]
TicketTypeTwoDays = [30, 18, 24, 90, 22.50]

def TicketPrices():
    for i in range(len(Days) - 1):
        print(TicketTypeOneDay[i])

    for i in range(len(Days) - 1):
        print(TicketTypeTwoDays[i])

TicketPrices()