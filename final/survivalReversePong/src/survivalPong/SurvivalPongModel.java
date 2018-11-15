package survivalPong;

import javafx.application.Platform;
import javafx.fxml.FXML;

import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;


public class SurvivalPongModel {

    private boolean gameOver;
    private int score;
    private int difficulty;
    public Timer timer;
    final private double FRAMES_PER_SECOND = 20.0;

    public SurvivalPongModel(int difficulty) {
        this.startNewGameWithDifficulty(difficulty);
    }

    /**
     * @param difficulty the user chosen hardness of the game with directly
     *                   correlates with the number of blocks
     */

    public void startNewGameWithDifficulty(int difficulty) {
        this.gameOver = false;
        this.score = 0;
        this.difficulty = difficulty;
        this.startTimer();
    }


    public void startTimer() {
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


    public boolean isGameOver() {
        return this.gameOver;
    }

    private int setDifficulty() {
        return this.difficulty;
    }

    public int getScore() {
        return this.score;
    }

    //mechanics of ball movement
    public void moveBall() {
    }

    //mechanics of user generated block movement, called by controller
    public void moveBlock() {
    }

    //locks user generated block in place
    public void freezeBlock() {
    }

    //spawns another block for the users to place after finalization
    //of previous block
    public void spawnNewBlock() {
    }

    public void bounceBallOffBlock() {
    }

    public void bounceBallOffWall() {
    }

}
