%% Seed
close all;
rng(6);
%% ground truth
MU=0;
TAU=1;
%% Sample Data
X=normrnd(MU,1/sqrt(TAU),1,30);
%% Prior Hyperparameters
mu0=0;
lambda0=1;
alpha0=1;
beta0=1;
%% Analytical Solution
n=length(X);
mu_post=(lambda0*mu0+n*mean(X))/(mu0+n);
lambda_post=lambda0+n;
alpha_post=alpha0+n/2;
beta_post=beta0+1/2*n*var(X,1)+n*lambda0/(lambda0+n)*(mean(X)-mu0)^2/2;
fprintf("mu_post=%.4f, lambda_post=%.4f, alpha_post=%.4f, beta_post=%.4f\n",mu_post,lambda_post,alpha_post,beta_post);
plot_density(@(x)(normal_gamma_pdf(x(1),x(2),mu_post,lambda_post,alpha_post,beta_post)),'green');
%% Variational Approximation
hold on;
[mu_post,lambda_post,alpha_post,beta_post]=variational_iteration(X,mu0,lambda0,alpha0,beta0,10);
fprintf("mu_post=%.4f, lambda_post=%.4f, alpha_post=%.4f, beta_post=%.4f\n",mu_post,lambda_post,alpha_post,beta_post);
plot_density(@(x)(normpdf(x(1),mu_post,1/sqrt(lambda_post))*gampdf(x(2),alpha_post,1/beta_post)),'blue');
hold off;