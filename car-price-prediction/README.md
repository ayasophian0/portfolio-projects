# Car Price Prediction: End-to-End Machine Learning Project

This repository documents a comprehensive project focused on predicting used car prices. The project spans the entire machine learning pipeline, from initial data acquisition and cleaning to model development, evaluation, and preparation for deployment.

**Live Application:** [**Aladin's Price Prediction Shop**](https://aladinspricepredictionshop.streamlit.app/)

---

### Project Objective

The primary goal of this project was to develop a robust machine learning model capable of accurately predicting the market price of used vehicles based on a diverse set of features. A secondary objective was to deploy the final model as an interactive web application using Streamlit.

---

### Project Workflow & Key Stages

The project was executed in five distinct phases:

1.  **Part I: Initial Data Cleaning & Preparation**
    *   Commenced with a raw dataset of approximately 29,000 car listings, featuring 58 initial attributes.
    *   Addressed fundamental data quality issues, including incorrect data types, parsing numerical values from strings (e.g., mileage, power, CO₂ emissions), and handling inconsistent formatting.
    *   Identified and initiated strategies for managing complex features containing lists of amenities.

2.  **Part II: Advanced Missing Value Imputation & Feature Refinement**
    *   Implemented targeted strategies for handling missing data, moving beyond simple imputation:
        *   Utilized string manipulation and regular expressions to extract pertinent information from textual columns (`description`, `manufacturer_color`) to fill gaps in features like `paint` and `gearbox`.
        *   Applied domain-specific knowledge (e.g., CO₂ emissions for electric vehicles, Euro emission standard timelines) to guide imputation logic.
        *   Employed `groupby` operations with appropriate aggregation (mode/median) for context-aware imputation.
    *   Engineered new features and standardized existing ones: `power` (to numerical HP), `engine_size` (to Liters), and converted multi-item string columns (e.g., `comfort_convenience`, `extras`) into numerical package counts, subsequently binned into meaningful tiers.
    *   This phase refined the dataset to approximately 28,600 observations and 30 well-defined columns.

3.  **Part III: Outlier Management, Data Standardization & Duplicate Removal**
    *   Conducted thorough outlier detection using statistical methods (histograms, boxplots) and bivariate analysis (scatter plots) for key numerical features like `price`, `co2_emissions`, `empty_weight`, and `fuel_consumption`.
    *   Applied domain knowledge to make informed decisions on treating outliers (capping, removal, or transformation).
    *   Finalized standardization of features like `emission_class` and simplified high-cardinality categorical features (`color`, `upholstery`) through logical grouping.
    *   Identified and removed 4,135 duplicate entries.
    *   The dataset was finalized to **23,858 unique and robust observations across 26 columns.**

4.  **Part IV: Baseline Modeling & Regularization**
    *   Performed machine learning-specific preprocessing, including One-Hot Encoding and Ordinal Encoding for categorical features, and MinMaxScaler for numerical features, orchestrated via `ColumnTransformer`.
    *   Developed and evaluated a baseline Linear Regression model.
    *   Implemented regularized linear models (Ridge and Lasso Regression), performing hyperparameter tuning (alpha values) with GridSearchCV to mitigate multicollinearity (VIF scores were analyzed) and improve generalization.
    *   Strategically filtered the `price` range (removing values <7,500 and >70,000) based on model diagnostic plots, which significantly improved the performance of linear models to an R² of approximately 0.88.

5.  **Part V: Advanced Modeling with XGBoost, Feature Selection & Deployment Preparation**
    *   Implemented an XGBoost Regressor, which demonstrated superior performance, achieving a **test R² of 0.93** and significantly lower MAE (~2,026) and MAPE (~10%).
    *   Conducted strategic feature selection, reducing the feature set from 25 to 14 key predictors to create a more compact and interpretable model for deployment. The `make_model` feature was also simplified to include only the top 20 most frequent models for enhanced usability in the application.
    *   Ensured the final XGBoost model was well-tuned to manage overfitting.
    *   The finalized model was saved for integration into the Streamlit web application.

---

### Key Technologies & Libraries

*   **Programming Language:** Python
*   **Data Manipulation & Analysis:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn (for preprocessing, linear models, metrics, `ColumnTransformer`), XGBoost
*   **Data Visualization:** Seaborn, Matplotlib
*   **Web Application Deployment:** Streamlit

---

### Final Model Performance (XGBoost with Selected Features)

*   **R² (Test Set):** 0.93
*   **Mean Absolute Error (MAE):** Approximately 2,026
*   **Mean Absolute Percentage Error (MAPE):** Approximately 10%

---

This project demonstrates an end-to-end machine learning workflow, emphasizing meticulous data preparation, iterative model development, and a focus on practical application. The resulting Streamlit application provides an interactive platform for predicting car prices based on the developed model.
