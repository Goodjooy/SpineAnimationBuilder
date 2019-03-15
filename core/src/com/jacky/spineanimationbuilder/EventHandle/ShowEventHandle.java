package com.jacky.spineanimationbuilder.EventHandle;

import com.badlogic.gdx.Input;
import com.badlogic.gdx.InputProcessor;
import com.jacky.spineanimationbuilder.AnimationBuilder;
import com.jacky.spineanimationbuilder.Screen.ShowScreen;

public class ShowEventHandle implements InputProcessor {
    private final AnimationBuilder game;
    private final ShowScreen screen;
    private boolean ctrlYeas=false;

    public ShowEventHandle(AnimationBuilder game,ShowScreen screen){
        this.game=game;
        this.screen=screen;
    }
    @Override
    public boolean keyDown(int keycode) {
        if (keycode== Input.Keys.CONTROL_RIGHT ||keycode==Input.Keys.CONTROL_LEFT)
            ctrlYeas=true;

        if (keycode==Input.Keys.SPACE)
           screen.saveAll();


        else return false;
        return true;
    }

    @Override
    public boolean keyUp(int keycode) {
        if (keycode== Input.Keys.CONTROL_RIGHT ||keycode==Input.Keys.CONTROL_LEFT)
            ctrlYeas=false;
        else return false;
        return true;
    }

    @Override
    public boolean keyTyped(char character) {
        return false;
    }

    @Override
    public boolean touchDown(int screenX, int screenY, int pointer, int button) {
        return false;
    }

    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        return false;
    }

    @Override
    public boolean touchDragged(int screenX, int screenY, int pointer) {
        return false;
    }

    @Override
    public boolean mouseMoved(int screenX, int screenY) {
        return false;
    }

    @Override
    public boolean scrolled(int amount) {
        return false;
    }
}
