setwd("D:/money")
schedule=read.csv("mlb_schedule_2014.csv",stringsAsFactors = FALSE)
boxscore=read.csv("mlb_boxscore_2014.csv",stringsAsFactors = FALSE)
f=function(x){
  #x="KCR"
  data=merge(schedule[schedule$tm==x,],boxscore,by="boxscore")
  data=data[order(data$rk),]
  head(data)
  data$era<-rep("",dim(data)[1])
  data$whip<-rep("",dim(data)[1])
  data$so9<-rep("",dim(data)[1])
  data$ba<-rep("",dim(data)[1])
  data$obp<-rep("",dim(data)[1])
  data$slg<-rep("",dim(data)[1])
  for(i in 6:dim(data)[1]){
    ip=0
    er=0
    so=0
    bb=0
    h=0#被打的安打
    hh=0#自己打的安打
    bbb=0#
    ab=0
    hbp=0
    sf=0
    tb=0
    for(j in (i-5):(i-1)){
      bbb=bbb+ifelse(data[j,"ha"]=="@",data[j,"gbb"],data[j,"hbb"])
      hbp=hbp+ifelse(data[j,"ha"]=="@",data[j,"ghbp"],data[j,"hhbp"])
      sf=sf+ifelse(data[j,"ha"]=="@",data[j,"gsf"],data[j,"hsf"])
      hh=hh+ifelse(data[j,"ha"]=="@",data[j,"gh"],data[j,"hh"])
      ab=ab+ifelse(data[j,"ha"]=="@",data[j,"gab"],data[j,"hab"])
      so=so+ifelse(data[j,"ha"]=="@",data[j,"hso"],data[j,"gso"])
      bb=bb+ifelse(data[j,"ha"]=="@",data[j,"hbb"],data[j,"gbb"])
      h=h+ifelse(data[j,"ha"]=="@",data[j,"hh"],data[j,"gh"])
      ip=ip+ifelse(data[j,"ha"]=="@",data[j,"gip"],data[j,"hip"])
      er=er+ifelse(data[j,"ha"]=="@",data[j,"ger"],data[j,"her"])
      tb=tb+ifelse(data[j,"ha"]=="@",data[j,"gslg"]*data[j,"gab"],data[j,"hslg"]*data[j,"hab"])
      
      data[i,"era"]<-9*er/ip
      data[i,"so9"]<-9*so/ip
      data[i,"whip"]<-(bb+h)/ip
      data[i,"ba"]<-hh/ab
      data[i,"obp"]<-(hh+bbb+hbp)/(ab+bbb+hbp+sf)
      data[i,"slg"]<-tb/ab
    }
    
  }
  schedule_v1=schedule[schedule$tm==x,]
  output=cbind(schedule_v1[,c("r","boxscore","ha")],data[,c("era","whip","so9","ba","obp","slg")])
  output
  
}

f("LAD")
total=f("ARI")
for(i in 2:length(unique(schedule$tm))){
  total=rbind(total,f(unique(schedule$tm)[i]))
}


ubx=unique(total$boxscore)
tdata=total[total$boxscore==ubx[1],]
sg=cbind(tdata[tdata$ha=="@",],tdata[tdata$ha=="",])[,c(1,4:10,13:18)]
ttdata=sg
for(i in 2:length(ubx)){
  tdata=total[total$boxscore==ubx[i],]
  sg=cbind(tdata[tdata$ha=="@",],tdata[tdata$ha=="",])[,c(1,4:10,13:18)]
  ttdata=rbind(ttdata,sg)
  
}
dim(ttdata)
ttdata<-ttdata[ttdata$era!="" & ttdata$era.1!="",]

names(ttdata)
write.table(ttdata, file ="model.csv",row.names=FALSE,sep=",")
