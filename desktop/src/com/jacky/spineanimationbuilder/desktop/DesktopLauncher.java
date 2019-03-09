package com.jacky.spineanimationbuilder.desktop;

import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;
import com.badlogic.gdx.graphics.Color;
import com.jacky.spineanimationbuilder.AnimationBuilder;

public class DesktopLauncher {
	public static void main (String[] arg) {
		LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
		config.width=config.height=512;
		config.title="Spine Animation Builder";
		config.backgroundFPS=-1;
		config.foregroundFPS=60;
		config.resizable=false;
		config.initialBackgroundColor= Color.WHITE;
		new LwjglApplication(new AnimationBuilder(), config);
	}
}
