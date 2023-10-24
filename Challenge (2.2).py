# Define the base class player
class player:
    def play(self):
        Print("The Player is player cricket.")

#Define the dervied class Batsman 
class Batsman(player):
       def play(self):
         print("The batsman is batting.")

# Define the dervied class Bowler 
class Bowler(player):
      def play(self):
          print("the bowler is bowling.")

# create objects of Batsman and Bowler classes 
batsman=Batsman()
bowler=Bowler()

# call the play() method for each object 
batsman.play()
bowler.play()