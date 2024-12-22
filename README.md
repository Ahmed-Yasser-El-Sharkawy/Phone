1. Case Description
a. Introduction
The mobile phone market is highly competitive, with companies like Apple and Samsung dominating the industry. Bob, a new entrant, faces the challenge of estimating the price range of his mobile phones accurately. Data mining techniques, especially classification, can provide insights into the relationship between phone features and their price range, enabling strategic decision-making. This project leverages classification techniques to address this challenge.
b. Problem Definition
The primary goal is to predict the price range of mobile phones based on their features. The problem is essential for Bob’s company to compete effectively by understanding market trends and consumer preferences. Solving this issue can improve product pricing strategies and enhance competitiveness.

c. Dataset Description
Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,Samsung etc.
He does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies.
Bob wants to find out some relation between features of a mobile phone(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good at Machine Learning. So he needs your help to solve this problem.

The dataset, sourced from Kaggle, contains 2000 records and 21 features. Key features include:
•	battery_power: Battery capacity (mAh)
•	ram: RAM size (MB)
•	fc: Front camera resolution (MP)
•	int_memory: Internal memory (GB)
•	price_range: Target variable (0: Low, 1: Medium, 2: High, 3: Very High)
The dataset represents various phone features and their corresponding price ranges.

d. Questions to Answer
Which features most influence the price range of mobile phones?
 
Can RAM size and battery power predict higher price ranges?
Yes, RAM size and battery power are among the most significant predictors of higher price ranges in mobile phones.
Importance of RAM Size:
1.	Performance Indicator: RAM size is a direct indicator of the device's ability to handle multiple applications and processes simultaneously. Higher RAM allows for better multitasking, faster app loading, and smoother operation.

2. Data Preprocessing
•	Missing Data Handling: Ensured the dataset was clean with no missing values.
•	Feature Scaling: Applied normalization for features like RAM and battery power.
•	Visualization:
o	Heatmap for missing data.
o	Before-and-after scaling visualizations.
Preprocessing ensures accurate and efficient model performance.
________________________________________
3. Exploratory Data Analysis (EDA)
Visualizations:
•	Correlation Heatmap: Highlighted strong correlations, such as RAM and price range.
•	 
•	Histograms: Displayed feature distributions like battery_power and int_memory.
 
•	Scatter Plots: Explored relationships between screen dimensions and resolution.
Insights:
•	Positive correlation between RAM and price range.
•	Moderate correlation between pixel height/width and price range.
•	Normal distribution for features like internal memory and talk time.
________________________________________
4. Feature Engineering
•	Selected RAM, battery_power, and pixel_resolution as key predictors.
•	Eliminated less relevant features using Recursive Feature Elimination.
•	Created interaction terms for screen dimensions.
Visualizations:
•	Feature importance plots.
 
5. Implementation of Algorithms
In this project, we implemented and evaluated various machine learning algorithms to classify the price range of mobile phones. Each algorithm offers unique capabilities and insights into the dataset. Here's an in-depth discussion of the models used:
________________________________________
1. Support Vector Classifier (SVC)
•	Description: SVC is a powerful classification algorithm that aims to find the hyperplane that best separates data into classes. It performs well in high-dimensional spaces and is robust to overfitting, especially when the number of features exceeds the number of samples.
•	Performance:
o	Train Accuracy: 95.37%
o	Test Accuracy: 95.50%
•	Why it Works Well:
o	SVC leverages kernel functions to map data into higher dimensions, enabling better separation between price range classes.
o	It handles complex relationships in the dataset efficiently.
•	Key Insights: The SVC outperformed other models in terms of accuracy, making it the best-performing model in this analysis.
________________________________________
2. Decision Tree (DT)
•	Description: Decision Trees are tree-structured classifiers that split the dataset based on feature values. Each node represents a decision based on a specific feature, leading to class labels at the leaves.
•	Performance:
o	Train Accuracy: 83.44%
o	Test Accuracy: 81.75%
•	Advantages:
o	Simple and interpretable model.
o	Identifies feature importance directly through splits.
•	Challenges:
o	Prone to overfitting, especially with deep trees.
o	Limited generalization on test data.
•	Key Insights: Although easy to interpret, the Decision Tree underperformed compared to ensemble and advanced models due to its tendency to overfit.
 
________________________________________
3. Random Forest (RF)
•	Description: Random Forest is an ensemble learning method that builds multiple decision trees and combines their outputs for more accurate and stable predictions. It reduces overfitting by averaging results from individual trees.
•	Why We Used It:
o	Handles high-dimensional datasets effectively.
o	Provides feature importance scores, giving insights into the dataset.
•	Advantages:
o	High robustness and generalization ability.
o	Can handle missing values and outliers effectively.
•	Key Insights: Random Forest enhanced the decision-making process by reducing variance seen in single Decision Trees.
 
________________________________________
4. Neural Networks (NN)
•	Description: Neural Networks are computational models inspired by the human brain. They consist of interconnected layers of neurons that capture complex, non-linear relationships within data.
•	Why We Used It:
o	Capable of modeling intricate patterns and interactions in the dataset.
o	Useful for datasets where feature relationships are highly non-linear.
•	Challenges:
o	Requires more computational resources and tuning compared to simpler models.
o	Can overfit if not properly regularized.
•	Key Insights: While NNs can potentially outperform traditional models, their computational cost and need for fine-tuning limited their practicality in this project.
 
________________________________________
Figures:
1.	Decision Boundaries: Visualizing the separation of classes by SVC, DT, and RF.
2.	Feature Importance: Highlighting the most influential features identified by Random Forest.
3.	Performance Metrics: Confusion matrices, ROC curves, and accuracy scores to compare model effectiveness.




6. Model Evaluation and Results
Evaluation Metrics:
•	SVC: Precision, Recall, F1-Score, ROC Curve.
  
•	DT: Confusion Matrix, Accuracy.
Findings:
•	SVC outperformed other models with high accuracy and robust performance.
•	Decision Tree provided interpretable results but underperformed compared to SVC.
________________________________________
7. Data Interpretation
•	RAM is the most significant predictor of price range.
•	Screen dimensions and battery capacity moderately influence pricing.
•	Higher accuracy with SVC highlights its suitability for classification tasks.
________________________________________
8. Insights About This Work
Reflections:
•	Data preprocessing and feature selection were critical to model performance.
•	Balancing model complexity with interpretability was a key challenge.
•	Results can guide pricing strategies and product development.
Challenges:
•	Managing class imbalances in target variable.
•	Hyperparameter tuning for optimal model performance.
________________________________________
9. Implementation
Deployment:
•	Created a Streamlit app for user-friendly predictions.
•	Model saved using Pickle for future use.
Tools:
•	Python (Pandas, Seaborn, Scikit-learn)
•	Streamlit for deployment.
Figures:
•	Screenshot of Streamlit app interface.
 

