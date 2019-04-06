package com.jacky.spineanimationbuilder;

import com.badlogic.gdx.Gdx;

import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.utils.JsonReader;
import com.badlogic.gdx.utils.JsonValue;
import com.esotericsoftware.spine.Skeleton;
import com.jacky.spineanimationbuilder.AnimationWork.Animation;
import com.jacky.spineanimationbuilder.AnimationWork.SubAnimations.SubAnimation;

/**
 * 下一步，json解析
 */
public class JsonIO {
    public enum actionType{
        UniformMotion,
        UniformSpeedMovement,
        FinishAtOnce,
        }
    private final static String jsonString=
            "{" +
                    "\"type\":\"Animation\"," +
                    "\"name\":\"text_animation\"," +
                    "\"SubAnimation\":[" +
                        "{" +
                            "\"name\":\"text\"," +
                            "\"bone\":\"face\"," +
                            "\"type\":0,"+
                            "\"rotate\":45.0," +
                            "\"scaleX\":1.0,"+
                            "\"scaleY\":1.0,"+
                            "\"shearX\":0.0,"+
                            "\"shearY\":0.0," +
                            "\"moveX\":0.0,"+
                            "\"moveY\":0.0," +
                            "\"boneLengthAdd\":0," +

                            "\"BaseOnAnimation\":false," +
                            "\"AutoBack\":true," +
                            "\"loop\":false," +
                            "\"ChildrenFallow\":true," +

                            "\"delay\":0.25," +
                            "\"playTime\":30"+
                        "}," +
                        "null," +
                        "null" +
                        "]" +
                    "}";



    private final JsonValue val;

    public JsonIO(String filename){
        JsonReader reader =new JsonReader();
        val=reader.parse(filename);


    }
    public static Animation loadAnimation(JsonValue value, Skeleton skeleton){
        Animation animation =new Animation();
        String type=value.getString("type");
        if (!type.equals("Animation"))
            return null;
        animation.setName(value.getString("name"));
        JsonValue subAnimations=value.get("SubAnimation");
        for (int i = 0; i <subAnimations.size ; i++) {
            animation.addSubAnimation(loadSubAnimation(subAnimations.get(i),skeleton));
        }
        System.out.println(animation);
        return animation;
    }
    private static SubAnimation loadSubAnimation(JsonValue value, Skeleton skeleton){
        SubAnimation subAnimation=new SubAnimation();
        if (!value.toString().equals("null") && value.getInt("type")==0){
        subAnimation.setBaseOnAnimation(value.getBoolean("BaseOnAnimation"));
        subAnimation.setAutoBack(value.getBoolean("AutoBack"));
        subAnimation.setChangeBoneData(false);

        subAnimation.setName(value.getString("name"));
        subAnimation.setScaleX(value.getFloat("scaleX"));
        subAnimation.setScaleY(value.getFloat("scaleY"));
        subAnimation.setRotate(value.getFloat("rotate"));
        subAnimation.setShearX(value.getFloat("shearX"));
        subAnimation.setShearY(value.getFloat("shearY"));
        subAnimation.setMoveX(value.getFloat("moveX"));
        subAnimation.setMoveY(value.getFloat("moveY"));
        subAnimation.setLengthChange(value.getFloat("boneLengthAdd"));

        subAnimation.setBone(skeleton.findBone(value.getString("bone")));

        subAnimation.setDelay(value.getFloat("delay"));
        subAnimation.setTime(value.getFloat("playTime"));

        subAnimation.realToSetUp();
        }
        return subAnimation;
    }
    public static JsonValue loadConfig(String fliename){
        JsonReader reader =new JsonReader();
        FileHandle fileHandle=Gdx.files.absolute(fliename);
        if (!fileHandle.exists())
            return null;
        return reader.parse(fileHandle);
    }
    public static void setConfig(JsonValue jsonValue){

    }

    public static void main(String []arg){
        JsonReader reader =new JsonReader();
        JsonValue val=reader.parse(jsonString);

        loadAnimation(val,null);


    }
}
