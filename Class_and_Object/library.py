class Book:
    def __init__(self, book_name, auther_name, volume, year, lot_size):
        self.book_name= book_name
        self.auther_name= auther_name
        self.volume= volume
        self.year= year
        self.lot_size= lot_size
    def display(self):
        print("Name of Book : ", self.book_name)
        print("Name of Auther : ", self.auther_name)
        print("Volume of Book : ", self.volume)
        print("Year of Book publish : ", self.year)
        print("Lot of Book : ", self.lot_size)
book1= Book("Python", "Shashi kumar", "1st", "2020", 2)
book2= Book("Python2", "Shashi kumar", "2nd", "2021", 1)
book3= Book("Python3", "Shashi kumar", "3rd", "2022", 2)
book4= Book("Python4", "Shashi kumar", "4th", "2023", 2)
book5= Book("Python5", "Shashi kumar", "5th", "2024", 2)
book1.display()
book2.display()
book3.display()
book4.display()
book5.display()



   
