/**
 * Main.java
 * @author Justin Yamada
 * @author Conor Gormally
 * @date November 18, 2018
 *
 * The main program for a pong-like program in JavaFX. The goal
 * of the game is to keep the bouncing flame within the screen
 * using the 4 blocks of grass.
 */

package pong;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

public class Main extends Application {

    /**
     *
     * @param primaryStage
     * @throws Exception
     */
    @Override
    public void start(Stage primaryStage) throws Exception{
        primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
            @Override
            public void handle(WindowEvent t) {
                Platform.exit();
                System.exit(0);
            }
        });

        FXMLLoader loader = new FXMLLoader(getClass().getResource("pong.fxml"));
        Parent root = (Parent)loader.load();
        Controller controller = loader.getController();

        //title of stage
        primaryStage.setTitle("Keep Flame Boi Alive");

        //sets the scene to be 700 by 500 pixels
        Scene scene = new Scene(root, 700, 500);
        primaryStage.setScene(scene);

        //if key stroke taken in send key stroke to controller
        scene.setOnKeyPressed(controller);
        primaryStage.show();

        root.requestFocus();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
