data()

data(women)

head(women)
tail(women)
summary(women)

women$height[1]
women$weight[1]

plot(weight~height, data = women, col="blue")

#creacion de Linear Model
modelo <- lm(weight~height, data = women)
modelo

#predecir_peso <- Theta0 + Tetha1*x
predecir_peso <- -87.52 + 3.45*women$height[1]
predecir_peso
women$weight[1]

error <- predecir_peso - women$weight[1]
error

abline(modelo, col="red")


predecir_peso <- -87.52 + 3.45*65
predecir_peso
