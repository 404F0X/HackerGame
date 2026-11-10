Analysis
What problem do I aim to solve?
When I played the gomoku with my friends in the boarding house,it was fun at first. However, with the development of our gomoku technique and more and more compaction happening,I find that the competitors are becoming repetitive for some reason. To make it better,I decided to program a gomoku-like game.
So,the rules of the traditional gomoku game are easy and accessible. On one hand, the easy rules make it easier to attract new players and make anyone start a game easily and bring them fun. On the other hand,the simple rules means when the player familiarizes themself with the game, their behavior will tend to become consistent, that means the different players may do the same dissections in different competitions,which makes the game increasingly deterministic.When it become more and more deterministic,then loss fun.
What problem do I need to solve?
Before starting to solve this problem,we should make the problem clear: what makes the traditional gomoku boring?referring the Rule(from Wiki) of it,we find that the core rules
This is a turn-based game; after placing a piece, the turn switches to the opponent.
The winning condition is for one player to form a line of five stones; if the board is filled without a line of five being formed, the game ends in a draw.
Based on "Core Rule 2," player actions are categorized into defensive and offensive moves, while the objective is defined as forming a line of five pieces.
This implies that as players gain experience and reach a certain level (a plateau), the scope of high-value decision-making narrows; players gravitate toward optimal moves, leaving less room for variation. Consequently, the decisions of both sides become predictable, and matches tend to become homogenized—a trend that eventually leads to player attrition.

based the analysis of the problem above, the root causes of the problem are:
1. Players have limited behavioral choices, leading to a convergence on the same high-value decisions.
2. Players receive few ongoing rewards, resulting in a lack of sufficient motivation to continue playing.





What will I do to solve these problems?
As the problem we identify in the last section. I will add these new rules
Add the skill systems in the program,it’s designed to increase the arena of strategic interaction because it will make players have to thinking about what skill will be used by their opponents, that should make more options that players may can choose
Add the special point on the board,the special point will appear randomly, when the player places a piece at this point, they will claim rewards,like expand advantages / acquire skills
We plan to introduce mechanics similar to HP and Attack Power to increase player margin for error; this serves as a source of positive feedback and expands the scope of choices available to players at each step.



What similar solutions exist? 
To make a better solution for the program,I find those existing solutions
Traditional Gomoku 
As a game similar to Gomoku, it is only natural to start with traditional Gomoku.These analysis are based on Play Gomoku Online 
Rule of traditional Gomoku
Players alternate turns placing a stone of their color on an empty intersection. Black plays first. The winner is the first player to form an unbroken line of five stones of their color horizontally, vertically, or diagonally. In some rules, this line must be exactly five stones long; six or more stones in a row does not count as a win and is called an overlineIf the board is completely filled and no one has made a line of 5 stones, then the game ends in a draw.(these text are from Wiki )

What are their features? 
Following the image below,we find that they offered the register/login function,Real-time online player number display, single and online battle 

The image below shows the “Single Player” page,which is a single player play against the robot, players are able to practice themselves with different difficulty ranks and choose which color they would like to be.

The image below shows the page when the player starts a competition with robot/real human,the state bar below shows the player name,whose term,the time the player has already used.There is also a semi-transparent piece used to indicate the position where you have currently chosen to place a piece.



When someone wins/loses,there is a notification window to let you know how many moves you take and how long you finished this competition.


The image below shows the signup/login page.They require the user name,email address and the password.Once you input the information correctly,they will create an account and log you in.

What data do they need/store/produce?
For the register,They should store the user name,password,email address.They will be used to create/check if the user log in information is correct or not.

For the playing page,they should store both of the player name,whose turn,and the state of the game board like where is each pieces
 What is the GUI like? 
The GUI is simple,the color scheme is based on blue and white.They make the UI concise and clear and that helps the player easier to find what they want.

What are the strengths and weaknesses?
strengths 
It provides an online platform and allows the players to compete anywhere. Because it runs on browsers which means it can support all the devices that support web browsers and the user can use it no matter where they are.
It can automatically check if there are 5 pieces in one row with same color and determine the winner.That leads to less mistake and argument due to the fair of algorithm.Because the computer only flower the rules of the gomoku and will not make mistakes
weaknesses
Firstly,it’s still based on traditional Gomoku rules,which means it will get boring and lose users with time.

Secondly,When registering,they do not require the submit code from the email that they ask for in the register page.That means the user can register their account by using other’s e-mail address.Morever,They hacker can register millions of account with individual email address and takes lots of server resource

4ASCEND

