s = list(
  name="John",
  age="21",
  GPA=3.5
)

class(s)="student"
print(s)
student=function(n,a,g){
  if(g>4||g<0) stop("GPA must be between 0 and 4")
  else{
    value=list(name=n,age=a,GPA=g)
    class(value)="student"
  }
  value
}
s2=student("ed",23,2.0)
print.student <- function(obj) {
  cat(obj$name, "\n")
  cat(obj$age, "years old\n")
  cat("GPA:", obj$GPA, "\n")
}
print(s2)
print(.S3methods(class="student"))
print(unclass(s2))

grade <- function(obj) {
  UseMethod("grade")
}
grade.default <- function(obj) {
  cat("grad is a generic function\n")
}
grade.student = function(obj){
  cat("The student's grade is ",obj$GPA,"\n")
}
grade(s2) # use grade.student
grade(c(1,2)) # use grade.default