package com.jacky.spineanimationbuilder.AnimationWork;

import com.esotericsoftware.spine.Skeleton;

public class AnimationState {
    Skeleton skeleton;
    com.esotericsoftware.spine.AnimationState animationState;
    public AnimationState(Skeleton skeleton, com.esotericsoftware.spine.AnimationState animationState){
        this.skeleton=skeleton;
        this.animationState=animationState;
    }
}
