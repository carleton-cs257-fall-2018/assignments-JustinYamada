package survivalPongs;

public class Controller {

  public void initialize() {
  }

  private int score;
  private boolean paused;

  public Controller() {
      this.paused = false;
      this.score = 0;
  }

  public void updateScore(){

  }

  @Override
  public void handle(KeyEvent keyEvent) {
      KeyCode code = keyEvent.getCode();
      double paddlePosition = this.paddle.getLayoutX();
      double stepSize = 15.0;
      if (code == KeyCode.LEFT || code == KeyCode.A) {
          // move paddle left
          if (paddlePosition > stepSize) {
              this.paddle.setLayoutX(this.paddle.getLayoutX() - stepSize);
          } else {
              this.paddle.setLayoutX(0);
          }
          keyEvent.consume();
      } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
          // move paddle right
          if (paddlePosition + this.paddle.getWidth() + stepSize < this.gameBoard.getWidth()) {
              this.paddle.setLayoutX(this.paddle.getLayoutX() + stepSize);
          } else {
              this.paddle.setLayoutX(this.gameBoard.getWidth() - this.paddle.getWidth());
          }
          keyEvent.consume();
      }
  }

  public void onPauseButton(ActionEvent actionEvent) {
      if (this.paused) {
          this.pauseButton.setText("Pause");
          this.startTimer();
      } else {
          this.pauseButton.setText("Continue");
          this.timer.cancel();
      }
      this.paused = !this.paused;
  }
}
