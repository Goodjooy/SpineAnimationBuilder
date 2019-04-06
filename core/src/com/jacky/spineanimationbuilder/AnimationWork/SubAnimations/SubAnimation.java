package com.jacky.spineanimationbuilder.AnimationWork.SubAnimations;

import com.badlogic.gdx.utils.Array;
import com.esotericsoftware.spine.Bone;
import com.esotericsoftware.spine.BoneData;

public class SubAnimation extends BasicSubAnimation {
    private String name;


    private Array<Float> data=new Array<Float>();


    private float speedAngle = 0.0f;
    private float speedMoveX = 0.0f;
    private float speedMoveY = 0.0f;
    private float speedShearX = 0.0f;
    private float speedShearY = 0.0f;
    private float speedScaleX = 0;
    private float speedScaleY = 0;
    private float speedLength = 0;

    private boolean baseOnAnimation = false;
    private boolean autoBack = false;
    private boolean changeBoneData = false;

    private float clock = 0.0f;
    private float workTime = 0.0f;

    private float keepTime;

    boolean firstTime = false;

    @Override
    public void update(float delta) {
        clock += delta;
        workTime = clock - delay < 0 ? 0 : clock - delay;
        if (autoBack) {
            if (clock >= 0 && clock < keepTime)
                updateInfoForward();
            else if (clock >= keepTime && clock <= (keepTime + time)) {
                if (!firstTime) {
                    updateInfoForward();
                    firstTime = true;
                } else {
                    workTime -= time;
                    updateInfoBackward();
                }
            } else if (clock > (keepTime + time)) {
                updateInfoBackward();
                if (loop) reset();
            }
        } else {
            if (clock >= 0 && clock <= keepTime)
                updateInfoForward();
            if (clock > keepTime && loop)
                reset();
        }

        if (workTime != 0)
            useAnimation();

        // System.out.printf("scaleX %f\nscaleY %f\nworktime %f\n\n",nowShearX,nowShearY,workTime);


    }

    private void workSpeed() {
        speedAngle = rotate / time;
        speedMoveX = moveX / time;
        speedMoveY = moveY / time;
        speedScaleX = scaleX / time;
        speedScaleY = scaleY / time;
        speedShearX = shearX / time;
        speedShearY = shearY / time;
        speedLength = lengthChange / time;
    }

    private void workOutInfo(float clock) {
        if (rotate >= 0)
            nowRotate = (clock * speedAngle <= rotate ? clock * speedAngle : rotate);
        else
            nowRotate = (clock * speedAngle >= rotate ? clock * speedAngle : rotate);

        if (moveX >= 0)
            nowPositionX = (clock * speedMoveX <= moveX ? clock * speedMoveX : moveX);
        else
            nowPositionX = (clock * speedMoveX >= moveX ? clock * speedMoveX : moveX);

        if (moveY >= 0)
            nowPositionY = (clock * speedMoveY <= moveY ? clock * speedMoveY : moveY);
        else
            nowPositionY = (clock * speedMoveY >= moveY ? clock * speedMoveY : moveY);

        if (scaleX >= 0)
            nowScaleX = (clock * speedScaleX <= scaleX ? clock * speedScaleX : scaleX);
        else
            nowScaleX = (clock * speedAngle >= scaleX ? clock * speedAngle : scaleX);

        if (scaleY >= 0)
            nowScaleY = (clock * speedScaleY <= scaleY ? clock * speedScaleY : scaleY);
        else
            nowScaleY = (clock * speedAngle >= scaleY ? clock * speedAngle : scaleY);

        if (shearX >= 0)
            nowShearX = clock * speedShearX <= shearX ? clock * speedShearX : shearX;
        else
            nowShearX = clock * speedShearX >= shearX ? clock * speedShearX : shearX;

        if (rotate >= 0)
            nowShearY = clock * speedShearY <= shearY ? clock * speedShearY : shearY;
        else
            nowRotate = (clock * speedAngle >= rotate ? clock * speedAngle : rotate);

        if (lengthChange >= 0)
            nowLength = clock * speedLength <= lengthChange ? clock * speedLength : lengthChange;
        else
            nowLength = clock * speedLength >= lengthChange ? clock * speedLength : lengthChange;

    }

    private void workOutInfo() {
        workOutInfo(workTime);
    }

    private void updateInfoForward() {
        workOutInfo();
        nowRotate = nowRotate + boneData.getRotation();
        nowPositionX = nowPositionX + boneData.getX();
        nowPositionY += boneData.getY();
        nowScaleX += 1;
        nowScaleY += 1;
        nowLength += boneData.getLength();

    }

    private void updateInfoBackward() {
        workOutInfo();
        nowRotate = boneData.getRotation() + rotate - nowRotate;
        nowPositionX = boneData.getX() + moveX - nowPositionX;
        nowPositionY = boneData.getY() + moveY - nowPositionY;
        nowScaleX = scaleX + 1 - nowScaleX;
        nowScaleY = scaleY + 1 - nowScaleY;
        nowShearX = shearX - nowShearX;
        nowShearY = shearY - nowShearY;
        nowLength = lengthChange - (workTime * speedLength <= lengthChange ? workTime * speedLength : lengthChange) +
                boneData.getLength();
    }

    private void useAnimation() {
        if (changeBoneData) {
            boneData.setPosition(nowPositionX, nowPositionY);
            boneData.setScale(nowScaleX, nowScaleY);
            boneData.setRotation(nowRotate);
            boneData.setShearX(nowShearX);
            boneData.setShearY(nowShearY);
            boneData.setLength(nowLength);
        } else {
            if (!baseOnAnimation)
                bone.setToSetupPose();
            bone.setPosition(nowPositionX, nowPositionY);
            bone.setScale(nowScaleX, nowScaleY);
            bone.setShearX(nowShearX);
            bone.setShearY(nowShearY);
            bone.setRotation(nowRotate);
        }

    }

    private void reset() {
        clock = 0;
        nowRotate = boneData.getRotation();
        nowPositionX = boneData.getX();
        nowPositionY = boneData.getY();
        nowScaleX = boneData.getScaleX();
        nowScaleY = boneData.getScaleY();
        nowShearX = nowShearY = 0;
        nowLength = boneData.getLength();
    }

    public void realToSetUp() {
        data.size=8;
        clock = 0;
        workSpeed();
        keepTime = time + delay;
        reset();
    }

    public void setAutoBack(boolean autoBack) {
        this.autoBack = autoBack;
    }

    public void setBaseOnAnimation(boolean baseAnimation) {
        this.baseOnAnimation = baseAnimation;
    }

    public void setChangeBoneData(boolean changeBoneData) {
        this.changeBoneData = changeBoneData;
    }

    public float getKeepTime() {
        if (autoBack)
            return keepTime + time;
        return keepTime;
    }

    @Override
    public void slotUpdate(float delta) {
        workOutInfo();
        super.slotUpdate( delta);
    }
}