Rule of 4ASCNED
Each Player has 6 HP at the start of this game.
The player can place one piece in each turn
When 4 pieces of the player is in the same line, ASCEND triggered. 
When ASCEND is triggered, all pieces from the ASCEND are removed from the board. The ASCEND then becomes a pending attack against the opponent. 
The opponent is allowed to make ASCEND to response the ASCEND made by the player
If the opponent place piece on the position which has been cleared by ASCEND,the damage of pending attack will reduce 1
After the response turn, the remaining attack strength is calculated and the opponent loses the corresponding amount of HP. If the response image of ASCEND is larger than pending image,The player recessive the damage
If a player's HP become less then 0(include 0), that player loses the game. 
The special points spawn randomly on the board; placing a piece on such a point will make it become a special piece with an attack power of 2.

What are their features? 
Compared to gomoku.com,there are no register/login functions.From the main page,I find that it offers 4 main modes

Play against CPU(Robot)
Play against another player on the same device
Play against the player online
Check the record of your game.


The image below show the page when I choose to play against robot.I find that there are also has different rank of the difficulty and I’m allowed to check the settings

The image below shows the setting page,
The players are allowed to change the Max HP of the player and robot,the thinking time of the player,who has the first move,and the first player's color. These things make the 4 ASCEND more fun because it makes the gameplay more diverse.

Now,I finished the settings,I started a game.There is a 9x9 board with a dice which is used to decide who has the first move.Then I find that if it’s my turn,it will tip me “My turn” on the right of my character.Also,there is a blue frame to show me where I will place the piece.
When there is 3 pieces in on line,it will tip you by a long line with your color  and a crisp sound

When there are 4 pieces in one line,the screen turns dark and the pieces fly near the character who triggers the ASCEND,and I have to respond to the ASCEND.Once the opponent can not make the ASCEND,They loss HP

Once the system calculator the and the player recessive damage,the special(green glasses) point will appear on the board

What data do they need/store/produce?
Based on observations of ASCNED,I find that they should store the settings in the settings page. They should also store the state of the board like where the special points are,the pieces of each player,because the algorithm needs them to analyze the game state. The HP should also be stored on 4ASCEND
 What is the GUI like? 
The art style of 4ASCEND is pixel art style,the developer uses dark black,white,red,green and blue as the main color,they make 4ASCEND more retro style.The main page of 4ASCEND is quite simple and direct,it put all the things you can do on the GUI which makes it clear and easy to start.

What are the strengths and weaknesses?
strengths 
Firstly,the rules of 4ASCEND are still simple and easy to understand.Compare to traditional gomoku,we find that the player should decide more things in each move because of the HP and ASCEND rules.Which increase the player behavior space and make the game less repetitive.

Secondly,the sound effects and visual effects make the feeling feeling.Comparing to traditional gomoku,the punchy sound effects and ASCEND special effects can bring the positive feelings for players.That makes the player feel more enjoyable in their program.

Thirdly,they has special pages to show players the rules.That could help new players get starting,because the player and read the rule book when they could not understand the rules
weaknesses
The most important weakness of 4ASCEND is inability to change the language.That makes it difficult when the people not from JP try to read the rules,which also means it’s harder for players to understand the meaning of each button and so on.

The second weakness is that 4ASCED does not have the new player guide,the only way for the new player to understand and try to using the rules is reading the “rule book”.Which also makes it harder to get started because players are much like to learning the rules in games instead of reading the long rule book.The design now is good,but in this case,it’s not good enough

The third weakness is that 4ASCEND the resources requirement,when ASCEND happens,the FPS will drop significantly.And that makes the bad gaming experience because there are no player can bear with the stuttering during the game
 

Gomoku with special skills
Rule of Gomoku with special skills
The core rules are still based on traditional gomoku rules.The difference between it and traditional gomoku is it imports the skills to the gomoku.Players are only allowed to use one skill in one turn.Here is some examples of the skill: remove opponent’s pieces,skip the opponent’s next turn and so on.

 What are their features? 
As the image below shows, the Gomoku with special skills offered a single game(played against LLM) and played with other players.Players are allowed to create games/join games.There are also some selections like “about”,”Version 2.0” which is update logs,leader board and feedback.
The image below is about the playing page(Single player mode),there are 3 windows.From left to right,there is a skills list of black(P1),the board and the skills of white(P2).Each skill has their own description and the CD on their options.
Without the skills list,it’s just traditional gomoku.So that I’m not going to talk about the things that we have analysed.

