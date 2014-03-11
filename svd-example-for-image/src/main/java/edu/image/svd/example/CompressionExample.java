package edu.image.svd.example;

import java.awt.image.BufferedImage;
import java.io.InputStream;
import java.util.List;

import javax.imageio.ImageIO;

import org.apache.commons.math.linear.RealMatrix;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import edu.image.svd.example.ReadImageImpl;
import edu.image.svd.example.SvdDecompositionImpl;
/**
 * 
 * @author Vipin Kumar
 *
 */
public class CompressionExample {

	private static final Logger log = LoggerFactory.getLogger( CompressionExample.class );
	
	private ReadImageImpl imager;
	
	private SvdDecompositionImpl sDecomposition;
	
	
	/**
	 * ReConstructed the matrix by using only 160 eigen values
	 */
	public void compressAndWriteImage() {

		try {

			/*read file from resources folder*/
			InputStream in = getClass().getResourceAsStream("/files/actress.jpg");

			BufferedImage image = ImageIO.read(in);

			

			int width = image.getWidth();
			int height = image.getHeight();

			/*convert the image to grayScale nxm matrix*/
			double[][] gray = imager.rgb2gray(image, height, width); 

			/*change the uint8 pixels value to double vaule*/
			double[][] doublePresionMatrix = imager.im2double(gray, height, width);

			/*perform SVD and get the matrix only with rank 160*/
			List<RealMatrix> lRealMatrixs =sDecomposition.doDecompose(doublePresionMatrix,160);
			
			/*reconstruct the image again*/
			sDecomposition.reConstructImage(lRealMatrixs);
			
			/*convert the reconstructed double image to uint8 */
			int[][] reconstructedImage = imager.im2unit8(doublePresionMatrix, height, width);
			
			
			imager.writeImage(reconstructedImage, height, width);

		
			

		} catch (Exception e) {

			log.error("Exception in process",e);
			
		}
	}
	
	

	public ReadImageImpl getImager() {
		return imager;
	}

	public void setImager(ReadImageImpl imager) {
		this.imager = imager;
	}

	public SvdDecompositionImpl getsDecomposition() {
		return sDecomposition;
	}

	public void setsDecomposition(SvdDecompositionImpl sDecomposition) {
		this.sDecomposition = sDecomposition;
	}
}
