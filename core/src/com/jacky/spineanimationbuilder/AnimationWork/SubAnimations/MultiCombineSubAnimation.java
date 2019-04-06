package com.jacky.spineanimationbuilder.AnimationWork.SubAnimations;

import com.badlogic.gdx.utils.Array;

public class MultiCombineSubAnimation extends BasicSubAnimation {

    private Array<BasicSubAnimation> subAnimations=new Array<BasicSubAnimation>();

    @Override
    public void update(float delta) {
        for (BasicSubAnimation animation : subAnimations) {
            animation.slotUpdate(delta);
            Array<Float> info=animation.getChange();
        }
    }
}
