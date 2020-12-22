install.packages("ggplot2")
install.packages("GGally")

library(ggplot2)
library(GGally)

# Carga de datos
data(iris)

d_iris <- iris
head(d_iris)
tail(d_iris)
str(d_iris)

summary(d_iris)

#Preprocesamiento
d_iris <- d_iris[1:100,]

set.seed(100)
N <- sample(1:100, 70) # 70% de entrenamiento
N
d_train <- d_iris[N,]
d_test <- d_iris[-N,]

summary(d_train)
summary(d_test)

#Exploracion
ggpairs(d_iris, mapping=ggplot2::aes(colour = Species))
ggpairs(d_train, mapping=ggplot2::aes(colour = Species))
ggpairs(d_test, mapping=ggplot2::aes(colour = Species))

#Grafica resalta una especie
x <- iris[sample(1:nrow(iris)),]
x <- cbind(x, useless = rnorm(nrow(x)))
x$virginica <- x$Species == "virginica"
x$Species <- NULL
plot(x, col= x$virginica + 1)


#Generar modelo
y <- d_train$Species #objetivo
X <- d_train$Petal.Length

#crear el modelo
modelo <- glm(y~X, family = "binomial")
summary(modelo)

#Evaluar el modelo

nuevas_entradas <- data.frame(x = d_test$Petal.Length)
predicciones <- predict(modelo, nuevas_entradas, type = "response")
predicciones
resultados <- data.frame(d_test$Petal.Length, d_test$Species, predicciones)
resultados

#graficar
qplot(resultados[, 1], round(resultados[,3]), col = resultados[,2], xlab = "Tamaño de Petalo", ylab= "Predicciones")

  
  
  
  
  
  
  