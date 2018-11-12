package survivalPong;

import java.util.Random;

public class survivalPongModel {

    private boolean gameOver;
    private int score;
    private int difficulty;

    public survivalPongModel(int difficulty) {
        this.startNewGameWithDifficulty(difficulty);
    }

    //begins the game 
    public void startNewGameWithDifficulty(int difficulty) {
        this.gameOver = false;
        this.score = 0;
        this.difficulty = difficulty;
        this.initializeLevel();
    }

    public boolean isGameOver() {
        return this.gameOver;
    }

    private void initializeLevel() {
    }

    private int setDifficulty(){
        return this.difficulty;
    }

    public int getScore() {
        return this.score;
    }

    public void moveBall() {
    }

    public void moveBlock() {
    }

    public void freezeBlock() {
    }

    public void spawnNewBlock() {
    }

    public void bounceBallOffBlock() {
    }

    public void bounceBallOffWall(){
    }
