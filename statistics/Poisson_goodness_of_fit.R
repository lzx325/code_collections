lambda=5

n_exp=30000
n_samples=5000
GLRT_statistics=rep(NA,n_exp)
Pearson_statistics=rep(NA,n_exp)
for(i in 1:n_exp){
  samples=rpois(n_samples,lambda)
  lambda_hat=mean(samples)
  O=rep(NA,5)
  E=rep(NA,5)
  O[1]=sum(samples==0)
  O[2]=sum(samples==1)
  O[3]=sum(samples==2)
  O[4]=sum(samples==3)
  O[5]=sum(samples>3)
  E[1]=dpois(0,lambda_hat)*n_samples
  E[2]=dpois(1,lambda_hat)*n_samples
  E[3]=dpois(2,lambda_hat)*n_samples
  E[4]=dpois(3,lambda_hat)*n_samples
  E[5]=ppois(3,lambda_hat,lower=F)*n_samples
  GLRT_statistic=0
  Pearson_statistic=0
  for(j in 1:5){
    if(O[j]>0){
      GLRT_statistic=GLRT_statistic+2*O[j]*log(O[j]/E[j])
    } 
    
    Pearson_statistic=Pearson_statistic+(O[j]-E[j])^2/E[j]
  }
  GLRT_statistics[i]=GLRT_statistic
  Pearson_statistics[i]=Pearson_statistic

}

hist(GLRT_statistics,prob=T,ylim=c(0,0.4),breaks=seq(0,max(GLRT_statistics),len=100))
x=seq(0,400,len=1e4)
lines(x,dchisq(x,3))
hist(Pearson_statistics,prob=T,ylim=c(0,0.4),breaks=seq(0,max(Pearson_statistics),len=100))
lines(x,dchisq(x,3))
