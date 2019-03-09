package com.jacky.spineanimationbuilder;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.esotericsoftware.spine.utils.TwoColorPolygonBatch;
import com.jacky.spineanimationbuilder.Screen.ShowScreen;
import com.jacky.spineanimationbuilder.spine.SpineLoader;

public class AnimationBuilder extends Game {
	OrthographicCamera camera;
	public TwoColorPolygonBatch batch;

	SpineLoader loader;

	@Override
	public void create() {
		camera=new OrthographicCamera();
		batch=new TwoColorPolygonBatch(2000);

		loader=new SpineLoader();

		loader.loadSkeleton(Gdx.files.absolute("D:\\porject\\cute_pic\\TextAsset\\aheye.skel"));
		this.setScreen(new ShowScreen(this));
	}

	public SpineLoader getLoader() {
		return loader;
	}
}
