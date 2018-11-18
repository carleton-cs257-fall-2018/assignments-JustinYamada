/**
 * Block.java
 * @author Justin Yamada
 * @author Conor Gormally
 * @date November 18, 2018
 *
 * A subclass of rectangle for the sprites of the blocks.
 */
package pong;

import javafx.scene.image.Image;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.ImagePattern;

public class Block extends Rectangle {

    public Block() {
        Image image = new Image("http://pixelartmaker.com/art/9a13872d51e52cf.png");
        setFill(new ImagePattern(image));
    }

}
