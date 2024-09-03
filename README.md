# Two-Player Chess Game README

Summary and Review of the Problem =>
My challenge involves developing a two-player chess game using Python's Pygame library. The game will include functionality for moving pawns , bishops , rooks ,knights ,Queen and King awsell as gameover , checkmate functionality it will have turn-based play were you can capture opponent pieces, and place the opposing team into check/checkmate . My proposed solution involves creating a visually appealing and fully functional chessboard with intuitive interactions, a proper game flow, and the ability to handle various game states, including turn switching and victory conditions.

# Running Game
To install pygame, use pip
    
    1)  pip install pygame
    
    2)  Once Pygame is installed run code on code editor and begin play with whites turn.

# Game Rules
The rules of the game are as follows , your aim is to place the opponents king into check to do this you may use your arsenal of pieces ,when you click on a piece you can see what valid moves it can take . Knights are allowed to move in an L shape, Pawns move upwards by 2 spaces and then 1 space , Bishops move diagonally , Rooks can move up,down & side to side, a Queen can move in any direction and a King can move 1 space in its surrounding squares. When a piece lands on a square occupied by an opponent’s piece, the opponent’s piece is captured and removed from the board. Captured pieces are displayed in the side menus.You can achieve checkmate by using your pisces to surround the enemy King. The game ends when one player successfully checkmates the opponent's king. A game-over message will appear, and the player can start a new game by pressing Enter.
 
