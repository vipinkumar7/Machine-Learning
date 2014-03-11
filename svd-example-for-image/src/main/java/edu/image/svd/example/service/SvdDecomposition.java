package edu.image.svd.example.service;

import java.util.List;

import org.apache.commons.math.linear.RealMatrix;

public interface SvdDecomposition {

	/**
	 * Decompose the matrix into S V and D
	 * @param testSquare
	 * @return
	 */
	public  List<RealMatrix> doDecompose(double[][] testSquare,int rank);
	
	/**
	 * Print the matrix to console
	 * @param matrix
	 */
	public  void showMatrix(RealMatrix matrix);
	
	/**
	 * Print the matrix to console
	 * @param matrix
	 */
	public  void showMatrix(double[][] matrix,int height,int width);
	
	/**
	 * 
	 * this method calculates U*S*V'
	 * 
	 * @param S
	 * @param V
	 * @param U
	 * @return
	 */
	public  double[][] reConstructImage(List<RealMatrix> svd);
	/**
	 * Reduce the S V and D matrix into the given rank
	 * @param matrix
	 * @param rank
	 * @param delim
	 * @return
	 */
	public  RealMatrix getRanked(RealMatrix matrix, int rank, char delim);
}
