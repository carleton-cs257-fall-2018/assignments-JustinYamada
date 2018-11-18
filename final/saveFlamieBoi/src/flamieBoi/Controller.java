/**
 * @author Justin Yamada
 * @author Conor Gormally
 * @date November 19, 2018
 */

package flamieBoi;

import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;


import java.util.Timer;
import java.util.TimerTask;
import java.lang.Math;

public class Controller implements EventHandler<KeyEvent> {
    private double FRAMES_PER_SECOND = 30.0;



    // This is part of the model
    @FXML private Ball ball;
    private int score;
    private boolean paused;
    private Timer timer;
    private int shiftPressed = 0;
    private Controller controller;

    //This is part of the view
    @FXML private Label scoreLabel;
    @FXML private Label end;
    @FXML private AnchorPane gameBoard;
    @FXML private Button pauseButton;
    @FXML private Button speedUpButton;
    @FXML private Button speedDownButton;
    @FXML private Block block;
    @FXML private Block block2;
    @FXML private Block block3;
    @FXML private Block block4;




    public Controller() {
        this.paused = true;
        this.score = 0;
    }

    public void initialize() {
        this.controller = new Controller();

    }

    //Creates a Timer object whose task is to update the animation
    private void startTimer() {
        this.timer = new java.util.Timer();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                Platform.runLater(new Runnable() {
                    public void run() {
                        updateAnimation();
                    }
                });
            }
        };

        long frameTimeInMilliseconds = (long)(1000.0 / FRAMES_PER_SECOND);
        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
    }

    //Kills and recreates the timer object, resets the frames per second and locations of the ball and blocks
    private void gameOver(){
        this.timer.cancel();
        this.refresh();
        this.resetBlocks();
        this.resetBall();
        this.timer = new java.util.Timer();
        this.FRAMES_PER_SECOND = 30.0;
        this.pauseButton.setText("Restart");
    }

    public void refresh(){
        this.end.setText(String.format("GAME OVER   SCORE: %d", this.score));
        this.speedUpButton.setText("Speed-Up");
        this.speedDownButton.setText("Slow-Down");
        this.scoreLabel.setText(String.format(""));
        this.paused = true;
        this.score = 0;
        this.shiftPressed = 0;
    }

    public void resetBall(){
        this.ball.setVelocityY(0);
        this.ball.setVelocityX(0);
        this.ball.resetLocation(240,80);

    }

    public void resetBlocks() {

        this.block.setLayoutX(0);
        this.block.setLayoutY(400);
        this.block.setX(0);
        this.block.setY(0);

        this.block2.setLayoutX(100);
        this.block2.setLayoutY(400);
        this.block2.setX(0);
        this.block2.setY(0);


        this.block3.setLayoutX(200);
        this.block3.setLayoutY(400);
        this.block3.setX(0);
        this.block3.setY(0);



        this.block4.setLayoutX(300);
        this.block4.setLayoutY(400);
        this.block4.setX(0);
        this.block4.setY(0);


    }


    /**
     * Function that checks whether or not one of 8 points (N, NE, E, SE, S, SW, W, NW) on the ball has contacted the
     * top or side of a block
     *
     * @param block the block being checked
     * @return bounceType (off the side or the top of the block)
     */
    public int checkBounce(Block block) {
        double ballCenterX = this.ball.getCenterX() + this.ball.getLayoutX();
        double ballCenterY = this.ball.getCenterY() + this.ball.getLayoutY();
        double ballRadius = this.ball.getRadius();

        //bounceType is 0 if the ball does not contact the block, 1 if the ball contacts the surfaces, and 2 if
        //the ball contacts the sides
        int bounceType = bouncePoints((ballCenterX), (ballCenterY + ballRadius), block);

        //Checks if the bottom of the ball has bounced off a surface or side of the platform
        if(bounceType != 0){
            return bounceType;
        }

        //Checks if the lower left point of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX - (ballRadius/Math.sqrt(2))), (ballCenterY + (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0){

            return bounceType;
        }

        //Checks if the left-most point of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX - ballRadius), (ballCenterY), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Checks if the upper left point of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX - (ballRadius/Math.sqrt(2))), (ballCenterY - (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0 ){
            return bounceType;
        }

        //Checks if the top of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX), (ballCenterY - ballRadius), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Checks if the upper right point of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX + (ballRadius/Math.sqrt(2))), (ballCenterY - (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Checks if the right-most point of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX + ballRadius), (ballCenterY), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Checks if the lower right point of the ball has bounced off a surface or side of the platform
        bounceType = bouncePoints((ballCenterX + (ballRadius/Math.sqrt(2))), (ballCenterY + (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0){
            return bounceType;
        }
        return bounceType;
    }

    /**
     * Helper function for checkBounce, which takes in the block being checked and our calculated bounce points
     *
     * @param bouncePointX
     * @param bouncePointY
     * @param block
     * @return bounceType (off the side or the top of the block)
     */
    private int bouncePoints(double bouncePointX, double bouncePointY, Block block) {
        double blockTop = block.getY() + block.getLayoutY();
        double blockBottom = blockTop +  block.getHeight();


        double blockLeft = block.getX() + block.getLayoutX();
        double blockRight = blockLeft + block.getWidth();


        // Bounce off block
        if (bouncePointX >= blockLeft && bouncePointX <= blockRight) {
            if (bouncePointY == blockTop && this.ball.getVelocityY() > 0 || bouncePointY == blockBottom && this.ball.getVelocityY() < 0) {
                return 1;
            }
        }
        if(bouncePointY >= blockTop && bouncePointY <= blockBottom){
            if((this.ball.getVelocityX() > 0 && bouncePointX == blockLeft) || (this.ball.getVelocityX() < 0 && bouncePointX == blockRight)){
                return 2;
            }
        }
        return 0;
    }


    private void updateAnimation() {
        double ballCenterX = this.ball.getCenterX() + this.ball.getLayoutX();
        double ballCenterY = this.ball.getCenterY() + this.ball.getLayoutY();
        double ballRadius = this.ball.getRadius();

        //If the ball bounces off the top or bottom, we invert its Y velocity but retain the X
        if(checkBounce(block) == 1 || checkBounce(block2) == 1 || checkBounce(block3) == 1 || checkBounce(block4) == 1) {
            this.ball.setVelocityY(-this.ball.getVelocityY());
            this.score++;
            this.scoreLabel.setText(String.format("Bounces: %d", this.score));
        }

        //If the ball bounces off the top or bottom, we invert its X velocity but retain the Y
        if(checkBounce(block) == 2 || checkBounce(block2) == 2 || checkBounce(block3) == 2 || checkBounce(block4) == 2) {
            this.ball.setVelocityX(-this.ball.getVelocityX());
            this.score++;
            this.scoreLabel.setText(String.format("Bounces: %d", this.score));
        }

        // Bounce off walls
        double ballVelocityX = this.ball.getVelocityX();
        double ballVelocityY = this.ball.getVelocityY();
        if (ballCenterX + ballRadius >= this.gameBoard.getWidth() && ballVelocityX > 0) {
            this.ball.setVelocityX(-ballVelocityX);
        } else if (ballCenterX - ballRadius < 0 && ballVelocityX < 0) {
            this.ball.setVelocityX(-ballVelocityX);
        } else if (ballCenterY + ballRadius >= this.gameBoard.getHeight()) {
            this.gameOver();
        } else if (ballCenterY - ballRadius < 0 && ballVelocityY < 0) {
            this.ball.setVelocityY(-ballVelocityY);
        }

        // Move the sprite.
        this.ball.step();

    }

    /**
     * The helper function for our handle method, which takes in a particular block based on how many times shift has been
     * pressed - effectively freezing each block once it has been moved
     *
     * @param block The block being moved
     * @param code  the code from the handle method
     * @param keyEvent the keyEvent from the handle method
     */
    public void moveBlock(Block block, KeyCode code, KeyEvent keyEvent) {
        double blockPositionX = block.getLayoutX();
        double blockPositionY = block.getLayoutY();
        double stepSize = 10.0;

        if (code == KeyCode.LEFT || code == KeyCode.A) {
            // move block left
            if (blockPositionX > stepSize) {
                block.setLayoutX(block.getLayoutX() - stepSize);
            } else {
                block.setLayoutX(0);
            }
            keyEvent.consume();
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            // move block right
            if (blockPositionX + block.getWidth() + stepSize < this.gameBoard.getWidth()) {
                block.setLayoutX(block.getLayoutX() + stepSize);
            } else {
                block.setLayoutX(this.gameBoard.getWidth() - block.getWidth());
            }
            keyEvent.consume();
        } else if (code == KeyCode.DOWN || code == KeyCode.S) {
            // move block DOWN
            if (blockPositionY + block.getHeight() + stepSize < this.gameBoard.getHeight()) {
                block.setLayoutY(block.getLayoutY() + stepSize);
            } else {
                block.setLayoutY(this.gameBoard.getHeight() - block.getHeight());
            }
            keyEvent.consume();
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            // move block UP
            System.out.println(blockPositionY);
            System.out.println(stepSize);

            if (blockPositionY > stepSize) {
                block.setLayoutY(block.getLayoutY() - stepSize);
            } else {
                block.setLayoutY(0);
            }
            keyEvent.consume();
        }
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();
        if(code == KeyCode.SHIFT) {
            shiftPressed++;
            keyEvent.consume();
        }
        if(shiftPressed == 0){
            moveBlock(block, code, keyEvent);
        }
        if(shiftPressed == 1) {
            moveBlock(block2, code, keyEvent);
        }
        if(shiftPressed == 2) {
            moveBlock(block3, code, keyEvent);
        }
        if(shiftPressed == 3) {
            moveBlock(block4, code, keyEvent);
        }

    }


    public void onPauseButton() {
        if (this.paused && pauseButton.getText().equals("Restart")) {
            this.ball.randomVelocity();
            this.pauseButton.setText("Start");
            this.speedUpButton.setText("Speed-Up");
            this.speedDownButton.setText("Slow-Down");
            this.end.setText(String.format(""));
        } else if (this.paused) {
            this.pauseButton.setText("Pause");
            this.startTimer();
            this.paused = !this.paused;
        }
        else {
            this.pauseButton.setText("Continue");
            this.timer.cancel();
            this.paused = true;
        }

    }

    //Allows the user to manually increase the frame rate
    public void onSpeedUpButton() {
        if(!this.paused && FRAMES_PER_SECOND != 1000) {
            this.timer.cancel();
            this.FRAMES_PER_SECOND += 10;
            this.speedUpButton.setText("FPS: " + FRAMES_PER_SECOND);
            this.speedDownButton.setText("Slow-Down");
            startTimer();
        }

        if(this.paused && FRAMES_PER_SECOND != 1000) {
            this.FRAMES_PER_SECOND += 10;
            this.speedUpButton.setText("FPS: " + FRAMES_PER_SECOND);
            this.speedDownButton.setText("Slow-Down");
            startTimer();
            this.timer.cancel();
        }
    }



    //Allows the user to manually decrease the frame rate
    public void onSpeedDownButton() {
        if(!this.paused && FRAMES_PER_SECOND != 0) {
            this.timer.cancel();
            this.FRAMES_PER_SECOND -= 10;
            this.speedDownButton.setText("FPS: " + FRAMES_PER_SECOND);
            this.speedUpButton.setText("Speed-Up");
            startTimer();
        }

        if(this.paused && FRAMES_PER_SECOND != 0) {
            this.FRAMES_PER_SECOND -= 10;
            this.speedDownButton.setText("FPS: " + FRAMES_PER_SECOND);
            this.speedUpButton.setText("Speed-Up");
            startTimer();
            this.timer.cancel();
        }


    }
}
