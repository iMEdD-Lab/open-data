rm(list = ls())#we clear the R environment 
library(missForest) # load the R library used to impute the dataset
library(KRLS)#load the R library used to compute RBF
library(irlba) #load the R library used to compute partial eigen decomposition
library(spam)# load R libraries to facilitate linear algebra computations
library(spam64)# load R libraries to facilitate linear algebra computations


setwd("/Users/angelos/Desktop/") #we set the working directory; be careful to change the path accordingly
cleaned_data = read.csv("cleaned_raw_data.csv") #read cleaned data for imputation 
names = cleaned_data$names
mydata = cleaned_data[,2:6,8:10] #remove some unused variables (used only for plots -not for similarity index)

##########log and logit transformations when needed ##############################
mydata[,c(1:2)] = log(mydata[,1:2])
mydata[,c(3:5)] =log( mydata[,c(3:5)]/(1-mydata[,c(3:5)]) )
##########################################################################################


mydata.imp <- missForest(mydata)$ximp  #impute missing values 

mysimils =gausskernel(mydata.imp, sigma=1) #compute similarity matrix
mysimils[which(mysimils<=10^(-5))]=0 #introduce sparsity to facilitate linear algebra computations by setting low similarities equal to 0


######################Compute regularized Laplacian of similarity matrix#########################################

diag(mysimils) =0
N= dim(mysimils)[1]
DD = rep(NA,N)
for(i in 1:N) DD[i] = sum(mysimils[i,])

DD = DD + mean(DD)
myd =diag.spam(1/sqrt(DD))
tSimils =myd%*%mysimils%*%myd
###############################################################

##################compute partial spectral decomposition of Laplacian##################
K=150
myeigen = partial_eigen(as.dgCMatrix.spam(tSimils), n =K, symmetric = TRUE)
U = myeigen$vectors
####################################

#########################normalize eigenvectors to have unit length####################################
scalar1 <- function(x) {x / sqrt(sum(x^2))}
Ustar = matrix(NA,dim(U)[1],dim(U)[2])
for(i in 1:dim(U)[1]){
  Ustar[i,] = scalar1(U[i,])
}
####################################

##################run k-means####################################
km = kmeans(Ustar,centers = 150,iter.max = 1000)

######################################################

###################find Tsitsipas cluster####################################
size_clsts = km$size
clsts = which(size_clsts>=2)
same_players =list()
tsitsipas_clst=rep(0,length(clsts))
for(i in 1:length(clsts)){
  same_players[[i]] =  which( km$cluster==clsts[i] ) 
  if(length(  intersect(same_players[[i]],which(names=="Stefanos Tsitsipas")))>0)
  {
    tsitsipas_clst[i] = 1
  }
}
select_tsitsip_clst = same_players[[which(tsitsipas_clst>0)]]
select_tsitsip_clst=select_tsitsip_clst[-5] #we exclude the fifth member of the cluster because he seems to be an outlier due to two injuries that he had and he stopped and started again
tsitsipas_clst_data = cleaned_data[select_tsitsip_clst,]
tsitsipas_clst_names = names[select_tsitsip_clst]
########################################################################



euclid_dist =function(x,y){ sqrt(sum(( x-y )^2  ))} #function to calculate euclidean distance of two vectors

myrankings = read.csv("ultimate_tennis_rankings_historical.csv")#read rankings data
tsitsipas_clst_data = cleaned_data[select_tsitsip_clst,] #data for players in  Tsitsipas cluster


tsitsipas_cluster_center = km$centers[which(tsitsipas_clst>0),]#center of StefanosT's cluster
dists = rep(NA,length(select_tsitsip_clst))
for(j in 1:length(select_tsitsip_clst)) dists[j] = euclid_dist(tsitsipas_cluster_center, Ustar[which(names==tsitsipas_clst_names[j]),])#calculate distances from center


##################from rankings data select only those for the players you want to use to predict Tsitsipas (in other cases change cluster as well)#######
rankings_data =matrix(NA,8,18)
inds_for_pred = 1:8
jj=0
for(j in inds_for_pred){
  jj=jj+1
  myinds =which(myrankings$name==tsitsipas_clst_names[j])
  rankings_data[jj,1:length(myinds)]= myrankings[myinds,1]
}

rankings_data = rankings_data[,6:15] #keep 10 years after the fifth of their path

########compute predictions (do not forget to change quantile limits for different players)
pred = predup=predlow = rep(NA,10)
for(t in 1:10){
  predlow[t] =rankings_data[order(rankings_data[,t],na.last = NA)[1],t]
  predup[t] = rankings_data[order(rankings_data[,t],na.last = NA)[3],t]
  pred[t] =round(0.5*(predup[t]+predlow[t]))
  
  ######use the code below (change FALSE to TRUE) to predict other than Tstisipas and Zverev
  if(FALSE){
    inds = 1:(length(which(!is.na(rankings_data[,t]))))
    pred[t] = mean(rankings_data[order(rankings_data[,t],na.last = NA)[inds],t],na.rm=T)
    predlow[t] = rankings_data[order(rankings_data[,t],na.last = NA)[1],t]
    predup[t] = rankings_data[order(rankings_data[,t],na.last = NA)[length(which(!is.na(rankings_data[,t])))],t]
  }
}

############################################################################################################


