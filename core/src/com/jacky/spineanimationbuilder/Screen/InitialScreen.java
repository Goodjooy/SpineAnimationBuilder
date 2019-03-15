package com.jacky.spineanimationbuilder.Screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.jacky.spineanimationbuilder.AnimationBuilder;

import javax.swing.*;
import javax.swing.filechooser.FileFilter;
import java.io.File;

public class InitialScreen implements Screen {
    AnimationBuilder game;

    OrthographicCamera camera;

    int index = 0;
    private String filename;
    private boolean isOpen = false;

    public InitialScreen(AnimationBuilder game) {
        this.game = game;
    }

    @Override
    public void show() {
        camera = new OrthographicCamera();
        camera.setToOrtho(false, 1024, 1024);
    }

    @Override
    public void render(float delta) {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        if (isOpen) {
            game.showScreen.setLoader(filename);
            game.setScreen(game.showScreen);
        }


        if (Gdx.input.isKeyPressed(Input.Keys.CONTROL_LEFT) && Gdx.input.isKeyPressed(Input.Keys.L)) {
            JFileChooser chooser = new JFileChooser();
            chooser.setDialogTitle("加载文件（skel）");
            chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
            chooser.addChoosableFileFilter(new FileFilter() {
                @Override
                public boolean accept(File file) {
                    String name = file.getName();
                    return file.isDirectory() || name.toLowerCase().endsWith(".skel") || name.toLowerCase().endsWith(".skel.txt");

                }

                @Override
                public String getDescription() {
                    return "*.atlas;*.atlas.txt";
                }
            });

            chooser.showOpenDialog(null);

            File file = chooser.getSelectedFile();

            if (file != null && file.exists()) {
                filename = file.getAbsolutePath();
                if (filename.endsWith(".skel.txt") || filename.endsWith(".skel")) {
                    isOpen = true;
                }
            }
        }

    }

    @Override
    public void resize(int width, int height) {

    }

    @Override
    public void pause() {

    }

    @Override
    public void resume() {

    }

    @Override
    public void hide() {

    }

    @Override
    public void dispose() {

    }

    public String getFilename() {
        return filename;
    }
}
