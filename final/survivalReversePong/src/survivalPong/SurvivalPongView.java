package survivalPong;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;
import javafx.scene.Group;

import java.util.Timer;
import java.util.TimerTask;

public class SurvivalPongView extends Group {
    final private double FRAMES_PER_SECOND = 20.0;

  @FXML private Ball ball;
  @FXML private Rectangle paddle;
  @FXML private Label scoreLabel;
  @FXML private AnchorPane gameBoard;

  private int score;

  public SurvivalPongView() {
  }


  //updates animation of ball and blocks walls
  private void updateAnimation() {
      double ballCenterX = this.ball.getCenterX() + this.ball.getLayoutX();
      double ballCenterY = this.ball.getCenterY() + this.ball.getLayoutY();
      double ballRadius = this.ball.getRadius();
      double paddleTop = this.paddle.getY() + this.paddle.getLayoutY();
      double paddleBottom = paddleTop + this.paddle.getHeight();


      double paddleLeft = this.paddle.getX() + this.paddle.getLayoutX();
      double paddleRight = paddleLeft + this.paddle.getWidth();


      // Bounce off paddle. NOTE: THIS IS A BAD BOUNCING ALGORITHM. The ball can badly
      // overshoot the paddle and still "bounce" off it. See if you can come up with
      // something better.
      if (ballCenterX >= paddleLeft && ballCenterX < paddleRight) {
          double ballBottom = ballCenterY + ballRadius;
          double ballTop = ballCenterY - ballRadius;

          if (ballBottom == paddleTop && this.ball.getVelocityY() > 0 || ballTop == paddleBottom && this.ball.getVelocityY() < 0) {
              this.ball.setVelocityY(-this.ball.getVelocityY());
              this.score++;
              this.scoreLabel.setText(String.format("Bounces: %d", this.score));
          }
      }

      // Bounce off walls
      double ballVelocityX = this.ball.getVelocityX();
      double ballVelocityY = this.ball.getVelocityY();
      if (ballCenterX + ballRadius >= this.gameBoard.getWidth() && ballVelocityX > 0) {
          this.ball.setVelocityX(-ballVelocityX);
      } else if (ballCenterX - ballRadius < 0 && ballVelocityX < 0) {
          this.ball.setVelocityX(-ballVelocityX);
      } else if (ballCenterY + ballRadius >= this.gameBoard.getHeight() && ballVelocityY > 0) {
          this.ball.setVelocityY(-ballVelocityY);
      } else if (ballCenterY - ballRadius < 0 && ballVelocityY < 0) {
          this.ball.setVelocityY(-ballVelocityY);
      }

      // Move the sprite.
      this.ball.step();
  }


}
