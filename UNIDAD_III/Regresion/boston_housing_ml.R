#install.packages("mlbench")
#install.packages("caret")

library(mlbench)
library(lattice)
library(ggplot2)
library(caret)

#Carga de datos
data("BostonHousing")

#Exploracion de datos
head(BostonHousing)
str(BostonHousing)
summary(BostonHousing)

#Limpieza de datos
sum(is.na(BostonHousing))

#Preparacion de los conjuntos de datos
set.seed(100)
configuracion <- createDataPartition(BostonHousing$medv, p = 0.8, list= FALSE)
datos_entrenamiento <- BostonHousing[configuracion,]
datos_testeo <- BostonHousing[-configuracion,]

#Creacion Modelo
Modelo <- train(
  medv ~ rm, data = datos_entrenamiento,
  method = "lm",
  na.action = na.omit,
  preProcess = c("scale", "center"),
  trControl = trainControl(method = "none")
)

summary(Modelo)

Modelo.training <- predict(Modelo, datos_entrenamiento)
Modelo.testing <- predict(Modelo, datos_testeo)

cor(datos_entrenamiento$medv, Modelo.training)
cor(datos_testeo$medv, Modelo.testing)

plot(medv~rm, data= datos_entrenamiento, col="blue")
plot(datos_entrenamiento$medv, Modelo.training, col="red")

