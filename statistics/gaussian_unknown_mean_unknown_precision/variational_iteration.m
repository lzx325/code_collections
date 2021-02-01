function [mu_post,lambda_post,alpha_post,beta_post]=variational_iteration(X,mu0,lambda0,alpha0,beta0,n_iter)
X_bar=mean(X);
X_sq_bar=mean(X.^2);
N=length(X);
mu_post=(lambda0*mu0+N*X_bar)/(lambda0+N);
alpha_post=alpha0+N/2;
E_mu=mu_post;
E_mu_sq=X_sq_bar;
E_tau=0;
for it=1:n_iter
    E_tau=(alpha0+N/2)/(1/2*  ( (N+lambda0)*E_mu_sq - 2*(lambda0*mu0+N*X_bar)*E_mu+lambda0*mu0^2 + N*X_sq_bar ) );
    E_mu_sq=1/((lambda0+N)*E_tau)+E_mu^2;
end
lambda_post=(lambda0+N)*E_tau;
beta_post=beta0+(1/2*  ( (N+lambda0)*E_mu_sq - 2*(lambda0*mu0+N*X_bar)*E_mu+lambda0*mu0^2 + N*X_sq_bar ) );
end