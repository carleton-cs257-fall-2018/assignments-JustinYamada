/**
 * Ball.java
 * Jeff Ondich, 10/29/14.
 *
 * A sample subclass of Sprite for CS257.
 */
package pong;

import javafx.fxml.FXML;
import javafx.scene.image.Image;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.ImagePattern;

public class Block extends Rectangle {

    public Block() {
        Image image = new Image("http://pixelartmaker.com/art/9a13872d51e52cf.png");
        setFill(new ImagePattern(image));
    }

}
