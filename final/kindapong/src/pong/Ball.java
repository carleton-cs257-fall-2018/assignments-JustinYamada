/**
 * Ball.java
 * Jeff Ondich, 10/29/14.
 *
 * A sample subclass of Sprite for CS257.
 */
package pong;

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

    public void step() {
        this.setCenterX(this.getCenterX() + this.velocityX);
        this.setCenterY(this.getCenterY() + this.velocityY);
    }

    public void resetLocation(double positionX, double positionY) {
        this.setCenterX(positionX);
        this.setCenterY(positionY);
    }

    public void randomVelocity(){
        Random random = new Random();

        this.setVelocityX((random.nextInt(10))-10);
        this.setVelocityY((random.nextInt(10))-10);
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
