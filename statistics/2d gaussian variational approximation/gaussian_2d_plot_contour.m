function gaussian_2d_plot_contour(mu,Sigma,color)
x1 = linspace(0,1);
x2 = linspace(0,1);
K_value=zeros(length(x1),length(x2));
for i=1:length(x1)
    for j=1:length(x2)
        x=[x1(i),x2(j)]';
        K_value(j,i)=(x-mu)'*(Sigma\(x-mu));
    end
end
contour(x1,x2,K_value,[1,4,9],color); % note the chi-square distribution of (x-mu)'*Lambda*(x-mu), with df=2
pbaspect([1 1 1]);
end