package com.jacky.spineanimationbuilder.Screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.PixmapIO;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.BufferUtils;
import com.badlogic.gdx.utils.ScreenUtils;
import com.esotericsoftware.spine.*;
import com.jacky.spineanimationbuilder.AnimationBuilder;
import com.jacky.spineanimationbuilder.SpineCharacter;
import com.sun.istack.internal.NotNull;

import javax.swing.*;
import javax.swing.filechooser.FileFilter;
import java.io.File;
import java.util.Scanner;

public class ShowScreen implements Screen {
    private final AnimationBuilder game;
    private final float[] bgColor;
    private final float scale;
    private SpineCharacter loader = null;
    private boolean firstStart = false;
    //private final SpineCharacter loader2;

    public String animation = "normal";


    OrthographicCamera camera;


    private SkeletonRenderer renderer = new SkeletonRenderer();

    private Array<Pixmap> files = new Array<Pixmap>();
    private String filename;


    public ShowScreen(AnimationBuilder game, float[] bgColor, float scale, int[] size) {
        this.game = game;
        this.bgColor = bgColor;
        this.scale = scale;

        camera = new OrthographicCamera();
        camera.setToOrtho(false, size[0], size[1]);


    }

    @Override
    public void show() {
    }

    @Override
    public void render(float delta) {
        if (firstStart) {
            delta = 0f;
            firstStart = false;
        }

        Gdx.gl.glClearColor(bgColor[0], bgColor[1], bgColor[2], bgColor[3]);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        camera.update();
        game.batch.getProjectionMatrix().set(camera.combined);


        if (loader != null) {
            Bone bone = loader.skeleton.findBone("leg_L");


            loader.state.update(delta);
            loader.state.apply(loader.skeleton);


            loader.skeleton.updateWorldTransform();

            game.batch.begin();
            renderer.draw(game.batch, loader.skeleton);
            game.batch.end();

            screenShort();
        }

        if (Gdx.input.isKeyPressed(Input.Keys.S) && Gdx.input.isKeyPressed(Input.Keys.CONTROL_LEFT))
            saveAll();

    }

    @Override
    public void resize(int width, int height) {
        camera.setToOrtho(false, width, height);
        loader.skeleton.setPosition(width / 2f, height / 4f);
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

    private void screenShort() {

        byte[] pixels = ScreenUtils.getFrameBufferPixels(0, 0, Gdx.graphics.getBackBufferWidth(), Gdx.graphics.getBackBufferHeight(), true);
        for (int i = 4; i < pixels.length; i += 4) {
            pixels[i - 1] = (byte) 255;
        }

        Pixmap pixmap = new Pixmap(Gdx.graphics.getBackBufferWidth(), Gdx.graphics.getBackBufferHeight(), Pixmap.Format.RGBA8888);
        BufferUtils.copy(pixels, 0, pixmap.getPixels(), pixels.length);
        files.add(pixmap);

    }

    public void saveAll() {
        String savePath;
        {
            JFileChooser chooser = new JFileChooser();
            chooser.setDialogTitle("保存序列图");
            chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
            chooser.setCurrentDirectory(new File(filename));

            chooser.showDialog(null, "选择文件夹");

            File file = chooser.getSelectedFile();
            if (file == null) return;
            savePath = file.getPath();

            int num = 0;
            for (Pixmap pixmap : files) {

                PixmapIO.writePNG(Gdx.files.absolute(savePath + "/" + num + ".png"), pixmap);
                pixmap.dispose();

                float ok = ((num) / (float) (files.size)) * 100.0f;
                System.out.printf("完成第%d个，当前进度%.2f%%\n", num, ok);

                num += 1;

            }
            System.out.println("done!,all finish");
            files.clear();
            System.exit(2);
        }


    }

    void setLoader(@NotNull String filename) {
        this.filename = filename;
        loader = new SpineCharacter(scale);

        FileHandle skelFile = Gdx.files.absolute(filename);
        FileHandle atlasFile = loader.findAtlasFile(skelFile);

        if (atlasFile == null || !atlasFile.exists()) {
            atlasFile = findAtlasFile();
        }

        loader.loadSkeleton(skelFile, atlasFile);

        loader.skeleton.setPosition(Gdx.graphics.getBackBufferWidth() / 2f, Gdx.graphics.getBackBufferHeight() / 4f);

        int num = 1;
        for (String animationName :
                loader.getAnimations()) {
            System.out.println(num + "). :--" + animationName);
            num += 1;
        }
        System.out.print("\n\t请选择动画：\t");

        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            loader.addAnimation(scanner.nextInt() - 1, true, 2);

        } else {
            loader.addAnimation(scanner.next(), true, 2, 0);
        }

        // System.out.println(loader.skeleton.getSlots());
        // System.out.println(loader.getAnimations());

        Bone bone_2 = loader.skeleton.findBone("hand_L2");
        bone_2.getData().setRotation(90);
        loader.skeleton.updateWorldTransform();

        firstStart = true;
    }

    private FileHandle findAtlasFile() {
        JFileChooser chooser = new JFileChooser();
        chooser.setDialogTitle("加载文件（Atlas）");
        chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        chooser.addChoosableFileFilter(new FileFilter() {
            @Override
            public boolean accept(File file) {
                String name = file.getName();
                return file.isDirectory() || name.toLowerCase().endsWith(".atlas") || name.toLowerCase().endsWith(".atlas.txt");

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
            if (filename.endsWith(".atlas.txt") || filename.endsWith(".atlas")) {
                return Gdx.files.absolute(filename);
            }
        }
        return null;
    }
}





