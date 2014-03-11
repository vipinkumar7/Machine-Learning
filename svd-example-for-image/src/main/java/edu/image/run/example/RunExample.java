package edu.image.run.example;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import edu.image.svd.example.CompressionExample;

/**
 * 
 * @author Vipin Kumar
 *
 */
public class RunExample {

	public static void main(String[] args) {
		
		AbstractApplicationContext context=new ClassPathXmlApplicationContext("spring.xml");
		
		context.registerShutdownHook();
		
		
		/* run the compression example*/
		CompressionExample compex=(CompressionExample) context.getBean("compressExample");
		
		compex.compressAndWriteImage();
		context.close();
	}
}
