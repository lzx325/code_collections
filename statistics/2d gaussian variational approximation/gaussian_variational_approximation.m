

mu=[0.5,0.5]';
U=[
    sqrt(2)/2,-sqrt(2)/2;
    sqrt(2)/2,sqrt(2)/2
];
D=[
    0.04,0;
    0,0.003
];
Sigma=U*D*U';
Lambda=inv(Sigma);
%Sigma=D;

hold on;
gaussian_2d_plot_contour(mu,Sigma,'green');
gaussian_2d_plot_contour(mu,[Lambda(1,1)^(-1),0;0,Lambda(2,2)^(-1)],'red');
gaussian_2d_plot_contour(mu,[Sigma(1,1),0;0,Sigma(2,2)],'blue');
hold off;