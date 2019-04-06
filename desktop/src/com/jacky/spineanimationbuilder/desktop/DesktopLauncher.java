package com.jacky.spineanimationbuilder.desktop;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.utils.JsonValue;
import com.jacky.spineanimationbuilder.AnimationBuilder;
import com.jacky.spineanimationbuilder.JsonIO;
import com.jacky.spineanimationbuilder.SpineCharacter;

import java.io.IOException;
import java.util.Scanner;

public class DesktopLauncher {
    private static float[] colors=new float[]{0,1,0,1};
    private static int width = 1024, height = 1024;
    private static int FPS = 30;
    private static float scale = 1.0f;
    private static boolean openGLUse = true;
    private static String title = "Spine Animation Builder";
    private static boolean isExit = false;


    public static void main(String[] arg) {
        LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
        JsonValue configs=null;
        if (arg.length==0){
            askInitial();
            config.width = width;
            config.height = height;
            config.title = title;
            config.backgroundFPS = config.foregroundFPS = FPS;
            config.resizable = true;
            config.initialBackgroundColor = Color.WHITE;
            config.allowSoftwareMode = openGLUse;
        }
        else {

        }
        new LwjglApplication(new AnimationBuilder(arg,colors,scale,width,height), config);
    }

    public static void askInitial() {
        System.out.print("欢迎使用由清弦凝绝开发的spine动画导出小工具(°∀°)ﾉ\n\n");

        while (!isExit) {
            System.out.print("\n-----------设置内容-----------\n" +
                    "\ta)设置屏幕的尺寸-【默认为1024X1024】\n" +
                    "\tb)设置渲染时的背景颜色-【默认为[0,255,0,255](RGBA)】\n" +
                    "\tc)设置FPS-【默认为30帧】\n" +
                    "\td)设置屏幕标题-【默认为：Spine Animation Builder】\n" +
                    "\te)设置是否使用openGL渲染-【默认为使用】\n" +
                    "\tf)设置spine的缩放-【默认为 1.0f】\n" +
                    "\tg)跳过设置\n" +
                    "\t\t选择： ");

            try {
                char input = (char) System.in.read();

                switch (input) {
                    case 'a': {
                        setSize();
                        break;
                    }
                    case 'b': {
                        setColor();
                        break;
                    }
                    case 'c': {
                        System.out.print("FPS为：");
                        Scanner scanner = new Scanner(System.in);
                        FPS = scanner.nextInt();
                        break;
                    }
                    case 'd': {
                        System.out.print("标题为：");
                        Scanner scanner = new Scanner(System.in);
                        title = scanner.next();
                        break;
                    }
                    case 'e': {
                        System.out.print("是否使用openGL渲染【y/n】：");
                        Scanner scanner = new Scanner(System.in);
                        String use = scanner.next();
                        openGLUse = use.equals("y");
                        break;
                    }
                    case 'f': {
                        System.out.print("缩放尺寸：");
                        Scanner scanner = new Scanner(System.in);
                        scale = scanner.nextFloat();
                        break;
                    }
                    case 'g': {

                        exitSetting();
                        break;
                    }
                    default:
                        break;

                }

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static void setSize() {
        System.out.print("宽：");
        Scanner scanner = new Scanner(System.in);
        width = scanner.nextInt();
        System.out.print("长：");
        height = scanner.nextInt();
    }

    private static void setColor() {
        Scanner scanner = new Scanner(System.in);
        scanner.reset();
        int r = 0, g = 255, b = 0, a = 255;
        System.out.print("RED：");
        r = scanner.nextInt();
        System.out.print("GREEN：");
        g = scanner.nextInt();
        System.out.print("BLUE：");
        b = scanner.nextInt();
        System.out.print("Alpha：");
        a = scanner.nextInt();

        colors = new float[]{r / 255.0f, g / 255.0f, b / 255.0f, a / 255.0f};
    }

    private static void exitSetting()
    {
        System.out.printf("\n\n-----------设置内容-----------\n" +
                        "\ta)设置屏幕的尺寸-【为%dX%d】\n" +
                        "\tb)设置渲染时的背景颜色-【为[%.2f,%.2f,%.2f,%.2f](RGBA)[0.0,1.0]】\n" +
                        "\tc)设置FPS-【为%d帧】\n" +
                        "\td)设置屏幕标题-【为：%s】\n" +
                        "\te)设置是否使用openGL渲染-【为%b】\n" +
                        "\tf)设置spine的缩放-【为 %.2f】\n\n"
                , width, height, colors[0], colors[1], colors[2], colors[3], FPS, title, openGLUse, scale);
        isExit=true;
    }
}
