Conor Gormally and Justin Yamada

Final Note: 
The game works and looks a lot better than we actually thought it would, which we're proud of. We also ended up following down our original plan for a bouncing algorithm, which doesn't work quite as well as we'd like, but works the significant majority of the time. The game resets and can be restarted, and we added buttons that allow the user to speed up and slow down the frame rate (effectively changing the viewed speed of the ball). After ~20-25 hours of work, we didn't have any more time to implement difficulty or drawing the arrow in the direction of the ball's movement, but it's kind of fun to have a ball with an unknown starting direction; we think it makes the game more difficult and fun. Thanks for all your help and great term! 

Brief Explanation:
Survival Reverse Pong: The game starts with the ball in the center of the screen, with an arrow depicting the motion of the ball’s travel. The player will place a number of horizontal barriers to prevent the ball from leaving the bottom of the box. If the ball leaves the bottom of the box the game is over. The goal of the game is to keep the ball from leaving the stage for as long as possible, where the score is determined by the time left. At the beginning of the game the user may decide the difficulty (number of bars to place), which acts as a multiplier for the score.

MVC Model:
The MVC model is necessary to both support both the internal structure and ease of use of our game. Our core model, consisting of ball and block objects that will interact within a grid using the mechanics set by the model. The model is responsible for the pong ball bouncing off a player generated wall. The controller is needed to respond to player inputs and updates the view so that the player can learn and watch the mechanics of the game. The view is needed to understand the difficulty settings and how the objects within the game interact. Our view for this game will be the game screen, consisting of a grid in which the game is played and areas designating rules, score, and difficulty. For example, by being able to see the game level, the player can see where to place blocks to keep the ball within the level. Without a view, the player could not interact properly with the game and use the controller.

Model Core Classes:
1)Ball: Gets and sets the velocity of how the ball moves.
2)Block: Has code on how blocks interact with ball (i.e. when and how the ball bounces off block)
3)Main: launches the game
4)SurvivalPongModel: contains the mechanics for the interaction of the ball with the blocks and the walls of the view
5)SurvivalPongView: creates the view that the player interfaces with. Includes playing grid as well as title, control, settings, and description area
6)Controller: Handles player input and updates the view
