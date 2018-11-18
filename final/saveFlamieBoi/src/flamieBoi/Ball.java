/**
 * Ball.java
 * @author Justin Yamada
 * @author Conor Gormally
 * @date November 18, 2018
 *
 * A subclass of circle to set and get the ball velocity. This class also changes
 * the sprite of the ball in the view model.
 */
package flamieBoi;

import javafx.fxml.FXML;
import javafx.scene.image.Image;
import javafx.scene.shape.Circle;
import javafx.scene.paint.ImagePattern;
import java.util.Random;


public class Ball extends Circle {
    @FXML private double velocityX;
    @FXML private double velocityY;


    public Ball() {
        Image image = new Image("http://pixelartmaker.com/art/156e827f7ec4ced.png");
        setFill(new ImagePattern(image));
    }

    //denotes how much the ball should move based on its current velocity

    public void step() {
        this.setCenterX(this.getCenterX() + this.velocityX);
        this.setCenterY(this.getCenterY() + this.velocityY);
    }

    /**
     *
     * @param positionX X coordinate to set
     * @param positionY Y coordinate to set
     */
    public void resetLocation(double positionX, double positionY) {
        this.setCenterX(positionX);
        this.setCenterY(positionY);
    }

    //sets a random velocity and applies it to the ball
    public void randomVelocity(){
        Random random = new Random();

        this.setVelocityX((random.nextInt(10)) -10);
        this.setVelocityY((random.nextInt(10)) -10);
        if(this.getVelocityX() == 0 || this.getVelocityX()%2 != 0 || this.getVelocityY() == 0 || this.getVelocityY()%2 != 0) {
            this.randomVelocity();
        }
    }

    public double getVelocityX() {
        return velocityX;
    }

    public void setVelocityX(double velocityX) {
        this.velocityX = velocityX;
    }

    public double getVelocityY() {
        return velocityY;
    }

    public void setVelocityY(double velocityY) {
        this.velocityY = velocityY;
    }
}
