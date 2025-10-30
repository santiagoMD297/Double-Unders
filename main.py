class Toy:
    def __init__(self, name: str, color: str, fun_level: int):
        # Make a new Toy with name, color and level of fun
        self.name = name
        self.color = color
        self.fun_level = int(fun_level)

    def cheer(self):
        # Make the toy say a happy message.
        return f"{self.name} goes: Yay! Let's play!"

    def __str__(self):
        # Text when you print the toy.
        return f"Toy(name='{self.name}', color='{self.color}', fun={self.fun_level})"

    def __eq__(self, other: object):
        # Two toys are equal when the name and the color are the same. The fun can differ
        return (self.name, self.color) == (other.name, other.color)

    def __lt__(self, other: "Toy"):
        # Compare by fun_level (so sorting puts less-fun first).
        return self.fun_level < other.fun_level

    def __add__(self, other: "Toy"):
        # Add two toys together to make a combo toy. The new toy's name is 'name1 + name2', color is 'mixed', and fun is the sum but not more than 10.
        new_name = f"{self.name}+{other.name}"
        new_color = "mixed"
        new_fun = self.fun_level + other.fun_level
        return Toy(new_name, new_color, new_fun)


class ToyBox:

    def __init__(self, toys):
    if toys is None:
        self._toys = []
    else:
        self._toys = list(toys)

    def add_toy(self, toy: Toy):
        #Put a toy into the box.
        self._toys.append(toy)

    def remove_toy_by_name(self, name: str) :
        #Take out the first toy with this name. 
        #Returns True if something was removed, False otherwise.
        
        for t in self._toys:
            if t.name == name:
                del self._toys[i]
                return True
        return False


    def total_fun(self) -> int:
        #Add up all the fun levels of the toys.
        return sum(t.fun_level for t in self._toys)


    def __len__(self):
        #How many toys are inside? This lets len(box) work.
        return len(self._toys)

    def __getitem__(self, index: int):
        #Let us do box[index] to get a toy at that spot.
        return self._toys[index]

    def __setitem__(self, index: int, toy: Toy):
        #Let box[index] = toy to replace a toy at that spot.
        self._toys[index] = toy

    def __str__(self):
        #Print the box and its toys
        return f"{self._toys } | fun={self.total_fun()}"

    def __eq__(self, other: object) -> bool:
        #Two boxes are equal if they have the same toys in the same order
        return self._toys == other._toys

    def __lt__(self, other: "ToyBox"):
        # We'll compare by total_fun.
        # This lets you sort boxes by how fun they are!
        return self.total_fun() < other.total_fun()

    def __add__(self, other: "ToyBox"):
        #Add two boxes together to make a bigger box with all the toys.
        return ToyBox(self._toys + other._toys)
