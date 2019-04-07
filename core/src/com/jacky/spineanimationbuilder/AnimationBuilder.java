package com.jacky.spineanimationbuilder;

import com.badlogic.gdx.Game;
import com.badlogic.gdx.utils.Array;
import com.esotericsoftware.spine.utils.TwoColorPolygonBatch;
import com.jacky.spineanimationbuilder.Screen.InitialScreen;
import com.jacky.spineanimationbuilder.Screen.LoadScreen;
import com.jacky.spineanimationbuilder.Screen.ShowScreen;

public class AnimationBuilder extends Game {
    public final float[] bgColor;
    private final float scale;
    private final int[] size = new int[2];

    public TwoColorPolygonBatch batch;

    public ShowScreen showScreen;
    public InitialScreen initialScreen;
    public LoadScreen loadScreen;

    private String[ ]arg;

    public AnimationBuilder(String[] arg, float[] bgColor, float scale, int width, int height) {
        this.arg =arg;

        this.bgColor = bgColor;
        this.scale = scale;
        this.size[0] = width;
        this.size[1] = height;

    }

    @Override
    public void create() {

        batch = new TwoColorPolygonBatch(2000);

        initialScreen = new InitialScreen(this);
        showScreen = new ShowScreen(this, bgColor, scale, size);
        loadScreen=new LoadScreen(arg);
        if ((arg.length==3||arg.length==4) &&arg[0].equals("-load")){
            this.setScreen(loadScreen);
        }
        else {
            this.setScreen(initialScreen);
        }
    }

    @Override
    public void resize(int width, int height) {
        super.resize(width, height);
    }

    public String[] getArg() {
        return arg;
    }
}
