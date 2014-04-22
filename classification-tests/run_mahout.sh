# change data to sparse
mahout seq2sparse -i classificationin -o classificationout

 
# divide the data into two parts one train and one test

mahout split -i classificationout/tfidf-vectors --trainingOutput train-vectors --testOutput test-vectors --randomSelectionPct 40 --overwrite --sequenceFiles -xm sequential

#train the classifier 
mahout trainnb -i train-vectors -el -li labelindex -o model -ow -c

#test the classifier on train data
mahout testnb -i train-vectors -m model -l labelindex -ow -o classificationout-testing -c

#test the classifier on test data

mahout testnb -i test-vectors -m model -l labelindex -ow -o classificationout-testing -c


