data=c(31,29,19,18,31,28,34,27,34,30,16,18,26,27,27,18,24,22,28,24,21,17,24)
n=length(data)
lambda_hat=mean(data)
alpha=0.10

cat("standard deviation by analytical solution\n")
print(sqrt(lambda_hat/n))

cat("standard deviation by MLE large sample theory\n")
print(sqrt(lambda_hat/n))

cat("confidence interval by MLE large sample theory\n")
print(c(lambda_hat-qnorm(alpha/2,lower=F)*sqrt(lambda_hat/n), lambda_hat+qnorm(alpha/2,lower=F)*sqrt(lambda_hat/n)))

n_exp=10000
lambda_hat_samples=rep(NA,n_exp)
for(i in 1:n_exp){
  lambda_hat_sample=rpois(1,n*lambda_hat)/n
  lambda_hat_samples[i]=lambda_hat_sample
}
cat("standard deviation by simulating the analytical form of sampling distribution\n")
print(sd(lambda_hat_samples))
cat("confidence interval by simulating the analytical form of sampling distribution\n")
print(lambda_hat+quantile(lambda_hat-lambda_hat_samples,c(alpha/2,1-alpha/2)))


n_exp=10000
lambda_hat_samples=rep(NA,n_exp)
for(i in 1:n_exp){
  samples=rpois(n,lambda_hat)
  lambda_hat_=mean(samples)
  lambda_hat_samples[i]=lambda_hat_
}

cat("standard deviation by bootstraping\n")
print(sd(lambda_hat_samples))
cat("confidence interval by bootstraping\n")
print(lambda_hat+quantile(lambda_hat-lambda_hat_samples,c(alpha/2,1-alpha/2)))
