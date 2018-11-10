/**
 * Ball.java
 * Jeff Ondich, 10/29/14.
 *
 * A sample subclass of Sprite for CS257.
 */
package pong;

import javafx.fxml.FXML;
import javafx.scene.shape.Rectangle;

public class Block extends Rectangle {
    @FXML private double positionX;
    @FXML private double positionY;

    public Block() {
    }

    public double getPositionX() {
        return positionX;
    }

    public void setPositionX(double positionX) {
        this.positionX = positionX;
    }

    public double getPositionY() {
        return positionY;
    }

    public void setPositionY(double positionY) {
        this.positionY = positionY;
    }
}
