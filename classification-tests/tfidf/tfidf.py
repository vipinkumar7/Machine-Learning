import math

""" Initial variable declaration"""

dictionary=list()
docCount=dict()
tfCount=dict()
tfidfvec=dict()
tfidf=dict()
labelweight=dict()
score=dict()
thetascore=dict()

numOfDocs=0

""" Function definitions for various stages"""

def clean(s):
    """ This function is used for cleaning the sentences out of
        special characters and returns the cleaned sentence"""
    
    sent=""
    for c in s:
        n=ord(c)
        if ((n>=65 and n<=90) or (n>=97 and n<=122) or n==32):
            sent=sent+c
    return sent
        

def create_dataset(flist):
    """ This takes all the input documents and creates a dataset
        out of them in a specific format for analyzing and filling
        all the dictionaries that are created above. It is also responsible
        for internally creating a dictionary of all distinct words."""
    
    global dictionary
    global numOfDocs
    i=0.0
    k=1
    op=open("./dataset.txt","a")
    op.seek(0)
    op.truncate()
    print "Creating dataset. Output file opened!"
    for filename in flist:
        fo=open(filename,"r")
        print "Reading file: "+filename
        classname="CLASS_"+str(i)+"/"
        print "Current class: "+classname
        k=1
        for sentence in fo:
            sentence=clean(sentence)
            words=sentence.split(" ")
            for word in words:
                if word not in dictionary:
                    dictionary.append(word)
            op.write(classname+str(k)+"\t"+sentence+"\n")
            numOfDocs+=1
            k+=1
        i+=1
        fo.close()
    op.close()

def dcountgen():
    """ This creates the document count for all the words in the dicitonary
        using the dataset created and stores it in docCount."""
    global dictionary
    global docCount
    op=open("./dataset.txt","r")
    for word in dictionary:
        count=0
        #print "Counting :"+word
        for line in op:
            sentence=line.split("\t")[1]
            sentence=sentence.rstrip()
            words=sentence.split(" ")
            if word in words:
                count+=1
        op.seek(0,0)
        #print word+" "+str(count)
        #k=raw_input()
        docCount[word]=count
    op.close()
        

def tfgen():
    """ This creates the term frequency count for all the words in a particular
        document by ingesting the dataset and storing the results in tfCount."""
    global tfCount
    ip=open("./dataset.txt","r")
    #print "\n\nReading the dataset and genratinf tfvector:"
    for line in ip:
        tf=dict()
        classname=line.split("\t")[0]
        
        doc=line.split("\t")[1]
        doc=doc.rstrip()
        words=doc.split(" ")
        for word in words:
            if word not in tf:
                tf[word]=1
            else:
                tf[word]+=1
        tfCount[classname]=tf
        tf={}
    ip.close()

def tfvectorgen():
    """ This generates the tfidf for all term in a particular document of every
        class and stores it in tfidfvec."""
    global tfdifvec
    for key1 in tfCount:
        #print key1
        tflist=tfCount[key1]
        tfidflist=dict()
        for key2 in tflist:
            tfidflist[key2]=float(math.sqrt(tflist[key2]))*float(math.log(numOfDocs/docCount[key2]))
            #print key2+" : "+str(tfidflist[key2])
        tfidfvec[key1]=tfidflist
        tfidflist={}

def tfidfgen():
    """ This generates all the smmed tfidf's of all distinct terms in a class
        and stores it in tfidf."""
    global tfidf
    global tfidfvec
    
    for key in tfidfvec:
        classname=key.split('/')[0]
        addlist=tfidfvec[key]
        if classname not in tfidf:
            tfidf[classname]=addlist
        else:
            tfidflist=tfidf[classname]
            for word in addlist:
                if word in tfidflist:
                    tfidflist[word]=float(tfidflist[word]+addlist[word])
                else:
                    tfidflist[word]=addlist[word]
            tfidf[classname]=tfidflist

def findlabelweight():
    """ Finds the label weight of all classes by summing all the feature weights
        in that particular class and stores in labelweight."""
    global tfidf
    global labelweight
    featuresum=0.0
    for classname in tfidf:
        classlist=tfidf[classname]
        for word in classlist:
            featuresum+=float(classlist[word])
        labelweight[classname]=featuresum

def score():
    """ Generates the theta scores for all the terms for their particular classes
        and stores in thetascore."""
    global dictionary
    numFeatures=len(dictionary)
    global labelweight
    global tfidf
    global thetascore
    for classname in labelweight:
        featurelist=tfidf[classname]
        scorelist=dict()
        for word in featurelist:
            score=((featurelist[word]+1)/(labelweight[classname]+1*numFeatures))
            #score=math.log(score)
            scorelist[word]=score
        thetascore[classname]=scorelist

def interface(sentence):
    """ This interface function is passed a sentence whose relevance with a
        document has to found. It uses thetascore to find the maxscore amongst
        all documents and find the document the sentence belongs to."""
    global thetascore
    sentence=clean(sentence)
    words=sentence.split(" ")
    maxscore=0.0
    classname=""

    for key in thetascore:
        scorelist=thetascore[key]
        score=0
        for word in words:
            if word in scorelist:
                score+=scorelist[word]
        if(score>maxscore):
            classname=key
            maxscore=score
    print "The relevance is highest in : "+str(classname)
    print "The score is : "+str(maxscore)
    
""" Now we start calling all the functions and developing the dictionaries
    to classify input text"""

files={"./doc1.txt","./doc2.txt","./doc3.txt"}
create_dataset(files)
tfgen()
dcountgen()
tfvectorgen()
tfidfgen()
findlabelweight()
score()
print "\n\nGive the string to find relevance:"
inputstring=raw_input()
interface(inputstring)
