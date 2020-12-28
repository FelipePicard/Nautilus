# name, point, age, nationality, board size, championships won

class Contestant(): #creates a class and defines the attributes of each object that belongs to the class
    def __init__(self, name, points, age, nationality, boardsize, cwon): 
        self.name = name
        self.points = points
        self.age = age
        self.nationality = nationality
        self.boardsize = boardsize
        self.cwon = cwon

    def __repr__(self): #defines how the data will be represented in the print() function
        r = "\n The contestant {}, from {}, is {} years old, and currently has {} points! He is riding a {}ft board. {} has won {} championships this far!\n" .format(self.name, self.nationality, self.age, self.points,  self.boardsize, self.name, self.cwon)
        return r

    #makes arithmetic comparations between the objects
    def __add__(self, contestant2):
        s = self.points + contestant2.points
        return s

    def __sub__(self, contestant2):
        t = self.points - contestant2.points
        return t

    def __gt__(self, contestant2):
        return (self.points > contestant2.points)

    def __lt__(self, contestant2):
        return (self.points < contestant2.points)

    def __eq__(self, contestant2):
        return (self.points == contestant2.points)

#creates the objects and their attributes
Medina = Contestant("Gabriel Medina", 100, 26, "Brazil", 5.11, 8)
Slater = Contestant("Kelly Slater", 80, 35, "USA", 6.0, 9)
Cadu = Contestant("Cadu Maverick", 50, 19, "Frio de Janeiro", 5.5, 0)
Joao = Contestant("João Frango", 30000, 20, "Pantanal matogrossense", 5.7, 1)

ranking = [Joao, Slater, Medina, Cadu]
ranking.sort(reverse = True) #sorts the ranking from highest to lowest points

print(ranking)
