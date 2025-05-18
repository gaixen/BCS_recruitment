# Setting up the maze as a rectangualr grid
within the maze()function the given .txt files are plotted as rectangular grids with X as walls and * as the destination. 
Since the maze file does not specify the Triwizard Cup position, we randomly generate it at the beginning of each episode in a non-wall cell within the function reset(). I also have made sure that the position of cup that Harry is chasing is different from Preacher's(death-eater) position and Harry's position itself.
# Description of @createenviroment
Wall position .txt files are loaded followed by initialisation of return rewards and length of actions.With the help of get_randomposition() random positions for Harry,the death_eater(from now on I'll tell this as preacher) and the cup are generated within reset().It is made sure that their positions don't coinside with the positions of walls.It is also made sure that initial positions of Harry and the preacher aren't the same o/w the case is trivial.A valid move in the game is defined as one where the position is within the grids and not in the walls(this is being ensured in alid_move()).
## Defining a step:
left,right,up,down movements are seperated and position of Harry is updated accordingly.It is to be noted that 2 bool variables re defined namely 'truncated' and 'terminated' which decides whether Harry is intercepted by the preacher and Harry wins the cup before an encounter with the preacher.In case any of these 2 happen, the game is over.Also step()
function has observation,reward,terminated,truncated,info as the return values.
## Defining a reward:
In case Harry get the cup 100 points are credited.I n case the preacher finds Harry 100 points are taken away.For an encounter with the wall 5 points are taken away.In case of all other move involved otherwise , 1 point is taken away.
## Using Breadth First Search Algorithm 
Here the preacher is eager to hunt Harry before it reaches the cup. For this it is most likly to use Breadth First Search Algorithm. Here two lists are initialised . One is Visited that contains all the nodes that has already been visited and another is the queue which stores the nodes yet to visit.They are both appended after each movement.
### consideration
Only the relative positions of cup and preacher wrt to Harry are taken here.
## Get the text files from The Goblet of Fire/demo_maze folder
