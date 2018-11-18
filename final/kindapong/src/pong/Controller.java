package pong;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;
import javafx.scene.shape.Circle;
import javafx.scene.image.*;

import java.awt.*;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.TimeUnit;
import java.lang.Math;

public class Controller implements EventHandler<KeyEvent> {
    private double FRAMES_PER_SECOND = 30.0;



    // This is part of the model
    @FXML private Ball ball;
    private int score;
    private boolean paused;
    private Timer timer;
    private int enterPressed = 0;
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
    @FXML private Block block5;
    @FXML private Block block6;





    public Controller() {
        this.paused = true;
        this.score = 0;
    }

    public void initialize() {
        this.controller = new Controller();

    }

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
        this.enterPressed = 0;
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

        this.block5.setLayoutX(400);
        this.block5.setLayoutY(400);
        this.block5.setX(0);
        this.block5.setY(0);


        this.block6.setLayoutX(500);
        this.block6.setLayoutY(400);
        this.block6.setX(0);
        this.block6.setY(0);


    }

    public int checkBounce(Block block) {
        double ballCenterX = this.ball.getCenterX() + this.ball.getLayoutX();
        double ballCenterY = this.ball.getCenterY() + this.ball.getLayoutY();
        double ballRadius = this.ball.getRadius();
        //Ball Bottom
        int bounceType = bouncePoints((ballCenterX), (ballCenterY + ballRadius), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Ball Lower-Left
        bounceType = bouncePoints((ballCenterX - (ballRadius/Math.sqrt(2))), (ballCenterY + (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0){

            return bounceType;
        }

        //Ball Left
        bounceType = bouncePoints((ballCenterX - ballRadius), (ballCenterY), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Ball Upper-Left
        bounceType = bouncePoints((ballCenterX - (ballRadius/Math.sqrt(2))), (ballCenterY - (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0 ){
            return bounceType;
        }

        //Ball Top
        bounceType = bouncePoints((ballCenterX), (ballCenterY - ballRadius), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Ball Upper Right
        bounceType = bouncePoints((ballCenterX + (ballRadius/Math.sqrt(2))), (ballCenterY - (ballRadius/Math.sqrt(2))), block);
        if(bounceType != 0){
            return bounceType;
        }

        //Ball Right
        bounceType = bouncePoints((ballCenterX + ballRadius), (ballCenterY), block);
        if(bounceType != 0){
            return bounceType;
        }

        bounceType = bouncePoints((ballCenterX + (ballRadius/Math.sqrt(2))), (ballCenterY + (ballRadius/Math.sqrt(2))), block);
        //Ball Lower Right
        if(bounceType != 0){
            return bounceType;
        }
        return bounceType;
    }

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


        if(checkBounce(block) == 1 || checkBounce(block2) == 1 || checkBounce(block3) == 1 || checkBounce(block4) == 1 || checkBounce(block5) == 1 || checkBounce(block6) == 1) {
            this.ball.setVelocityY(-this.ball.getVelocityY());
            this.score++;
            this.scoreLabel.setText(String.format("Bounces: %d", this.score));
        }

        if(checkBounce(block) == 2 || checkBounce(block2) == 2 || checkBounce(block3) == 2 || checkBounce(block4) == 2 || checkBounce(block5) == 2 || checkBounce(block6) == 2) {
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
            enterPressed++;
            keyEvent.consume();
        }
        if(enterPressed == 0){
            moveBlock(block, code, keyEvent);
        }
        if(enterPressed == 1) {
            moveBlock(block2, code, keyEvent);
        }
        if(enterPressed == 2) {
            moveBlock(block3, code, keyEvent);
        }
        if(enterPressed == 3) {
            moveBlock(block4, code, keyEvent);
        }
        if(enterPressed == 4) {
            moveBlock(block5, code, keyEvent);
        }
        if(enterPressed == 5) {
            moveBlock(block6, code, keyEvent);
        }

    }

    public void onPauseButton(ActionEvent actionEvent) {
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

    public void onSpeedUpButton(ActionEvent actionEvent) {
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




    public void onSpeedDownButton(ActionEvent actionEvent) {
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
