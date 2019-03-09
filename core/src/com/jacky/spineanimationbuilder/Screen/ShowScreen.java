package com.jacky.spineanimationbuilder.Screen;

import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.TextureAtlas;
import com.esotericsoftware.spine.AnimationState;
import com.esotericsoftware.spine.Skeleton;
import com.esotericsoftware.spine.SkeletonRenderer;
import com.jacky.spineanimationbuilder.AnimationBuilder;
import com.jacky.spineanimationbuilder.spine.SpineLoader;

import java.awt.*;

public class ShowScreen implements Screen {
    private final AnimationBuilder game;
    private final SpineLoader loader;

    private Skeleton skeleton;
    private SkeletonRenderer renderer;
    private AnimationState state;
    private TextureAtlas atlas;

    private AnimationState.TrackEntry trackEntry;

    OrthographicCamera camera;

    int num=0;

    public ShowScreen(AnimationBuilder game)
    {this.game=game;
    this.loader=game.getLoader();

    this.atlas=loader.getAtlas();
    this.skeleton=loader.getSkeleton();
    this.state=loader.getState();
    this.renderer=new SkeletonRenderer();

    trackEntry=new AnimationState.TrackEntry();

    camera=new OrthographicCamera();
    camera.setToOrtho(false,512,512);



    }
    @Override
    public void show() {

    }

    @Override
    public void render(float delta) {
        Gdx.gl.glClearColor(1,1,1,1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        camera.update();
        game.batch.getProjectionMatrix().set(camera.combined);

        skeleton.setPosition(num,100);
        state.update(delta);
        state.apply(skeleton);

        state.setAnimation(0,"dance",true);
        state.setAnimation(0,"motou",true);
        skeleton.updateWorldTransform();

        game.batch.begin();
        renderer.draw(game.batch,skeleton);
        game.batch.end();

        num+=150*delta;

        if (num>=512)
            num=0;

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
}
