package edu.image.svd.example;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.imageio.ImageIO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import edu.image.svd.example.service.ReadImage;


/**
 * 
 * @author Vipin Kumar
 *
 */
public class ReadImageImpl implements ReadImage {
	private static final Logger log = LoggerFactory.getLogger( ReadImageImpl.class );
	
	private String fileName; 
	@Override
	public List<int[][]> imread(BufferedImage image) {
		int width = image.getWidth();
		int height = image.getHeight();

		List<int[][]> rgbArrays = new ArrayList<int[][]>();

		int[][] resultR = new int[height][width];
		int[][] resultG = new int[height][width];
		int[][] resultB = new int[height][width];

		switch (image.getType()) {

		case BufferedImage.TYPE_4BYTE_ABGR:

			break;
		case BufferedImage.TYPE_INT_ARGB:

			break;

		case BufferedImage.TYPE_3BYTE_BGR:

			for (int row = 0; row < height; row++) {
				for (int col = 0; col < width; col++) {
					int pixel = image.getRGB(col, row);
					resultR[row][col] = (pixel >> 16) & 0x000000FF;
					resultG[row][col] = (pixel >> 8) & 0x000000FF;
					resultB[row][col] = (pixel) & 0x000000FF;
				}
			}

			break;

		default:

		}
		rgbArrays.add(resultR);
		rgbArrays.add(resultG);
		rgbArrays.add(resultB);
		return rgbArrays;
	}

	@Override
	public double[][] rgb2gray(BufferedImage image, int height, int width) {

		double[][] gray = new double[height][width];

		for (int row = 0; row < height; row++) {
			for (int col = 0; col < width; col++) {

				int pixel = image.getRGB(col, row);
				int R = (pixel >> 16) & 0x000000FF;
				int G = (pixel >> 8) & 0x000000FF;
				int B = (pixel) & 0x000000FF;
				double Ga = 0.21 * R + 0.71 * G + 0.07 * B;
				gray[row][col] = Ga;

			}
		}

		return gray;

	}

	@Override
	public double[][] im2double(int[][] inputMatrix, int height, int width) {
		double[][] doublePresionMatrix = new double[height][width];

		for (int row = 0; row < height; row++) {
			for (int col = 0; col < width; col++) {
				doublePresionMatrix[row][col] = inputMatrix[row][col] / 255.00;

			}
		}

		return doublePresionMatrix;
	}

	@Override
	public double[][] im2double(double[][] inputMatrix, int height, int width) {
		double[][] doublePresionMatrix = new double[height][width];

		for (int row = 0; row < height; row++) {
			for (int col = 0; col < width; col++) {
				doublePresionMatrix[row][col] = inputMatrix[row][col] / 255.00;

			}
		}

		return doublePresionMatrix;
	}

	

	
	public int[][] im2unit8(double[][] inputMatrix, int height, int width) {
		int[][] uint8Matrix = new int[height][width];
		for (int row = 0; row < height; row++) {
			for (int col = 0; col < width; col++) {
				uint8Matrix[row][col] = (int) (inputMatrix[row][col] * 255.00);

			}
		}

		return uint8Matrix;

	}

	
	public void writeImage(int[][] inputMatrix, int height, int width) {

		final BufferedImage image = new BufferedImage(width, height,
				BufferedImage.TYPE_USHORT_GRAY);
		
		for (int row = 0; row < height; row++) {
			for (int col = 0; col < width; col++) {
				image.setRGB(col, row, inputMatrix[row][col]);

			}
		}
			try {
				
				log.info("Writing image to file");
				
				ImageIO.write(image, "gif", new File(fileName));
			} catch (IOException e) {
				
				log.error("Not able to write File:",e);
			}

	}

	

	public void setFileName(String fileName) {
		this.fileName = fileName;
	}
}
