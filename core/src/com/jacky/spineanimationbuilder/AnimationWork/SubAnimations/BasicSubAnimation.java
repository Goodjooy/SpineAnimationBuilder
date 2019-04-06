package com.jacky.spineanimationbuilder.AnimationWork.SubAnimations;

import com.badlogic.gdx.utils.Array;
import com.esotericsoftware.spine.Bone;
import com.esotericsoftware.spine.BoneData;

public class BasicSubAnimation {
    private String name;

    Bone bone;
    BoneData boneData;

    private Array<Float> data = new Array<Float>();

    float rotate = 0;
    float moveX = 0;
    float moveY = 0;
    float scaleX = 1;
    float scaleY = 1;
    float shearX = 0;
    float shearY = 0;
    float lengthChange = 0;

    float nowRotate = 0;
    float nowPositionX = 0;
    float nowPositionY = 0;
    float nowScaleX = 0;
    float nowScaleY = 0;
    float nowShearX = 0;
    float nowShearY = 0;
    float nowLength = 0;

    float delay = 0.0f;
    float time = 0;

    boolean loop = false;


    public void update(float delta) {

    }

    public void slotUpdate(float delta) {
        data.set(0, nowRotate);
        data.set(1, nowPositionX);
        data.set(2, nowPositionY);
        data.set(3, nowScaleX);
        data.set(4, nowScaleY);
        data.set(5, nowShearX);
        data.set(6, nowShearY);
        data.set(7, nowLength);
    }

    public Array<Float> getChange() {
        return data;
    }

    /*setter & getter*/
    public void setRotate(float rotate) {
        this.rotate = rotate;
    }

    public void setMoveX(float moveX) {
        this.moveX = moveX;
    }

    public void setMoveY(float moveY) {
        this.moveY = moveY;
    }

    public void setScaleX(float scaleX) {
        this.scaleX = scaleX - 1;
    }

    public void setScaleY(float scaleY) {
        this.scaleY = scaleY - 1;
    }

    public void setShearX(float shearX) {
        this.shearX = shearX;
    }

    public void setLengthChange(float lengthChange) {
        this.lengthChange = lengthChange;
    }

    public void setShearY(float shearY) {
        this.shearY = shearY;
    }

    public void setTime(float time) {
        this.time = time;
    }

    public void setDelay(float delay) {
        this.delay = delay;
    }

    public void setLoop(boolean loop) {
        this.loop = loop;
    }

    public void setBone(Bone bone) {
        this.bone = bone;
        this.boneData = bone.getData();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
