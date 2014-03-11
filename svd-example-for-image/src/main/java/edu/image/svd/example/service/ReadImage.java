package edu.image.svd.example.service;

import java.awt.image.BufferedImage;
import java.util.List;

public interface ReadImage {

	/**
	 * This  function takes a RGB image (mxnx3) and gives the three mxn R,G and B componet 
	 * from it.
	 * @param  {@link BufferedImage}
	 * @return {@link List} of 2D mxn {@link Array}
	 */
	public List<int[][]> imread(BufferedImage image);
	/**
	 * Converts the RGB image to grayScale
	 * @param  {@link BufferedImage}
	 * @param height
	 * @param width
	 * @return
	 */
	public double[][] rgb2gray(BufferedImage image, int height, int width);
	
	/**
	 * This is  method works as im2double of Matlab but not that much good
	 * Converts the uint8 image matrix to double 
	 * 
	 * @param inputMatrix
	 * @param height
	 * @param width
	 * @return
	 */
	public double[][] im2double(int[][] inputMatrix, int height, int width);
	
	/**
	 * 
	 * @param inputMatrix
	 * @param height
	 * @param width
	 * @return
	 */
	public double[][] im2double(double[][] inputMatrix, int height, int width);
	
	/**
	 * Convert double matrix again to uint8
	 * @param inputMatrix
	 * @param height
	 * @param width
	 * @return
	 */
	public int[][] im2unit8(double[][] inputMatrix, int height, int width);
	/**
	 * Write  the image to file location
	 * @param inputMatrix
	 * @param height
	 * @param width
	 */
	public void writeImage(int[][] inputMatrix, int height, int width);
}
