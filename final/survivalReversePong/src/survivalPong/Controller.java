package survivalPong;

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

import java.util.Timer;
import java.util.TimerTask;

public class Controller implements EventHandler<KeyEvent> {

    final private double FRAMES_PER_SECOND = 20.0;

    @FXML private Button pauseButton;
    @FXML private Label scoreLabel;
    @FXML private AnchorPane gameBoard;
    @FXML private Rectangle paddle;
    @FXML private Ball ball;
    @FXML private SurvivalPongView survivalPongView;
    private SurvivalPongModel survivalPongModel;

    private int score;
    private boolean paused;

    public Controller() {
        this.paused = false;
        this.score = 0;
    }

    public void initialize() {
        this.survivalPongModel = new SurvivalPongModel(3);
    }

    public void updateScore() {
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();
        double paddlePositionX = this.paddle.getLayoutX();
        double paddlePositionY = this.paddle.getLayoutY();
        double stepSize = 15.0;
        string word = "paddle";

        if (code == KeyCode.LEFT || code == KeyCode.A) {
            // move paddle left
            if (paddlePositionX > stepSize) {
                this.paddle.setLayoutX(this.paddle.getLayoutX() - stepSize);
            } else {
                this.paddle.setLayoutX(0);
            }
            keyEvent.consume();
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            // move paddle right
            if (paddlePositionX + this.paddle.getWidth() + stepSize < this.gameBoard.getWidth()) {
                this.paddle.setLayoutX(this.paddle.getLayoutX() + stepSize);
            } else {
                this.paddle.setLayoutX(this.gameBoard.getWidth() - this.paddle.getWidth());
            }
            keyEvent.consume();
        } else if (code == KeyCode.DOWN || code == KeyCode.S) {
            // move paddle up
            if (paddlePositionY + this.paddle.getHeight() + stepSize < this.gameBoard.getHeight()) {
                this.paddle.setLayoutY(this.paddle.getLayoutY() + stepSize);
            } else {
                this.paddle.setLayoutY(this.gameBoard.getHeight() - this.paddle.getHeight());
            }
            keyEvent.consume();
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            // move paddle Down
            if (paddlePositionY > stepSize) {
                this.paddle.setLayoutY(this.paddle.getLayoutY() - stepSize);
            } else {
                this.paddle.setLayoutY(0);
            }
            keyEvent.consume();
        }

    }

    public void onPauseButton(ActionEvent actionEvent) {
      if (this.paused) {
          this.pauseButton.setText("Pause");
          survivalPongView.startTimer();
      } else {
          this.pauseButton.setText("Continue");
          this.survivalPongView.timer.cancel();
      }
      this.paused = !this.paused;
  }
}

