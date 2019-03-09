package com.jacky.spineanimationbuilder.spine;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.PixmapIO;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.TextureAtlas;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.utils.Array;
import com.esotericsoftware.spine.*;
import com.sun.istack.internal.NotNull;

public class SpineLoader {

    private Skeleton skeleton;
    private SkeletonData skeletonData;

    private FileHandle skeletonFile;

    private TextureAtlas atlas;

    private AnimationState state;

    private Array<Animation> animations = new Array<Animation>();
    private Array<Skin> skins = new Array<Skin>();

    final TextureAtlas.AtlasRegion fake;

    public SpineLoader() {
        Pixmap pixmap = new Pixmap(32, 32, Pixmap.Format.RGBA8888);
        pixmap.setColor(new Color(1f, 1f, 1f, 1f));
        pixmap.fill();
        fake = new TextureAtlas.AtlasRegion(new Texture(pixmap), 0, 0, 32, 32);
        pixmap.dispose();
    }


    public void loadSkeleton(final FileHandle skeletonFile) {
        if (skeletonFile!=null){
            String skeletonFileName = skeletonFile.name();
            if ((skeletonFileName.endsWith(".skel.txt")||skeletonFileName.endsWith(".skel")) && skeletonFile.exists()) {
                //load atlas file
                String path=skeletonFileName.substring(0, skeletonFileName.length() -
                        (skeletonFileName.endsWith(".skel.txt")?9:5)) + ".atlas.txt";
                FileHandle atlasFile = skeletonFile.sibling(path);

                //FileHandle data = !atlasFile.exists() ?
                //      null : atlasFile

                atlas = new TextureAtlas(atlasFile) {
                    @Override
                    public AtlasRegion findRegion(String name) {
                        //System.out.println(name);
                        AtlasRegion region = super.findRegion(name);
                        if (region == null) {
                            // Look for separate image file.
                            //寻找单独图片
                            FileHandle file = skeletonFile.sibling(name + ".png");
                            //如果找到了
                            if (file.exists()) {
                                //载入为贴图
                                Texture texture = new Texture(file);
                                //设置滤波
                                texture.setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
                                //新建为新的方位集
                                region = new AtlasRegion(texture, 0, 0, texture.getWidth(), texture.getHeight());
                                //赋值 name
                                region.name = name;
                            }
                        }
                        return region != null ? region : fake;
                    }
                };
                SkeletonBinary binary = new SkeletonBinary(atlas);
                binary.setScale(0.5f);
                skeletonData = new SkeletonData();
                skeletonData = binary.readSkeletonData(skeletonFile);

                if (skeletonData.getBones().size == 0) {
                    System.out.println("没有骨骼信息");
                    return;
                }

                skeleton = new Skeleton(skeletonData);
                skeleton.updateWorldTransform();
                skeleton = new Skeleton(skeleton);
                skeleton.updateWorldTransform();

                state = new AnimationState(new AnimationStateData(skeletonData));

                state.addListener(new AnimationState.AnimationStateAdapter() {
                    @Override
                    public void event(AnimationState.TrackEntry entry, Event event) {
                        System.out.println(event.toString() + "  " + entry.toString());
                        super.event(entry, event);
                    }
                });

                this.skeletonFile = skeletonFile;

                //load skin and animation
                for (Animation animation : skeletonData.getAnimations())
                    animations.add(animation);
                for (Skin skin : skeletonData.getSkins())
                    skins.add(skin);
                System.out.println(animations);
                System.out.println("done.");
            }

        }
    }

    public Skeleton getSkeleton() {
        return skeleton;
    }

    public AnimationState getState() {
        return state;
    }

    public TextureAtlas getAtlas() {
        return atlas;
    }
}
