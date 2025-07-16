import random
# Standard suits and ranks for a 52-card deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}

class Card:
    """
     Represents a single card with a suit, rank, and value.
     """
    def __init__ (self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """
     Represents a full deck of playing cards. Using Card objects to create cards based on suit and rank.
     """
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                created_cards = Card(s,r)
                self.deck.append(created_cards)

    """Method for Shuffling the deck."""
    def shuffle (self):
        random.shuffle(self.deck)

new_deck= Deck()    # Deck created
new_deck.shuffle()  # Deck shuffled

class Player:
    """
    Represents a player in the game, holding a hand of cards and a name.
    """
    def __init__(self, name):
        self.name = name
        self.hand = []
    def __str__(self):
        return f"Assigned Player name: {self.name}"

class PlayerHand:
    """
       Takes two player names, creates Player objects, and deals the deck.
       """
    def __init__ (self,name1,name2):
        self.name1 = Player(name1)
        self.name2 = Player(name2)

        for i,x in enumerate(new_deck.deck):
            if i%2 == 0:
                self.name1.hand.append(x)
            else:
                self.name2.hand.append(x)
    def __str__(self):
        return f"{self.name1.name} has {len(self.name1.hand)} \n{self.name2.name} has {len(self.name2.hand)} "

class Rounds:
    """
       Represents the logic for each round. It would include player input and resolving battles/'wars'.
       """
    def __init__(self, player_hand):
        self.round = 1
        self.player_hand = player_hand  # Instance of PlayerHand

    def play_round(self):

        print(f"\n--- Round {self.round} ---")
        holded_cards = []   # Cards on hold that later needs to transferred to winner of a round.

        while True:
            # For Debugging: To reveal Player Hand while testing the game uncomment the below 2 lines.
            #print(f"{self.player_hand.name1.name}'s hand: {[str(card) for card in self.player_hand.name1.hand]}")
            #print(f"{self.player_hand.name2.name}'s hand: {[str(card) for card in self.player_hand.name2.hand]}")

# Get player1 input>>drawing card as per input>>moving card to holding deck> shuffling the hand to avoid cheating
            while True:
                try:
                    idx1 = int(input(f"{self.player_hand.name1.name}, choose a card index (1-{len(self.player_hand.name1.hand)}): "))
                    if idx1 <=0:
                        print("Please enter value within the range")
                        continue
                    card1 = self.player_hand.name1.hand.pop(idx1-1)
                    holded_cards.append(card1)
                    random.shuffle(self.player_hand.name1.hand)
                    break
                except (ValueError, IndexError):
                    print("Invalid index. Try again.")

# Get player2 input>>drawing card as per input>>moving card to holding deck> shuffling the hand to avoid cheating
            while True:
                try:
                    idx2 = int(input(f"{self.player_hand.name2.name}, choose a card index (1-{len(self.player_hand.name2.hand)}): "))
                    if idx2 <=0:
                        print("Please enter value within the range")
                        continue
                    card2 = self.player_hand.name2.hand.pop(idx2-1)
                    holded_cards.append(card2)
                    random.shuffle(self.player_hand.name2.hand)
                    break
                except:
                    print("Invalid index. Try again.")

            # Show drawn cards
            print(f"{self.player_hand.name1.name} drew: {card1} (value: {card1.values})")
            print(f"{self.player_hand.name2.name} drew: {card2} (value: {card2.values})")

        # Determining Winner or War. Also while at War checking if player have sufficient hand.
            if card1.values > card2.values:
                self.player_hand.name1.hand.extend(holded_cards)
                print(f"{self.player_hand.name1.name} wins the round!")
                break
            elif card2.values > card1.values:
                self.player_hand.name2.hand.extend(holded_cards)
                print(f"{self.player_hand.name2.name} wins the round!")
                break
            else:
                print("It's a WAR!!!!")
                if len(self.player_hand.name1.hand) < 7 and len(self.player_hand.name2.hand) < 7:
                    print(f"Both {self.player_hand.name1.name} and {self.player_hand.name2.name} does not have enough cards for war! Its a Draw")
                    return "Draw"
                elif len(self.player_hand.name1.hand) < 7:
                    print(f"{self.player_hand.name1.name} does not have enough cards for war! Game over.")
                    return "Win2"
                elif len(self.player_hand.name2.hand) < 7:
                    print(f"{self.player_hand.name2.name} does not have enough cards for war! Game over.")
                    return "Win1"
                for x in range(8):
                    x1 = self.player_hand.name1.hand.pop(random.randint(0, len(self.player_hand.name1.hand) - 1))
                    x2 = self.player_hand.name2.hand.pop(random.randint(0, len(self.player_hand.name2.hand) - 1))
                    holded_cards.append(x1)
                    holded_cards.append(x2)
                    # Show hand sizes for loop War !!!!
                print(f"{self.player_hand.name1.name}'s now has {len(self.player_hand.name1.hand)} Cards \t\t\t\t {self.player_hand.name2.name}'s now has {len(self.player_hand.name2.hand)} Cards")
            continue

        # Changes Round when completed
        self.round += 1
        # Show hand sizes for start of each Round !!!!
        print(f"{self.player_hand.name1.name}'s now has {len(self.player_hand.name1.hand)} Cards \t\t\t\t {self.player_hand.name2.name}'s now has {len(self.player_hand.name2.hand)} Cards")

class GameChecker:
    """
      On/Off Switch for game. To see if game needs to be continued or stopped.
      """
    def __init__(self, player_hand):
        self.player_hand = player_hand

    def play_game(self):
        """
               Runs the entire game until a win, draw, or both players lose all cards.
        """
        rounds = Rounds(self.player_hand)
        gameon = True
        while gameon:
            # Check for Draw or win conditions. If either of the condition break from while loop.
            if len(self.player_hand.name1.hand) > 0 and len(self.player_hand.name2.hand) > 0:
                result = rounds.play_round()
                if result == 'Draw':
                    print("It was a Draw..")
                    break
                elif result == 'Win1':
                    print(f"{self.player_hand.name1.name} WON!")
                    break
                elif result == 'Win2':
                    print(f"{self.player_hand.name2.name} WON!")
                    break
                # else, continue the game
            else:
                if len(self.player_hand.name1.hand) == 0 and len(self.player_hand.name2.hand) == 0:
                    print("Both players ran out of cards. It's a DRAW.")
                elif len(self.player_hand.name1.hand) == 0:
                    print(f"{self.player_hand.name1.name} WON! the game")
                else:
                    print(f"{self.player_hand.name2.name} WON! the game")
                break

# Example usage:
class Playername:
    """
     Handles getting unique, confirmed player names from user input.
     """

    def __init__(self,num_players=2):
        self.num_players = num_players
        self.players = []

    def get_names(self):
        """
        Prompts for player names, confirms no duplicate name and ask for name confirmation.
        Returns: List of player names.
        """
        for i in range(1, self.num_players + 1):
            while True:
                name = input(f"Enter your name (Player {i}): ").strip()
                # Check if name already taken
                if name in self.players:
                    print(f"The name '{name}' is already taken. Please enter a different name.")
                    continue
                confirm = input(f"Confirm if you want to continue your name as {name} - Y/N: ").strip().upper()
                if confirm == 'Y':
                    self.players.append(name)
                    break
                elif confirm == 'N':
                    print("Please enter a new name.")
                else:
                    print("Enter only 'Y' or 'N' to confirm the name.")
        return self.players

# --- Starting Game ---

# Get player names
names = Playername()    # names object created with class Player. This will have name.players list
player_names = names.get_names()
# Method get_names used to get 2 unique player names. returns list of 2 players in new object player_names.

assign_player = PlayerHand(player_names[0], player_names[1])
# PlayerHand will take 2 args, name1 and name 2 for creating 2 player's hand from deck.

game = GameChecker(assign_player)
# Now GameChecker will start the game. Both class Rounds and GameChecker has attr player_hand.

game.play_game()
# GameChecker method play_game() has Class Rounds -- round_play_round() method defined within which will start first round and game will start.
