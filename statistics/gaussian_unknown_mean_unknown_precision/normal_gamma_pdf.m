function density=normal_gamma_pdf(mu,tau,mu0,lambda0,alpha0,beta0)
tau_density=gampdf(tau,alpha0,1/beta0);
mu_density=normpdf(mu,mu0,1/sqrt(lambda0*tau));
density=tau_density*mu_density;
end