strengths 
The first strength is the rules,it imports the skills into the gomoku which makes it more possible.
weaknesses
The first weakness is there is no way to change the language.
The second weakness is the opponent can see what skills you have and this renders information transparent, turns skills into mere tools, and reduces the scope for strategic maneuvering.
The third weakness is there are no recording which means players can not do game review.That means they are unable to improve themselves in the game

What’s the final program I want to make
Based on the analysis I did,I find that gomoku.com makes the game easier to start and play against with other players by automatic rule validation and online playing.But it still hasn't changed the rules which means it’s still the gomoku and didn’t solve the core problem of gomoku.However,its online features provided good inspiration for my project.

To the 4ASCEND,compared to gomoku.com,it has less online features like online accounts.However, for this project, its rules are more worthy of reference.Because it makes the game more variability which solve the core problem of traditional gomoku game by using simple rules to make the more possibilities.Also,I should also take the recording feature, it can help players observe previous matches they played, this reduces the learning cost for players.Because that allowed improve themselves by reflecting on past matches but not gaining experience through matches.And usually, the last one will make the player feeling frustrated when loss.Moreover,the stuttering caused by special effects also warns me,do not sacrifice game performance for visual effects.Because it makes players feel very bad and once players feel bad,then the game losses them.

To the Gomoku with special skills,same as 4ASCEND,it does not support English for some reason which is bad.Because when players can’t understand the text,then they will not be interested in these games.Additionally,the colors does not coordinate well and it makes it a bit tiring to read.However,the idea of skills is still worth to consider.

So,based on these analysises,I decided to make a gomoku-like game,which combines the rules of both games.I will keep the online gaming and account systems in the program,the core rules from 4ASCEND and the skills ideas.

What is the core functionality of the solution?
it’s the time to make the program clear:
The program should have the board,the program is based on the board,the board should store where pieces and special points,the owner of each piece and where the player can place the piece.These make the computer able to process the board states of the program.
The program should also have the rule engine to determine rules,this the brain of the program because it’s responsible to check the board if there is ASCEND/back attack in the board,the place that the player going to place a piece is legal or not and so on.That reduce the repetitive tasks that players have to deal with that are unrelated to the actual gameplay.

The program should also have the GUI that the user can clearly understand the situation on the board.Because if there are no GUI for players,it will be hard for them to analyze the board state and the program will lose its speciality,then the program will lose fun and hard to get started.

The program should also allow the single player mode(two players play on the same computer),it’s the base of the whole program because the online playing,the LAN playing,the robot playing share the same logic.Which means it could reduce the code that I need developing because they are repeat work.
What extras could you add?
After deciding the necessary part of the program,I’m able to add some extra features to make the program better

Firstly,it’s the online gaming,it allowed the players around the world to play together

Secondly,the ELO system,the players are more likely to play with others that has same rank.If the player always play with the higher rank player,they may fell frustration which means the bad gaming fells

Thirdly,the AI opponent should be added in,when the player wants to improve themselves without play with real human players due to some reason.They are able to play against AI and that could make a better gaming feelings

Lastly,the recording system,the player is able to check the past gaming records and use them to improve themselves by finding the better move in the past games.

What computational methods could be used?
After I make the things that I need to do clear,I’m able to decide the computational methods I should use.

First,I need something to represent the board and store the data in the board.There is a dictionary,list,graph that I can choose.Finally,I decide to use 2D-list to represent the board because It can be regarded as a coordinate system, where each coordinate represents a space that can place a piece.So that I can use list[y][x] to represent the space and it allows the rule engine  to use list comprehensions to get pieces that are in the same line.That could reduce the resource usage because we don’t need to make convent the data every time to process.

Second,I need something to store the repeat things like pieces,boards,players because if I make new elements every time,then the code could be horrible. And I find the object could be used to represent the repeat things by Instantiate a common class.For example,I can class Piece,then in the next time,I’m able to directly making list[y][x] to Piece which reduce the repeat working and make a better develop efficient

Third,I need something to store the password from the user,the service should not store any password.So I need something to make the service able check if the password is true without the exact password.That makes me to choose hax,because usually,one hex value can only represent one value which could be the password.Which means the user can only give us the password hax,then we can check if the hax is as same as it in the service to prevent the lack of password.

Fourth,abstraction should be used in my program because it makes the code easy to understand by reducing the unnecessary part of the code.It’s very important because it makes the responsibilities for each part of the project clearly defined and reduces the confusion.For example,if the GUI manages and game engine both manage the board,it makes the responsibilities confuse because the GUI does not care how board working,it responsible to how to display the board.That’s the reason why I disease to use abstraction


