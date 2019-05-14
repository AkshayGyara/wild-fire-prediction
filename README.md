# Big Data Driven Wildfire Risk Analysis and Prediction
Wildfire prediction constitutes a significant component of forest fire management. It plays a major role in resource allocation, mitigation and recovery efforts. 

This repository contains description and analysis of wild ]fire prediction methods based on artificial intelligence utilising two different types of data - weather data and satellite images. Wildfire risk prediction algorithms, based on Logistic Regression, Random Forests, Convolutional neural networks and Faster-R-CNN are presented. The algorithms depend on weather conditions and satellite images of a particular location in order to predict the fire. The implementation of the algorithms using satellite data and sensor data demonstrated its ability to accurately predict  and detect the fire occurrence. Finally, the outcome of supervised learning was analyzed using cellular automata.

## Weather Data: 

During summers large quantities of dried leaves, grass, deadwood, and small plants fuel the fires in the forest. The wind and the terrain are also key factors that help in spreading the fire across the forest. Relative humidity readings and air temperature forecasts are general conditions that can be an indication of fire danger across the entire fire ground.
The goal in scope is to provide data analytics and insights into the relationship between weather and the possibility of wildfire at San Diego County. The frequency of large wildfires is influenced by a complex combination of natural and human factors. Temperature, terrain slope, relative humidity, wind speed, and vegetation (fuel density) are important aspects of the relationship between fire frequency and ecosystems.

##  Satellite Data: 

As satellite data covers large areas and helps in the identification of extremely large features. Satellite images provide insights about the vegetation changes over the season and the change in human activity over a terrain. These types of data contain information related to the state of crops (NDVI: Normalized Difference Vegetation Index), meteorological conditions (LST: Land Surface Temperature) as well as the fire indicator “Thermal Anomalies”.  These aspects can be leveraged to predict the possibility of fire in a place at a particular time. 
    	
Data source: USGS earth explorer

## Model Evaluations

| **Model** | **dataset size** | **metric status** | **comments** |
| --- | --- | --- | --- |
| Faster R-CNN | 1200 images | mAP: 0.997 | Used techniques to differentiate between cloud and smoke. Classes: smoke and fire |
| CNN | 2000 images | F1 score: 0.85 | Classified into 3 different classes: smoke, fire and nofire. Ran 50 epochs with different optimizations. |
| Logistic regression | 10 years weather data | F1 score = 0.85 | Tweaked number of iterations and random state value |
| Random Forest | 10 years weather data | F1 score = 0.98 | Achieved good results with maxDepth = 8 |
| KNN | 10 years weather data | F1 score = 0.94 | Tweaked value of k (no. of neighbor) |
| SVM | 10 years weather data | F1 score = 0.97 | used gridsearch for getting best parameters of gamma and c hyperparameters to achieve good results |
| Naive Bayes | 10 years weather data | F1 score = 0.54 | Relies on independence assumption. Performed badly because realistically data was interdependent. |
| Decision Tree | 10 years weather data | F1 score = 0.86 | Susceptible to overfitting. maxDepth used was 6. |

