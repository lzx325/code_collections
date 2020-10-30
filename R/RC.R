Polygon=setRefClass("Polygon")
Regular=setRefClass("Regular")

# Specify parent classes
Triangle=setRefClass("Triangle", contains = "Polygon")
EquilateralTriangle=setRefClass("EquilateralTriangle",
            contains = c("Triangle", "Regular"))
Polygon=setRefClass("Polygon", fields = c("sides"))

student <- setRefClass("student",
                       fields = list(name = "character", age = "numeric", GPA = "numeric"))
s1=student(name="ally",age=12,GPA=3.0)
s2=s1
s2$age=14
print(s1) # s1$age will change accordingly
s3=s1$copy()
print(s3)