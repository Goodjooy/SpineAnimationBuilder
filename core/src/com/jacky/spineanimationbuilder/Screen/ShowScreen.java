package com.jacky.spineanimationbuilder.Screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.*;
import com.badlogic.gdx.utils.*;
import com.esotericsoftware.spine.*;
import com.esotericsoftware.spine.attachments.Attachment;
import com.jacky.spineanimationbuilder.AnimationBuilder;
import com.jacky.spineanimationbuilder.AnimationWork.SubAnimations.SubAnimation;
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

    private int dd=1;
    private float angle=0;
    private float angleSpeed=-1.5f;
    private com.jacky.spineanimationbuilder.AnimationWork.Animation animation;

    private long millis=0;

    OrthographicCamera camera;


    private SkeletonRenderer renderer = new SkeletonRenderer();

    private Array<Pixmap> files = new Array<Pixmap>();
    private String filename;

    private boolean startScreenShort = false;


    public ShowScreen(AnimationBuilder game, float[] bgColor, float scale, int[] size) {
        this.game = game;
        this.bgColor = bgColor;
        this.scale = scale;

        camera = new OrthographicCamera();
        camera.setToOrtho(false, size[0], size[1]);


    }

    @Override
    public void show() {
        millis= TimeUtils.millis();
    }

    @Override
    public void render(float delta) {
        if (firstStart) {
            delta = 0f;
            firstStart = false;
        }
        if (startScreenShort)
            Gdx.gl.glClearColor(bgColor[0], bgColor[1], bgColor[2], bgColor[3]);
        else
            Gdx.gl.glClearColor(0, 0, 0, 0);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        camera.update();
        game.batch.getProjectionMatrix().set(camera.combined);


        if (loader != null) {
            Bone bone = loader.skeleton.findBone("face");

            if (startScreenShort) {


                loader.state.update(delta);
                loader.state.apply(loader.skeleton);
                loader.skeleton.updateWorldTransform();

                animation.update(delta);

            //   bone.setToSetupPose();
            //   angle += angleSpeed * delta;
            //   bone.setRotation(angle);
               loader.skeleton.updateWorldTransform();
//
//
            //   long time = TimeUtils.millis() - millis;
//
            //   if (time > 2000 && time <= 4000)
            //       angleSpeed = 1.5f;
            //   else if (time > 4000&&time<=6000)
            //       angleSpeed = -1.5f;
            //   else if(time>6000){
            //       angleSpeed = 1.5f;
            //       millis=TimeUtils.millis();
               //}

              // System.out.println(angleSpeed);
            }

            game.batch.begin();
            renderer.draw(game.batch, loader.skeleton);
            game.batch.end();
           if (startScreenShort)
               screenShort();
        }


        if (Gdx.input.isKeyPressed(Input.Keys.S) && Gdx.input.isKeyPressed(Input.Keys.CONTROL_LEFT))
            saveAll();
        // camera.translate(90*delta,90*delta);
        if (Gdx.input.isKeyPressed(Input.Keys.UP))
            camera.translate(0, -150 * delta);
        if (Gdx.input.isKeyPressed(Input.Keys.DOWN))
            camera.translate(0, 150 * delta);
        if (Gdx.input.isKeyPressed(Input.Keys.LEFT))
            camera.translate(150 * delta, 0);
        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT))
            camera.translate(-150 * delta, 0);

        if (Gdx.input.isKeyPressed(Input.Keys.Q))
            camera.rotate(90 * delta);
        if (Gdx.input.isKeyPressed(Input.Keys.E))
            camera.rotate(-90 * delta);

        if (Gdx.input.isKeyPressed(Input.Keys.G)) {
            millis = TimeUtils.millis();
            startScreenShort = true;
        }
        if (Gdx.input.isKeyPressed(Input.Keys.H))
            startScreenShort = false;

        if (Gdx.input.isKeyPressed(Input.Keys.R))
            camera.setToOrtho(false);

        if (Gdx.input.isKeyPressed(Input.Keys.ESCAPE))
            addAnimation();


        if (Gdx.input.isKeyPressed(Input.Keys.F1) && Gdx.input.isKeyPressed(Input.Keys.CONTROL_RIGHT))
            System.exit('e');
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

        }

        System.out.println("\n还要添加动画吗（y/n）");
        Scanner scanner = new Scanner(System.in);
        if (scanner.next().equals("y")) {
            firstStart = true;
            addAnimation();
        } else System.exit('t');


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


        addAnimation();
        appendAnimation();

        // System.out.println(loader.skeleton.getSlots());
        // System.out.println(loader.getAnimations());

        // Bone bone_2 = loader.skeleton.findBone("hand_L2");
        // bone_2.getData().setRotation(90);
        // loader.skeleton.updateWorldTransform();
        System.out.println(loader.skeleton.getBones());
       // bigTexture(2.5f);

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

    private void addAnimation() {
        startScreenShort=false;
        loader.state.clearTracks();
        loader.clearAction();
        int num = 1;
        for (String animationName :
                loader.getAnimations()) {
            System.out.println(num + "). :--" + animationName);
            num += 1;
        }
        System.out.print("\n\t请选择动画：\t");
        boolean isAdd = true;
        while (isAdd) {


            Scanner scanner = new Scanner(System.in);
            if (scanner.hasNextInt()) {
                loader.addAnimation(scanner.nextInt() - 1, true, 0);

            } else {
                loader.addAnimation(scanner.next(), true, 0, 0);
            }
            System.out.print("当前动画\n\n\t");
            Array<AnimationState.TrackEntry> trackEntries = loader.getAction();
            for (AnimationState.TrackEntry entry : trackEntries) {
                System.out.print(entry + "->");
            }
            System.out.println("END");
            System.out.println("还要添加动画吗（y/n）");
            isAdd = scanner.next().equals("y");
        }

        Array<AnimationState.TrackEntry> trackEntries = loader.getAction();
        for (AnimationState.TrackEntry entry : trackEntries) {
            System.out.print(entry + "->");
        }
        System.out.println("END\n");

        System.out.println("Animation is real!");
        firstStart=true;
    }

   private void appendAnimation() {
       animation = new com.jacky.spineanimationbuilder.AnimationWork.Animation();

       SubAnimation subAnimation = new SubAnimation();
       subAnimation.setBone(loader.skeleton.findBone("root"));
       subAnimation.setAutoBack(true);
       subAnimation.setDelay(0);
       subAnimation.setBaseOnAnimation(true);
       subAnimation.setLoop(false);
       subAnimation.setRotate(25);
       subAnimation.setScaleY(2.5f);
       subAnimation.setScaleX(2.5f);
       subAnimation.setTime(5);
       subAnimation.realToSetUp();

       SubAnimation subAnimation1=new SubAnimation();
       subAnimation1.setBone(loader.skeleton.findBone("root"));
       subAnimation1.setAutoBack(true);
       subAnimation1.setDelay(subAnimation.getKeepTime());
       subAnimation.setBaseOnAnimation(true);
       subAnimation1.setLoop(false);
       subAnimation1.setRotate(-25);
       subAnimation1.setScaleY(2.5f);
       subAnimation1.setScaleX(2.5f);
       subAnimation1.setTime(5);
       subAnimation1.realToSetUp();


       animation.addSubAnimation(subAnimation);
       animation.addSubAnimation(subAnimation1);
       animation.realToGo();

   }
  private void rand(){
      Array<Slot> slotArray=loader.skeleton.getDrawOrder();
      for (Slot slot : slotArray) {
          Attachment attachment=slot.getAttachment();

         // TextureAtlas.AtlasRegion region=loader.skeleton;
          FloatArray val = slot.getAttachmentVertices();
          float[]vertices=new float[val.size];
          for (int i = 0; i < vertices.length; i++) {
              vertices[i]=val.get(i);
          }
          slot.getAttachmentVertices();
          short[]triangles=new short[10];
          //triangles
          Pixmap pixmap=new Pixmap(10,10, Pixmap.Format.RGBA8888);
          pixmap.setColor(1,1,1,0);
          pixmap.fill();

          Texture texture =new Texture(pixmap);


          texture.getTextureData().consumePixmap();
          game.batch.draw(texture, vertices,0,vertices.length,triangles,0,triangles.length);
      }
  }
}




