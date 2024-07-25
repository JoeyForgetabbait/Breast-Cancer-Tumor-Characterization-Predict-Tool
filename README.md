![P (3)](https://github.com/user-attachments/assets/f49ff719-4ad9-47e9-aff1-ce9f7ae2e75e)

### Breast Cancer Tumor Prediction Tool

## Overview

Breast cancer affects approximately 13% of women in the United States and remains a significant health concern. Our project focuses on developing a machine learning model to predict the malignancy of breast masses based on cell nuclei characteristics. 

The dataset comprises 569 samples, with features derived from digitized images of fine needle aspirates of breast masses. These features characterize cell nuclei. The diagnosis column serves as the target variable, while the identity (ID) column, used for identification, will be omitted. Initially, our unoptimized model will utilize 30 features, which will be refined through optimization to enhance model performance.

**Key attributes in this dataset include:**

- ID number
- Diagnosis (M = malignant, B = benign), our target variable.
- Various numerical features such as radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension, computed from digitized images of FNA. Numerical Features are explained further below
+ Radius: Mean of distances from center to points on the perimeter
+ Texture: Standard deviation of gray-scale values
+ Perimeter
+ Area
+ Smoothness: Local variation in radius lengths
+ Compactness: Perimeter² / area - 1.0
+ Concavity: Severity of concave portions of the contour
+ Concave points: Number of concave portions of the contour
+ Symmetry
+ Fractal dimension: "Coastline approximation" - 1
  
Note: The ID column is excluded from the analysis as it is used only for identification.

Our analysis aims to leverage these attributes to develop a robust prediction tool for early diagnosis of breast cancer.

For more information about the dataset, including details about its collection and availability, please refer to the official webpage:
 [Breast Cancer Wisconsin (Diagnostic) Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic).
 The inspiration was derived from a Kaggle Statistical Analysis  [Breast Cancer Data - Statistical Analysis
](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostichttps://www.kaggle.com/code/rohithpai/breast-cancer-data-statistical-analysis)


**Breast Cancer Overview**

According to the American Cancer Society, breast cancer occurs when cells in the breast grow uncontrollably. These cells often form a tumor that can be detected via an x-ray or felt as a lump. The tumor is considered malignant (cancerous) if the cells can invade surrounding tissues or spread to other parts of the body. While breast cancer primarily affects women, men can also develop the disease.

**Dataset Application**

The dataset contains diagnoses of lumps and masses found in patients, classifying them as either malignant (denoted by 'M') or benign (denoted by 'B'). This project will use these classifications to train and evaluate machine learning models, aiming to accurately predict the diagnosis based on the provided attributes.

## Model Performance

In this project, various machine learning algorithms were evaluated, including:
+ **Neural Network Model:** Achieved an accuracy of 99%.

  ![Accuracy rating for neural network model](Resources/image(1).png)
+ **Support Vector Machine (SVM) Model:** Achieved an accuracy of 97%.

  ![Accuracy rating for SVM model for all columns](Resources/image(2).png)
  ![Accuracy rating for SVM model for mean column](Resources/image(3).png)
  ![Accuracy rating for SVM model for standard error column](Resources/image(4).png)
  ![Accuracy rating for SVM model for worst (optimized) column](Resources/image(5).png)
  
For the SVM model, we explored several less optimal versions before finalizing the optimized version that delivered the best performance.

## Feature

Main feature- Predicts the likelihood of breast cancer based on input data if it could be malignant or benign.

## Installation

git clone https://github.com/JoeyForgetabbait/Breast-Cancer-Tumor-Characterization-Predict-Tool.git

## Usage

Provide examples and instructions for using your tool. Include screenshots if possible. For example:



## Example Output

Include a snippet of expected output or results to give users an idea of what to expect.

## Acknowledgment for tools used

**_Programming Languages:_** Python, Html, JavaScript, CSS

**_Python Library:_**
- Flask: https://flask.palletsprojects.com/en/3.0.x/
- Pandas: https://pandas.pydata.org/
- Scikit-Learn: https://scikit-learn.org/stable/
- Pathlib: https://docs.python.org/3/library/pathlib.html
- Numpy: https://numpy.org/
- Joblib: https://joblib.readthedocs.io/en/stable/
- OS: https://docs.python.org/3/library/os.html


