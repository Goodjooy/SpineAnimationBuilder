package com.jacky.spineanimationbuilder.Screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.g2d.TextureAtlas;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.FloatArray;
import com.esotericsoftware.spine.*;
import com.esotericsoftware.spine.attachments.Attachment;
import com.jacky.spineanimationbuilder.SpineCharacter;

public class LoadScreen implements Screen {
    private String[] args;
    private String json = "{\"error\":null,\"name\":null,\"bones\":\"bones\",\"slot\":\"slot\",\"animation\":\"animation\",\"atlas\":null}";

    public LoadScreen(String[] args) {
        this.args = args;
    }

    @Override
    public void show() {

    }

    @Override
    public void render(float delta) {
        SpineCharacter character = new SpineCharacter();
        try {
            character.loadSkeleton(args[1], args[2]);
            character.skeleton.setToSetupPose();

            String boneString;
            StringBuilder bones = new StringBuilder("{");
            for (Bone bone : character.skeleton.getBones()) {

                BoneData boneData = bone.getData();
                String value;
                StringBuilder valueBuilder = new StringBuilder("{\"name\":\"" + boneData.getName() + "\"," +
                        "\"index\":" + boneData.getIndex() + "," +
                        "\"length\":" + boneData.getLength() + "," +
                        "\"parent\":" + (boneData.getParent() == null ? "null," : "\"" + boneData.getParent().getName() + "\",") +
                        "\"color\":" + "[" + boneData.getColor().r + "," + boneData.getColor().g + "," + boneData.getColor().b + "," + boneData.getColor().a + "]," +
                        "\"rotate\":" + boneData.getRotation() + "," +
                        "\"scaleX\":" + boneData.getScaleX() + "," +
                        "\"scaleY\":" + boneData.getScaleY() + "," +
                        "\"shearX\":" + boneData.getShearX() + "," +
                        "\"shearY\":" + boneData.getShearY() + "," +
                        "\"transform\":\"" + boneData.getTransformMode().name() + "\"," +
                        "\"x\":" + boneData.getX() + "," +
                        "\"y\":" + boneData.getY() + "," +
                        "\"a\":" + bone.getA() + "," +
                        "\"b\":" + bone.getB() + "," +
                        "\"c\":" + bone.getC() + "," +
                        "\"d\":" + bone.getD() + "," +
                        "\"children\":[");
                if (bone.getChildren().size != 0) {
                    for (Bone bone1 : bone.getChildren()) {
                        String names = "\"" + bone1.getData().getName() + "\"";
                        valueBuilder.append(names).append(",");
                    }
                    value = valueBuilder.toString();
                    value = value.substring(0, value.length() - 1);
                    value = value + "]";
                } else {
                    value = valueBuilder.toString();
                    value = value + "]";
                }
                value = value + "}";
                bones.append("\"").append(boneData.getName()).append("\"").append(":").append(value).append(",");
            }
            boneString = bones.toString().substring(0, bones.length() - 1) + "}";
            json = json.replace("\"bones\":\"bones\"", "\"bones\":" + boneString);

            String animateString;
            StringBuilder animate = new StringBuilder("{");
            for (Animation animation : character.skeletonData.getAnimations()) {
                animate.append("\"").append(animation.getName()).append("\":")
                        .append(animation.getDuration()).append(",");

            }
            animateString = animate.toString().substring(0, animate.length() - 1) + "}";
            json = json.replace("\"animation\":\"animation\"", "\"animation\":" + animateString);

            String slotsString;
            StringBuilder slots = new StringBuilder("{");
            for (Slot slot : character.skeleton.getSlots()) {
                String slotString;
                StringBuilder slot_work = new StringBuilder();
                Attachment val = slot.getAttachment();
                        slot_work.append("\"").append(slot.getData().getName()).append("\":{")
                                .append("\"attachment\":\"").append(val==null?"null":val.toString()).append("\",")
                        .append("\"attachment_time\":").append(slot.getAttachmentTime()).append(",")
                        .append("\"bone\":\"").append(slot.getBone().getData().getName()).append("\",")
                        .append("\"color\":" + "[").append(slot.getColor().r)
                        .append(",").append(slot.getColor().g).append(",")
                        .append(slot.getColor().b).append(",").append(slot.getColor().a).append("],")
                        //      .append("\"dark_color\":" + "[").append(slot.getDarkColor().r)
                        //      .append(",").append(slot.getDarkColor().g).append(",")
                        //      .append(slot.getDarkColor().b).append(",").append(slot.getDarkColor().a).append("],")
                        .append("\"index\":").append(slot.getData().getIndex()).append(",")
                        .append("\"blend\":").append(slot.getData().getBlendMode().getDest()).append(",")
                        .append("\"attachment_vertices\":[");

                if (slot.getAttachmentVertices().size != 0) {
                    FloatArray pos = slot.getAttachmentVertices();
                    for (float value : pos.toArray()) {
                        slot_work.append(value).append(",");
                    }
                    slotString = slot_work.toString().substring(0, slot_work.length() - 1);
                    slotString = slotString + "]}";
                } else {
                    slotString = slot_work.toString();
                    slotString = slotString + "]}";
                }

                slots.append(slotString).append(",");
            }
            slotsString = slots.toString().substring(0, slots.length() - 1) + "}";
            json = json.replace("\"slot\":\"slot\"", "\"slot\":" + slotsString);

            json=json.replace("\"name\":null","\"name\":\""+character.skeletonData.getName()+"\"");

            String regionString;
            StringBuilder regions=new StringBuilder("[");
            for (TextureAtlas.AtlasRegion region:character.getAtlas().getRegions()){
                regions.append("\"").append(region.name).append("\",");
            }
            regionString=regions.toString().substring(0,regions.length()-1)+"]";
            json=json.replace("\"atlas\":null","\"atlas\":"+regionString);

        } catch (Throwable info) {
            info.printStackTrace();
            json = json.replace("\"error\":null", "\"error\":\"" + info.toString()+"\"");
        }
        FileHandle out;
        if (args.length==4)
            out= Gdx.files.absolute(args[3]+"\\respond.bat");
        else
            out=Gdx.files.absolute(System.getProperty("user.dir")+"\\respond.bat");

        out.writeString(json,false);
        System.out.print("save at:");
        System.out.println(out.path());

        System.exit(-1);
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
