#Easter egg basket inventory
class Candy:
    def __init__(self, candy_name, candy_amt, candy_value):
        self.candy_name = candy_name
        self.candy_amt = candy_amt
        self.candy_value = candy_value

class Person:
    def __init__(self, person_name, total_points):
        self.person_name = person_name
        self.total_points = total_points
        self.candy_inventory = {}
    
    #create candy and give it a value
    def add_candy(self):
        candy_name = input("Enter the name of the candy!: ")
        candy_value = int(input("Enter the point value of the candy! "))
        candy_name = Candy(candy_name, 1, candy_value)
        #adds candy to inventory as a dictionary
        self.candy_inventory[candy_name.candy_name] = candy_name.candy_amt
                           
    #add to the amount of candy ALREADY in your inventory
    def add_quantity(self):
        print(list(self.candy_inventory.keys))
        candy_to_edit = input("Enter the name of the candy you want to add to")
        if candy_to_edit in self.candy_inventory:
            add_amt = int(input("How much do you want to add? "))
            self.candy_inventory[candy_to_edit] = self.candy_inventory.get(candy_to_edit, 0) + add_amt

    def view_inventory(self):
        print(f"Displaying Inventory: \n {self.candy_inventory}")
    
        

def create_person():
    person_name = input("Enter your name to begin!: ")
    person = Person(person_name, 0)
    return person


def Return():
    leave = int(input("Enter 1 to exit and 2 to continue."))
    return leave

def main():
    person = create_person()
    while True:
        Action = int(input("""What would you like to do?:
                            [1] - Add Candy
                            [2] - Add quantity
                            [3] - View inventory
                            """))
        
        if Action == 1:
            person.add_candy()
            leave = Return()
            if leave == 1:
                 break
            else:
                continue
        elif Action == 2:
            person.add_quantity()
            leave = Return()
            if leave == 1:
                 break
            else:
                continue
        elif Action == 3:
            person.view_inventory()
            leave = Return()
            if leave == 1:
                 break
            else:
                continue
        else:
            print("Please input a valid option.")


main()


