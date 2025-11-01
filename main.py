class Toy:
    #this function runs automatically when you make a new Toy
    def __init__(self, name, color, fun_level):
        self.name = name
        self.color = color
        self.fun_level = int(fun_level)

    #makes the toy say something
    def cheer(self):
        return f"{self.name} goes: Yay! Let's play!"

    #when you print the toy, this is what shows up
    def __str__(self):
        return f"Toy(name='{self.name}', color='{self.color}', fun={self.fun_level})"

    #check if two toys are equal (same name and color)
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    # Compare toys by fun level (for sorting)
    def __lt__(self, other):
        return self.fun_level < other.fun_level

    # Add two toys together to make a new combined toy
    def __add__(self, other):
        if not isinstance(other, Toy):
            return False
        new_name = f"{self.name}+{other.name}"  # combine names
        new_color = "mixed"                     # set new color
        new_fun = self.fun_level + other.fun_level
        return Toy(new_name, new_color, new_fun)

class ToyBox:
    #runs when you make a new ToyBox
    def __init__(self, toys=None):
        # If no toys are given, start with an empty list
        if toys is None:
            self.toys = []
        else:
            self.toys = list(toys)  # make a list from the toys we got

    #add a new toy to the box
    def add_toy(self, toy):
        self.toys.append(toy)

    #remove a toy by its name (first one found)
    def remove_toy_by_name(self, name):
        for toy in self.toys:
            if toy.name == name:
                self.toys.remove(toy)
                return self.toys

    #add up all fun levels inside the box
    def total_fun(self):
        total = 0
        for toy in self.toys:
            total += toy.fun_level
        return total

    #let len(box) tell us how many toys are inside
    def __len__(self):
        return len(self.toys)

    #let us use box[index] to get a toy
    def __getitem__(self, index):
        return self.toys[index]

    #let us use box[index] = toy to replace a toy
    def __setitem__(self, index, toy):
        self.toys[index] = toy

    #what shows when we print the ToyBox
    def __str__(self):
        toy_names = []
        for toy in self.toys:
            toy_names.append(toy.name)
        #turn the list into a single string
        names_text = ", ".join(toy_names)
        return f"ToyBox({names_text}) | total fun: {self.total_fun()}"

    #compare two ToyBoxes to see if they have the same toys
    def __eq__(self, other):
        return self.toys == other.toys

    #compare boxes by total fun (so we can sort them)
    def __lt__(self, other):
        return self.total_fun() < other.total_fun()

    #add two ToyBoxes together to make a new one with all toys inside
    def __add__(self, other):

        return ToyBox(self.toys + other.toys)