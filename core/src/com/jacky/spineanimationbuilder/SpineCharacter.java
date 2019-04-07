package com.jacky.spineanimationbuilder;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.TextureAtlas;
import com.badlogic.gdx.utils.Array;
import com.esotericsoftware.spine.*;

public class SpineCharacter {

    private  float scale=1.0f;
    public Skeleton skeleton;
    public SkeletonData skeletonData;

    private FileHandle skeletonFile;

    private TextureAtlas atlas;

    public AnimationState state;

    private Array<String> animations = new Array<String>();
    private Array<String> skins = new Array<String>();
    private Array<AnimationState.TrackEntry> action=new Array<AnimationState.TrackEntry>();

    private int index=0;

    private float time=0;

    public SpineCharacter(float scale){
        this.scale=scale;
    }
    public SpineCharacter(){}

    public void loadSkeleton(final String skeletonFile,final String atlasFile){
        FileHandle skeleton =Gdx.files.absolute(skeletonFile);
        System.out.println(skeleton.exists());
        loadSkeleton(skeleton,Gdx.files.absolute(atlasFile));
    }

    public void loadSkeleton(final FileHandle skeletonFile,final FileHandle atlasFile) {
        Pixmap pixmap = new Pixmap(32, 32, Pixmap.Format.RGBA8888);
        pixmap.setColor(new Color(1f, 1f, 1f, 1f));
        pixmap.fill();
        final TextureAtlas.AtlasRegion fake = new TextureAtlas.AtlasRegion(new Texture(pixmap), 0, 0, 32, 32);
        pixmap.dispose();
        if (skeletonFile != null) {
            String skeletonFileName = skeletonFile.name();
            if ((skeletonFileName.endsWith(".skel.txt") || skeletonFileName.endsWith(".skel")) && skeletonFile.exists()) {
                //load atlas file

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
                binary.setScale(scale);
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
                     //   System.out.println(event.toString() + "  " + entry.toString());
                        super.event(entry, event);
                    }
                });

                this.skeletonFile = skeletonFile;

                //load skin and animation
                for (Animation animation : skeletonData.getAnimations())
                    animations.add(animation.getName());
                for (Skin skin : skeletonData.getSkins())
                    skins.add(skin.getName());

                System.out.printf("\n\n----load %s, done.----\n\n",skeletonData.getName());
            }

        }
    }

    public AnimationState.TrackEntry addAnimation(String animation,boolean loop,float delay,int index){
        AnimationState.TrackEntry trackEntry=state.addAnimation(this.index,animation,loop,delay);
        trackEntry.setMixDuration(trackEntry.getAnimationEnd()-trackEntry.getAnimationStart());
        time+=trackEntry.getAnimationTime();
        //action.add(trackEntry);
        this.index=trackEntry.getTrackIndex();
        this.action.add(trackEntry);
        return trackEntry;
    }
    public AnimationState.TrackEntry addAnimation(Animation animation,boolean loop,float delay){
        AnimationState.TrackEntry trackEntry=state.addAnimation(index,animation,loop,delay);
        trackEntry.setMixDuration(trackEntry.getAnimationEnd()-trackEntry.getAnimationStart());
        //action.add(trackEntry);
        this.index+=1;
        this.action.add(trackEntry);
        return trackEntry;
    }
    public AnimationState.TrackEntry addAnimation(int index,boolean loop,float delay){
        AnimationState.TrackEntry trackEntry=state.addAnimation(this.index,animations.get(index),loop,delay);
        trackEntry.setMixDuration(trackEntry.getAnimationEnd()-trackEntry.getAnimationStart());
        time+=trackEntry.getAnimationTime();
        //action.add(trackEntry);
        this.index=trackEntry.getTrackIndex();
        this.action.add(trackEntry);
        return trackEntry;
    }
    public FileHandle findAtlasFile(final FileHandle skeletonFile) {
        String skeletonFileName=skeletonFile.name();
        String path = skeletonFileName.substring(0, skeletonFileName.length() -
                (skeletonFileName.endsWith(".skel.txt") ? 9 : 5)) + ".atlas.txt";
        FileHandle atlasFile = skeletonFile.sibling(path);
        if (!atlasFile.exists())
            atlasFile = skeletonFile.sibling(path.replace(".txt",""));
        return atlasFile;
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

    public Array<String> getAnimations() {
        return animations;
    }

    public Array<String> getSkins() {
        return skins;
    }

    public float getTime() {
        return time;
    }

    public Array<AnimationState.TrackEntry> getAction() {
        return action;
    }
    public  void clearAction(){
        action.clear();
    }
}
