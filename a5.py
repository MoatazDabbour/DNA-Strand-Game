# Moataz Dabbour 
# Assignment 5

import random as r

class Dna:
    
    BASES = ["C", "G", "A", "T"]
    
    def generate(num: int) -> str:
        """ Generate random DNA strand
            Returns a string of random characters of DNA nucleobases [C, G, A, T] that is 'num' long/
        >>> gen(4)
            'CAGG'
        >>> gen(4)
            'ATCC'
        """
        strand = str()
        for nbase in range(num):
            strand += r.choice(Dna.BASES)
        return strand
    

    def expandable(compr) -> bool:

        return not compr.isalpha()
     
    
    def compl(self):

        compl_str = str()
        for base in self:
            if base == "A":
                compl_str += "T"
            if base == "T":
                compl_str += "A"
            if base == "C":
                compl_str += "G"
            if base == "G":
                compl_str += "C"
        return compl_str


    def reverse(self):

        rev_str = self[::-1]
        return rev_str


    def compr(self):

        count = 1
        compr_strand = str()
        for i in range(len(self) - 1):  # For each char in strand - 1
            if self[i] != self[i + 1]:  # If unique
                compr_strand += self[i]  # Add to answer
                count = 1  # Reset count to 1
            if self[i] == self[i + 1]:  # If not unique
                if count == 1:  # Check if first repeating value
                    for j in range(i, len(self) - 1):  # Count remaining repeating values from that point
                        if self[j] == self[j + 1]:
                            count += 1
                        else:
                            break  # Stop when finished
                    compr_strand = compr_strand + str(count)  # Add count to 'corr_ans' value added when last change
                else:
                    pass
        compr_strand += self[-1]
        
        return compr_strand


    def __init__(self, n = 1):
        self.strand = Dna.generate(n)
        self.length = n
        self.compl = Dna.compl(self.strand)
        self.rev = Dna.reverse(self.strand)
        self.compr = Dna.compr(self.strand)
        self.expandable = Dna.expandable(self.compr)


    def __repr__(self) -> str:
        return "%s" % (self.strand)


class Player:

    score = int()

    def name_promt() -> str:
        """
        Prompts the user for a name input and returns it
        """
        name = input("\nWelcome to the DNA quiz game! \nEnter your username >> ")
        return name

    def __init__(self) -> None:
        self.name = Player.name_promt()
        self.score = 0 


    def addscore(a:int):
        Player.score += a

    def __repr__(self) -> str:
        return f"{self.name}"


def feedback(posneg: str):
    """ Prints a positive or negative feeback based on the char 'posneg'
    """
    
    POSITIVE = ["Wow!", "Well done!", "Amazing!", "Fantastic!", "Good Job!", "You make me proud!", "Great!"]
    NEGATIVE = ["Awee!", "Darn!", "Im sorry!", "Unfortunatly.", "Afraid not.", "Hit & miss!"]

    if posneg == 'P':
        print(f"\n{r.choice(POSITIVE)} That is correct! Your score is: {Player.score}\n")
    if posneg == 'N':
        print(f"\n{r.choice(NEGATIVE)} That is not correct. Your score is: {Player.score}\n")


def n_promt(player: Player):
    """
    Returns the chosen length of nucleobases strands [int, str]
    Returns int if n is positive integer.
    Returns str if n is not.
    """
    n = input(f"Hi {player}, please enter a positive integer for the DNA length >> ")

    if n.isnumeric():
        n = int(n)
        if n > 1:
            print("\nSelect an option [1-4] to answer a question or [5] to quit the game.\nWin the game by scoring at least 10 points!\n")
            return n # Return int
    else:
        return n # Return string


def complement(strand: Dna):
    """ Complement strand selection
        Complements DNA strand and prompts the user for answer.
    
        Key:
        A ↔ T
        C ↔ G
    """
    ans = input(f"\nWhat is the compliment of {strand}? >> ")
    if ans.upper() == strand.compl:
        Player.addscore(2)
        feedback('P')
    else:
        feedback('N')
    return


def reverse(strand: Dna):
    """ Reverse strand selection
        Reverses DNA strand and prompts the user for answer
    """
    ans = input(f"\nWhat is the reverse of {strand}? >> ")
    if ans.upper() == strand.rev:
        Player.addscore(2)
        feedback('P')
    else:
        feedback('N')
    return


def compress(strand: Dna):
    """ Compress strand selection
        Return the compressed form of a DNA strand, where an integer is placed before repeated nbases to point to number of repetition
        AAA → 3A
        TT → 2T
        CCCC → 4C

    """
    ans = input(f"\nWhat is the compressed form of {strand}? >> ")
    if ans.upper() == strand.compr:
        Player.addscore(3)
        feedback('P')
    else:
        feedback('N')
    return


def expand(strand: Dna):
    """ Expand strand selection
        compresses DNA strand and prompts the user for original.
    """    
    ans = input(f"\nWhat is the expanded form of {strand.compr}? >> ")
    if ans.upper() == strand.strand:
        Player.addscore(3)
        feedback('P')
    else:
        feedback('N')
    return


def main() -> None:

    UI = "1. Complement [2 points]     2. Reverse [2 points]     3. Compress [3 points]     4. Expand [3 points]     5. Quit\n>> "
    user_input = ""
    player = Player()
    n = None
    while not isinstance(n, int):  # repeat prompt for a valid 'n'
        n = n_promt(player)
    while user_input != "5":
        user_input = input(UI)
        if user_input == "1":  # Complement
            strand = Dna(n)
            complement(strand)
        elif user_input == "2":  # Reverse
            strand = Dna(n)
            reverse(strand)
        elif user_input == "3":  # Compress
            
            strand = Dna(n)
            while strand.expandable == False:   # Loop to make sure strand is expandable.
                strand = Dna(n)
            compress(strand)
            
        elif user_input == "4":  # Expand
            
            strand = Dna(n)
            while strand.expandable == False:   # Loop to make sure strand is expandable
                strand = Dna(n)
            expand(strand)
            
        elif user_input == "5":  # Quit
            if Player.score >= 10:
                print(f"\nThank you for playing, {player}! you are a winner with a score of {Player.score}")
            else:
                print(f"\nThank you for playing, {player}! You only scored {Player.score}")
            score = 0
        else:
            print("\nPlease enter a value between [1 - 5]\n")


if __name__ == "__main__":
    main()

