class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def gatStatus(self):
        print(f"The name of the Train is {self.name}")
        print(f"The seats available in the Train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print( f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full")

    def cancelTicket(self, seatNo):
        seatNo = int(input("Enter your seat no: "))
        self.seatNo = seatNo
        print("Your ticket is cancled secssesfully")
        self.seats = self.seats + 1


intercity = Train("Intercity Express: 14015", 90, 1)
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.gatStatus()
intercity.cancelTicket(1)
intercity.gatStatus()
