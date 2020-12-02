#install.packages("MASS")
#install.packages("ISLR")

library(MASS)
library(ISLR)

data(Boston)
summary(Boston)

plot(medv~crim, data= Boston, col="blue")
plot(medv~zn, data= Boston, col="blue")

#matriz de correlacion
pairs(~ medv + crim + zn + indus + chas + nox + rm + age + dis + rad + tax + ptratio + black + lstat, data= Boston, main= "Correlacion de atributos de Boston")

pairs(~ medv + rm + lstat, data= Boston, main= "Correlacion de atributos de Boston")

#crear modelo lineal
Modelo1 = lm(medv~rm, data = Boston)
summary(Modelo1)

grafico1 <- plot(medv~rm, data = Boston, col= "blue")
abline(Modelo1, col= "red")
#predecir
confint(Modelo1)
predict(Modelo1, data.frame(rm = c(10,20,30)), interval = "confidence")

#crear modelo lineal
Modelo2 = lm(medv~lstat, data = Boston)
summary(Modelo2)
grafico2 <- plot(medv~lstat, data = Boston, col= "blue")
abline(Modelo2, col= "red")
#predecir
confint(Modelo2)
predict(Modelo2, data.frame(lstat = c(10,20,30)), interval = "confidence")



