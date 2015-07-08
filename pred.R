
setwd("D:/money")
source("gbg_2015.R")
setwd("D:/money")
model1=read.csv("model.csv",stringsAsFactors = FALSE)
n=5
means<-apply(model1, 2, mean) 
sds<-apply(model1, 2, sd)   

model=scale(model1,means,sds)

pred=function(g,h){
tv=as.numeric(c(f(g),f(h)))
tv=(tv-means[-c(1,8)])/sds[-c(1,8)]
cos.sim=function(ma, mb){
  mat=sum(diag(tcrossprod(ma, mb)))
  t1=sqrt(sum(ma*ma))
  t2=sqrt(sum(mb*mb))
  mat / (t1*t2)
}
tc=c()
guest=c()
host=c()
for(i in 1:dim(model[,-c(1,8)])[1]){
  guest[i]=model1[i,1]
  host[i]=model1[i,8]
  tc[i]=(cos.sim(tv,as.numeric(model[i,-c(1,8)])))
}
data=data.frame("similarity"=tc,"guest"=guest,"host"=host)
data=data[order(data$similarity,decreasing = TRUE),]
data=head(data,n)

c(weighted.mean(data$guest, data$similarity),weighted.mean(data$host, data$similarity))
#c(weighted.mean(data$guest, 10:1),weighted.mean(data$host, 10:1))

#data
}
pred("CIN","WSN")
pred("SDP","PIT")
#
pred("HOU","CLE")
pred("STL","CHC")
pred("ATL","MIL")
pred("TBR","KCR")
pred("TOR","CHW")
pred("BAL","MIN")
pred("DET","SEA")
pred("NYM","SFG")
pred("NYM","SFG")
pred("OAK","NYY")
pred("MIL","CIN")
pred("PHI","ATL")
pred("LAA","COL")

pred("MIA","BOS")

pred("PHI","LAD")

pred("ARI","TEX")
