package survivalPong;

import java.util.Random;

public class survivalPongModel {

    private boolean gameOver;
    private int score;
    private int difficulty;

    public survivalPongModel(int difficulty) {
        this.startNewGameWithDifficulty(difficulty);
    }

    /**
    * @param difficulty the user chosen hardness of the game with directly
    * correlates with the number of blocks
    */
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

    public void bounceBallOffWall(){
    }
