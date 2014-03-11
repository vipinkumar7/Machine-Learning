package edu.image.svd.example;

import java.util.ArrayList;
import java.util.List;

import org.apache.commons.math.linear.MatrixUtils;
import org.apache.commons.math.linear.RealMatrix;
import org.apache.commons.math.linear.SingularValueDecomposition;
import org.apache.commons.math.linear.SingularValueDecompositionImpl;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import edu.image.svd.example.service.SvdDecomposition;

/**
 * This class is responsible for SVD Factorization and reconstructing the image with the random rank
 * @author Vipin Kumar
 * 
 */
public class SvdDecompositionImpl implements SvdDecomposition{

	private static final Logger log = LoggerFactory.getLogger( SvdDecompositionImpl.class );

	
	public  List<RealMatrix> doDecompose(double[][] testSquare,int rank) {
		RealMatrix matrix = MatrixUtils.createRealMatrix(testSquare);

		SingularValueDecomposition svd = new SingularValueDecompositionImpl(
				matrix);

		RealMatrix S=getRanked(svd.getS(), rank, 'S');
		RealMatrix U=getRanked(svd.getU(), rank, 'U');
		RealMatrix V=getRanked(svd.getV(), rank, 'V');
		
		List<RealMatrix> svdList=new ArrayList<RealMatrix>();
		svdList.add(S);
		svdList.add(U);
		svdList.add(V);
		return svdList;
		

	}

	
	public  void showMatrix(RealMatrix matrix) {
		final int m = matrix.getRowDimension();

		log.debug("The Matrix is :");
		for (int i = 0; i < m; i++) {
			double[] rowMatrix = matrix.getRow(i);

			for (int j = 0; j < rowMatrix.length; j++) {
				log.debug(rowMatrix[j] + " ");
			}
			
			log.debug("\n");
		}

	}

	public  void showMatrix(double[][] matrix,int height,int width) {

		log.debug("The Double Matrix is :");
		for (int row = 0; row < height; row++) {
			for (int col = 0; col < width; col++) {
				log.debug(matrix[row][col] + "\t");
			}
			log.debug("\n");
		}

	}
	
	
	public  double[][] reConstructImage(List<RealMatrix> svd) {
		RealMatrix S=svd.get(0);
		RealMatrix U=svd.get(1);
		RealMatrix V=svd.get(2);
		
		RealMatrix real = U.multiply(S);
		real = real.multiply(V.transpose());

		final int m = real.getRowDimension();
		final int n = real.getColumnDimension();

		double[][] doubleMat = new double[m][n];

		for (int i = 0; i < m; i++) {
			double[] rowMatrix = real.getRow(i);

			for (int j = 0; j < rowMatrix.length; j++) {
				doubleMat[i][j] = rowMatrix[j];
			}

		}
		return doubleMat;

	}

	
	public  RealMatrix getRanked(RealMatrix matrix, int rank, char delim) {

		double[][] doubleMat = null;

		switch (delim) {

		case 'S':
			doubleMat=new double[rank][rank];
			for (int i = 0; i < rank; i++) {
				double[] rowMatrix = matrix.getRow(i);

				for (int j = 0; j < rank; j++) {
					doubleMat[i][j] = rowMatrix[j];
				}

			}
			break;
		default: {
			doubleMat=new double[matrix.getRowDimension()][rank];
			for (int i = 0; i < matrix.getRowDimension(); i++) {
				
				double[] rowMatrix = matrix.getRow(i);
				for (int j = 0; j < rank; j++) {
					
					doubleMat[i][j] = rowMatrix[j];
				}

			}
		}
		}

		RealMatrix mat = MatrixUtils.createRealMatrix(doubleMat);
		return mat;

	}
}
