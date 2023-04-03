#Temperature Analysis

library('ggplot2')
library('forecast')
library('tseries')
library('plotly')
library('zoo')
library('xts')
data<- read.csv("data/avg_temp.csv")
data$Date <- as.Date(data$Date, format = "%Y-%m-%d")
data <- data[order(data$Date), ]
data<- as.xts(data, order.by = data$Date)

plot_ly(data = data, x = data$Date.Number, y = data$Anomaly,
        type = 'scatter', mode = 'lines')

#Make 1 year summary
data$one_yrs <-NA
data$one_yrs <- rollmean(data$Anomaly, k=365, fill = NA)

plot_ly(data = data, x = data$Date.Number, y = data$one_yrs,
        type = 'scatter', mode = 'lines')

#Make 10 year summary

data$one_yrs <- rollmean(data$Anomaly, k=12, fill = NA)

plot_ly(data = data, x = data$Date, y = data$one_yrs,
        type = 'scatter', mode = 'lines')
