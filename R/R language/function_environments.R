fun=function(){
    cat("The local environment of the function, environment(): ","\n")
    print(environment())
    cat("The parent of the local environment of the function, or the environment where fun is defined, parent.env(environment())","\n")
    print(parent.env(environment()))
    cat("The parental frame, parent.frame(): ","\n")
    print(parent.frame())
}

fun2=function() fun()

cat("When calling fun() from globalenv\n\n")
fun()
cat("\n")
cat("When calling fun() from fun2()\n\n")
fun2()

cat("\n")
newenv=new.env()
environment(fun)=newenv
cat("When environment(fun) is changed to newenv\n")
print(newenv)
cat("\n")
fun()
cat("\n")
fun2()

cat("\nThe environment where the function variable 'fun' locates:\n")
print(pryr::where("fun"))