# UML Style Diagram 
![Screenshot 2024-09-03 at 13 17 57](https://github.com/user-attachments/assets/f91e0a0c-846b-4831-b226-62d63412527a)


# Initial Working Plan and Development Strategy

Development Strategy: The game will be built incrementally using an object-oriented design approach. I will start by creating the chessboard using the draw_board function and then adding the draw_piceas function to draw the pieces onto the board . My next step will be handling the piece movements for this I will create the logic for valid moves each piece can take and place the logic into check_piece  functions. Then I will be adding in a function to check which players turn it is and code a prompt to the player saying “its whites turn” or vice versa . The last thing I will create is the logic for a winning player , forfeiting and a gameover screen aswell as the option to restart the game. 

Approach to Quality: I will ensure quality by adhering to best coding practices such as encapsulation of my functions and creating reusable code I will thoroughly unit test my game during the development phases and create clear comments explaining my events and functions. I will also complete user testing once the game is finished and compile a questionnaire on feedback I get from users 

# Epics => 
Chessboard Creation: Set up the graphical user interface using Pygame and drawing the chessboard.

Piece Initialization: Loading chess piece images from my assets folder and positioning them correctly on the board.

Player Interaction: Implement player turn handling and input processing for selecting and moving pieces.

Game Logic: Develop functions to check valid moves, detect check/checkmate, and handle piece capturing.

Endgame Handling: Implement victory conditions and game reset functionality.

# Object-Oriented Design and Breakdown
Game Class: Handles the main game loop, event handling, and state management.

Board Class: Manages the chessboard's drawing and piece placement.

Piece Class: Implements the behavior of each type of chess piece, such as movement and capturing.

Utility Classes: Provide helper functions for tasks such as checking valid moves and detecting check/checkmate conditions.

# Release 1 
Task: Set up the basic chessboard using Pygame and load piece assets onto the board. 
Code Review: Initial code successfully draws the chessboard and pieces, and the GUI elements are responsive to user actions.
Changes: Added comments to improve code clarity and modularized the functions for drawing the board and pieces.


# Release 2
Task: Implement piece selection and valid move calculations for each piece.
Code Review: Piece selection is functional, and valid moves are accurately calculated. Turn-based logic has been implemented.
Changes: Refined the logic for handling special moves like pawn promotion and castling.

# Release 3
Task: Ensure proper handling of check and checkmate scenarios aswell as a gameover screen and a forfeit button.
Code Review: The game correctly detects check/checkmate and highlights the king when in check the forfeit button displays a winner message and allows the player to 
Changes: Improved efficiency in move validation and check detection by streamlining condition checks.

# Reflection on Key Design Challenges
One of the key design challenges was figuring out how to indicate to the user that they were in check this was important because checking would then lead to a gameover and there would need to be a clear way to show the player that they were in danger and had to move their king piece somewhere safe . After some brainstorming I came up with three ideas to do this one being having text displayed to the player telling them “you are in check” . The second idea being to prevent the user from being able to move any of their other pisces until they move their king out of check . My last idea was having the square around the king flash when in check. I decided to go with the last option as I felt it was the clearest way to indicate check to the player as the flashing border around the king would be visually distinct and indiciates the plater that their king was in danger. I had to iterate through a function to check if the king was in check and then add a border around the kings square to indicate this to the user. For the white king in check I created a flashing red border and for black king in check I created a blue border.

# Evaluation
# Code refactoring and REuse
During development I refactored the code in several areas for reusabiltiy for e.g the movement of the Queen in a chess game is the same as the rook and bishops moves added together as a Queen can move both diagonally like a bishop and up\down side/side like a rook. This meant I could refactor the code I wrote for checking valid bishop and rook moves for the queen.The end result being a concise check_queen function that reused the logic from my check_bishop and check_rook functions

# Advanced Programing Principles 
I used a variety of advanced programming principles in my code below I will be briefly going over some:
Object-Oriented Design (OOD): My game leverages OOD principles to encapsulate behaviors within classes, promoting modularity and ease of management. Each piece in the game is represented by a class (such as Pawn, Rook, Knight, etc.), which encapsulates the specific behavior and movement rules for that piece.

Encapsulation: By encapsulating the piece's attributes and behaviors (like movement rules and position) within their respective classes, the code adheres to OOD principles. This allows the game to manage pieces as distinct objects, each with their own states and methods.

Polymorphism: Polymorphism is used to allow different pieces to share a common interface (e.g., Piece class), but each piece implements its own version of certain behaviors, such as calculating valid moves. For instance, the get_valid_moves() method is defined differently for each piece but shares a common signature, allowing the game to handle all pieces generically while still respecting their unique rules.

Design Patterns:

State Pattern: The chess game employs the state pattern to manage the game's various states (such as waiting for input, processing moves, checking for a checkmate, etc.). The state pattern is particularly useful in scenarios where an object must change its behavior based on its state. For example, the game can be in different states such as:

WaitingForInput: The game is waiting for the player to select a piece or move.

ProcessingMove: The game is evaluating a move and updating the board.

GameOver: The game has ended, and a winner has been declared or a stalemate occurred.
By isolating the logic for each state, the game can more easily transition between states without mixing responsibilities, improving the separation of concerns.

Modularization and Separation of Concerns: The game is designed in a modular fashion, separating different functionalities into discrete components (classes and methods). For instance, the logic for managing the board (Board class), managing individual pieces (Piece subclasses), and handling the game loop and user input (Game class) are all clearly separated. This reduces complexity in any single part of the code, allowing each module to be independently developed, tested, and maintained.

Example: The Game class is responsible for handling high-level game logic such as player turns and win condition checks, while the Board class focuses solely on managing the pieces' positions and valid moves. This modular approach makes the code more flexible and easier to extend or modify.

# Feature Showcase and Innovations
Displaying Captured Pieces : Pieces that are captured are displayed on the side of the screen in a mini form,allowing players to keep track of the captured pieces.
Flashing King Square : A flashing square is applied to the king square when its placed in check to indicate to the user that their king is in danger.
Forfeit Functionality : A Forfeit button is on the lower right corner of the screen allowing for players to forfeit the game and restart. 

# Refelective Review & Future Improvements
Overall the game is playable and all the epics I have designed for the game were successfully completed, I was able to reuse code for e.g when creating the check_queen function that reuses code logic from the rook and bishop functions; aswell as use a state pattern to resolve the games logic. Looking back some things I could have done better is too add in a pop up text for when the king is in check , this was one of my initial ideas on indicating a checked king to the player . My current code just enables a flashing effect on the king once its in check in addition to this I could also add text saying “your king is check” to the bottom of the page to make it clearer to the player that the reason why their king is flashing is because the opponent has them in check. Another future improvement I can do is add the logic for pawn promotion ( this is when a pawn reaches the end of the board and can be promoted to another piece) . Evaluating my games overall impromance I would say its base functionality works and it has a solid turn by turn gameplay though it could be  improved by adding a computer vs player functionality where users can play against a chess ai instead of one another. 

