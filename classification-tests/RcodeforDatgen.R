##@author Vipin Kumar

### random Binomial distribution for the probability of success 1/2 /3 1/6 respectively

	U <- array(0,dim= c(10,30))
for(i in 1:10)
{
	U[i,] <- rbinom(30,10,1/6)
} 
	write(U, "/home/hduser/onebysix.txt",ncolumns=30,append=TRUE, sep = "\t")
for(i in 1:10)
{
	U[i,] <- rbinom(30,10,1/6)
} 
write(U, "/home/hduser/onebysix.txt",ncolumns=30,append=TRUE, sep = "\t")




	U <- array(0,dim= c(10,30))
for(i in 1:10)
{
	U[i,] <- rbinom(30,10,1/2)
} 
	write(U, "/home/hduser/onebytwo.txt",ncolumns=30,append=TRUE, sep = "\t")
for(i in 1:10)
{
	U[i,] <- rbinom(30,10,1/2)
} 
write(U, "/home/hduser/onebytwo.txt",ncolumns=30,append=TRUE, sep = "\t")


	U <- array(0,dim= c(10,30))
for(i in 1:10)
{
	U[i,] <- rbinom(30,10,1/3)
} 
	write(U, "/home/hduser/onebythree.txt",ncolumns=30,append=TRUE, sep = "\t")
for(i in 1:10)
{
	U[i,] <- rbinom(30,10,1/3)
} 
write(U, "/home/hduser/onebythree.txt",ncolumns=30,append=TRUE, sep = "\t")

