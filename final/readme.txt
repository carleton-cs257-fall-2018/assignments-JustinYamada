Conor Gormally and Justin Yamada

Brief Explanation:
Survival Reverse Pong: The game starts with the ball in the center of the screen, with an arrow depicting the motion of the ball’s travel. The player will place a number of horizontal barriers to prevent the ball from leaving the bottom of the box. If the ball leaves the bottom of the box the game is over. The goal of the game is to keep the ball from leaving the stage for as long as possible, where the score is determined by the time left. At the beginning of the game the user may decide the difficulty (number of bars to place), which acts as a multiplier for the score.

MVC Model:
The MVC model is necessary to both support both the internal structure and ease of use of our game. Our core model, consisting of ball and block objects that will interact within a grid using the mechanics set by the model. The model is responsible for the pong ball bouncing off a player generated wall. The controller is needed to respond to player inputs and updates the view so that the player can learn and watch the mechanics of the game. The view is needed to understand the difficulty settings and how the objects within the game interact. Our view for this game will be the game screen, consisting of a grid in which the game is played and areas designating rules, score, and difficulty. For example, by being able to see the game level, the player can see where to place blocks to keep the ball within the level. Without a view, the player could not interact properly with the game and use the controller.

Model Core Classes:
1)Ball: Gets and sets the velocity of how the ball moves.
2)Block: Has code on how blocks interact with ball (i.e. ball bounces off block)

