
# Predicting Customer Bookings

Prepared for **UMBC Data Science Master Degree Capstone** by **Dr. Chaojie (Jay) Wang**  
Author: **Esther Priyadarshini**  
- [GitHub Repository](https://github.com/ESTHER-PRIYADARSHINI/UMBC-DATA606-Capstone/tree/main)
- [LinkedIn Profile](https://www.linkedin.com/in/estherpriyadarshini/)
- [PowerPoint Presentation File](#)
- [YouTube Video](#)

## Background

### Project Overview
This project aims to build a predictive model to understand factors influencing booking completion, ultimately enhancing business strategies for improved conversion rates.

### Why Does It Matter?
Better prediction capabilities lead to actionable strategies, enabling businesses like British Airways to optimize marketing, target key customer segments, and increase booking conversion rates.

### Research Questions
1. What are the key factors influencing customer booking completion?
2. How accurately can customer booking completion be predicted using machine learning models?
3. Which features have the highest impact on booking completion?

## Data

### Dataset Overview
- **Source**: British Airways
- **Size**: 50,000 rows × 14 columns (3.1 MB)
- **Representation**: Each row represents a customer booking attempt.
- **Class Imbalance**: 85% incomplete bookings, 15% complete bookings.
  - Addressed using the SMOTE technique.

### Data Dictionary
| Column Name           | Data Type | Definition                                     | Potential Values (if categorical) |
|-----------------------|-----------|-----------------------------------------------|-----------------------------------|
| `num_passengers`      | Integer   | Number of passengers traveling                | -                                 |
| `sales_channel`       | Categorical | Channel where the booking was made            | Internet, Mobile                 |
| `trip_type`           | Categorical | Type of trip                                  | RoundTrip, CircleTrip, OneWay    |
| `purchase_lead`       | Integer   | Days between travel and booking date          | -                                 |
| `length_of_stay`      | Integer   | Days spent at the destination                 | -                                 |
| `flight_hour`         | Integer   | Hour of flight departure                      | 0–23                              |
| `flight_day`          | Categorical | Day of the week of flight departure           | Mon, Tue, ..., Sun               |
| `route`               | Categorical | Flight route (Origin -> Destination)          | High cardinality (~1000+ routes) |
| `booking_origin`      | Categorical | Country from where the booking was made       | ~100 countries                   |
| `wants_extra_baggage` | Boolean    | Whether customer opted for extra baggage      | True, False                      |
| `wants_preferred_seat`| Boolean    | Whether customer opted for a preferred seat   | True, False                      |
| `wants_in_flight_meals`| Boolean   | Whether customer opted for in-flight meals    | True, False                      |
| `flight_duration`     | Float      | Total duration of the flight (in hours)       | -                                 |
| `booking_complete`    | Boolean    | Whether the booking was completed             | True, False                      |

### Key Insights
- Correlation matrix:
  - **Flight duration**: Negatively correlated with booking completion (-0.11).
  - **Number of passengers**: Negatively correlated with length of stay (-0.12).

## Exploratory Data Analysis (EDA)

- Summary statistics for target variable and predictors:
    - `purchase_lead`: Mean and standard deviation [to be computed].
    - `length_of_stay`: Distribution analysis.
    - `flight_duration`: Box plots to analyze spread.
- Visualizations:
    - Bar plots for categorical features (e.g., `sales_channel`, `trip_type`).
    - Histograms for numerical features (e.g., `purchase_lead`).
    - Correlation heatmap for numerical predictors.
- Data cleaning steps: Addressed missing values (none), duplicates (none), and high-cardinality issues (e.g., `route` frequency encoding).
- Feature engineering: Encoding categorical variables, normalization, and SMOTE.

## Model Training

### Models
- Logistic Regression
- Random Forest (with hyperparameter tuning)
- XGBoost

### Training Strategy
- Train-test split: 80/20
- Addressed class imbalance with SMOTE.
- Tools: Python, scikit-learn, XGBoost, Plotly.

### Deployment
- Web app deployed via Streamlit for user interaction with the predictive models.

### Evaluation Metrics
- Accuracy, Precision, Recall, F1-Score, ROC-AUC.

## Conclusion

### Key Findings
- Improved prediction accuracy with ensemble models like Random Forest and XGBoost.
- Feature importance analysis revealed critical factors like `purchase_lead` and `trip_type`.
- Better prediction  Better strategies  Higher booking conversion rates.

### Limitations
- Imbalanced dataset required synthetic oversampling techniques (SMOTE).
- Potential biases in feature engineering.

### Future Work
- Incorporating additional features like customer demographics.
- Experimenting with advanced ensemble techniques and external data sources.

## References

- [List of references and resources used in the project]