What are the limitations of scope/functionality
The scope of my program will include the rule engine,the network,and other things.How every,the AI player will take me a lot of time to learn how to build an AI player so that I’m not going to spend any time on the AI player.

The network may be unstable due to the physical location of the service,which means I have to buy the service in different countries to improve the network connection.However,it’s out of my range.


What hardware and software will be required to support the solution?

It required the pygame,because the pygame provides multiple useful tools to help me develop the program faster.For example it can be used to help me process the player input,like what does the player click.Which help the programs processes the events easier.the other reason is the pygame is based on python which is a program language that easier to learn and use.That takes me less to learn and easier to find the solutions of problems online.

It also required the python version = 3.13,the newest python version that the pygame supports.Which means I can take advantage of python's new features and performance optimizations.

Due to the requirement of python,it also required windows >= 8.1 .because the python 3.13 can not run on windows that the version is less then 8.1.

It needs the mouse/keyboard to let the computer know what they want to do.And then send them to my program so that my program is able to process the event and trigger the functions.

It also needs the screen,easily,if there is no screen,how does the player know  what’s going on in the program




Decomposition
Firstly,we should make the responsibility clear for different modules of the program.
In my program,it should be like Player Action -> Input Handler -> Game Controller -> Game Logic -> Renderer
Play Single Game
Process Player Input
recessive click or keyboard input from user
convert input into game event
 Game Controller
Determine the current game state
Determine the current player
Call the required game logic module
 Rule Engine
Determine 4ASCEND
Determine Response
Caculat Dmage
Create Special Point
Execute Skill
 Render
Render the main GUI
Render the game effect
Service/Client
…






Class Design
Player
The Model class responsibility to the class of the object and the data structure of Board,Player and so on


Field
Entered
Updated
Validation
player_id
When created
Not updated
Required integer
Player_name
When created
Not updated
Required string
HP
When created
When caculate dmage
Required integer
skill_point
When created
When use skill or place in special point
required integer and no less than 0


Method
Algorithm
notes
loseHealth(damage)->int
 self.HP-=dmage
return self.hp
Used after Attack/Response resolution

Piece

Field
Entered
Updated
Validation
x
When created
Not updated
Required int and not out of board
y
When created
Not updated
Required and not out of board
player
When created
Not updated
Required Player type
effect
When created
Not updated
Required list




Cell

Field
Entered
Updated
Validation
x
When created
Not updated
Required int and not out of board
y
When created
Not updated
Required and not out of board
piece
When created
Not updated
Required Piece type
effect
When created
Not updated
Required list


Board

Field
Entered
Updated
Validation
Board
When created
When board update,for example place piece,create special point
Required Cell type
length
When created
Not updated
Required integer
width
When created
Not updated
Required integer




Method
Algorithm
notes
get_cell(x,y):->Cell
if x,y is in board:
 return self.board[y][x]
else:
 return None
The method also check if the piece is in the board
get_piece(x,y):->Piece
return get_cell(x,y).piece
Noting here
remove_piece(x,y)
self.get_cell(x,y).piece=None


Noting interesting
remove_pieces(piece_list)
for piece in piece_list:
 self.get_cell(piece.x,piece.y).piece=None
recessive list[piece],set all the  piece in cell into None 
place_piece(x,y,Player)
if get_cell(x,y).piece is None:
 get_cell(x,y).piece=Piece(x,y,Player)
Noting interesting

RuleRngine

Field
Entered
Updated
Validation
board
When created
Not updated
Required Board type
current_player
When created
When end of the turn
Required Player Type
player1
When created
Not updated
Required Player Type
player2
When created
Not updated
Required Player Type



Method
Algorithm
notes
detect_piece_in_line(x,y,player)
for i in board:
 for cell in board:
  if cell.piece.player=player
  add piece_in_line
returns the list of pieces that connected when place the piece
detect_ASCEND(x,y,player)
for line in self.detect_piece_in_line(x,y,player):
 if len(line) >= 4
 ASCEND.append(line)
4ASCEND triggered when 4 piece in one line
remove_piece(x,y)
self.get_cell(x,y).piece=None


Noting interesting
detect_Response(x,y
return self.detect_ASCEND(x,y,player)


used to detect if there is also 4 pieces in one line
calculate_damage(ascend,respond,current_player)
if len(ascend)-len(respond) > 0
 current_player.loseHealth(damage)
else: 
 if current_player ==self.p1:
   self.p2.lossHealth(damage)
 else:
  self.p1.lossHealth(damage) 
  




iedi