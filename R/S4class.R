# define S4 class
student=setClass("student", slots=list(name="character", age="numeric", GPA="numeric"))
s <- new("student",name="John", age=21, GPA=3.5)
s2 = student(name="Li",age=22,GPA=3.4) # using the generator function returned by setClass

setMethod("show",
          "student",
          function(object) {
            cat(object@name, "\n")
            cat(object@age, "years old\n")
            cat("GPA:", object@GPA, "\n")
          }
)

# S4 inheritance example
setClass(
  "Person",
   slots=list(name="character",age="numeric")
)
setClass(
  "Employee",
  slots=list(working_experience="numeric"),
  contains="Person"
)
alice=new("Person",name="Alice",age=40)
john=new("Employee",name="John",age=20,working_experience=10)

# S4 inherits S3 or base type object example
setClass("RangedNumeric",
         contains = "numeric",
         slots = list(min = "numeric", max = "numeric"))
rn=new("RangedNumeric",min=1,max=10,1:10)
## The @.Data field contains the underlying S3 object or base type object
print(rn@.Data)

# modifying S4 objects in function will not work
changeAge=function(person){person@age=100}
changeAge(alice)
show(alice)