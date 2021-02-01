function gaussian_2d_plot_contour(density_fun,color)
x1 = linspace(-1,1);
x2 = linspace(0,2);
K_value=zeros(length(x1),length(x2));
for i=1:length(x1)
    for j=1:length(x2)
        x=[x1(i),x2(j)];
        K_value(j,i)=density_fun(x);
    end
end
contour(x1,x2,K_value,color);
%contourf(x1,x2,K_value,'LineColor','none');
%colorbar;
pbaspect([4 3 1]);
end