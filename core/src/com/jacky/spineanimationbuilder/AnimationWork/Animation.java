package com.jacky.spineanimationbuilder.AnimationWork;

import com.badlogic.gdx.utils.Array;
import com.jacky.spineanimationbuilder.AnimationWork.SubAnimations.SubAnimation;

/**
 * 这是自定义动画的每一段动画的类
 * 需要有一个计时器
 * 需要有一个数组，保存所有子动画
 */
public class Animation {
    private String name;
    private float keepTime=0;
    private boolean loop=false;
    private Array<SubAnimation> subAnimationArray=new Array<SubAnimation>();

    public void update(float delta) {
        for (SubAnimation animation : subAnimationArray) {
            animation.update(delta);
        }
    }
    public void realToGo(){
        for (SubAnimation animation : subAnimationArray) {
            keepTime=keepTime>=animation.getKeepTime()?keepTime:animation.getKeepTime();
            animation.realToSetUp();
        }
    }
    public void setLoop(boolean loop){this.loop=loop;}
    public void addSubAnimation(SubAnimation animation){
        this.subAnimationArray.add(animation);
    }
    public void delSubAnimation(SubAnimation animation){
        subAnimationArray.removeValue(animation,false);
    }
    public  void setSunAnimation(int index,SubAnimation animation){
        subAnimationArray.set(index,animation);
    }

    public void setName(String name) {
        this.name = name;
    }

    public Array<SubAnimation> getSubAnimationArray() {
        return subAnimationArray;
    }

}
