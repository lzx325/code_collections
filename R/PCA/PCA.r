library(datasets)
data(iris)

iris_mat=as.matrix(iris[,1:4])
iris_mat_mean=apply(iris_mat,2,mean)
iris_mat_center=iris_mat-rep(iris_mat_mean,each=nrow(iris_mat))

pc=prcomp(iris_mat,rank.=3)

print(iris_mat_mean)
print(pc$center)

pc$rotation

# The following are same
head(predict(pc))
head(predict(pc,iris_mat))
head((iris_mat_center %*% pc$rotation))


