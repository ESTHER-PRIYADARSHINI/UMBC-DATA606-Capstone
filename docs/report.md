
# Predicting Customer Bookings

## Title: **Enhancing Buisness Insights For British Airways**

Prepared for **UMBC Data Science Master Degree Capstone Fall 2024** Advised by **Dr. Chaojie (Jay) Wang**  
Author: **FNU Esther Priyadarshini**  
- [GitHub Repository](https://github.com/ESTHER-PRIYADARSHINI/UMBC-DATA606-Capstone/tree/main)
- [LinkedIn Profile](https://www.linkedin.com/in/estherpriyadarshini/)
- [PowerPoint Presentation File](https://docs.google.com/presentation/d/1ahgKaqQC6SdfLLqJFZblKgSkt1iOnSDb/edit?usp=sharing&ouid=109867590505726275106&rtpof=true&sd=true)
- [YouTube Video](https://www.youtube.com/watch?v=uVX-CYmGOTo)

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
 
    ![Unknown-3](https://github.com/user-attachments/assets/9935b290-66e6-4290-a98c-674e5d7ba96a)



## Exploratory Data Analysis (EDA)

### Key Visualizations and Insights

1. **Purchase Lead vs Booking Completion**:
    - The boxplot below shows that customers who complete their bookings (booking_complete = 1) generally have shorter purchase lead times compared to those who do not complete their bookings.
    - Insight: Long purchase lead times may indicate lower commitment, and shorter times may reflect more urgent bookings.

    
   ![newplot-2](https://github.com/user-attachments/assets/b1a24b03-12ab-4b4f-8e32-bdbe260c23a7)

   

3. **Number of Passengers vs Booking Completion**:
    - The bar chart demonstrates that bookings with only one or two passengers dominate the dataset. Customers with a single passenger are less likely to complete their bookings compared to multi-passenger bookings.
    - Insight: Single-passenger bookings could signify exploratory or casual browsing behavior.

    
   ![newplot-3](https://github.com/user-attachments/assets/c32119fa-a8fe-4895-bf7b-a2695d646df1)


5. **Flight Hour vs Booking Completion**:
    - The histogram shows booking completion rates across different flight hours. Booking completion is relatively consistent throughout the day, though early morning hours (e.g., 0–6 AM) show fewer completions.
    - Insight: Customers booking flights during off-peak hours might be less committed.

    
   ![newplot-4](https://github.com/user-attachments/assets/3b90812b-555a-4c6e-b52f-e6141dbc96a1)


6. **Booking Completion Distribution**:
    - The bar chart reveals a significant class imbalance in the dataset, with only 15% of bookings marked as complete and 85% as incomplete.
    - Insight: This imbalance was addressed using SMOTE during preprocessing to improve model performance.

    
   ![newplot](https://github.com/user-attachments/assets/619adcf8-cd8d-4713-b2e8-2b432e2f17de)



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
- Logistic Regression - unsatisfactory results
- Random Forest (with hyperparameter tuning) - improved performance metrics as shown below in screenshots
- XGBoost - improved performance metrics on par with hyperparameter tuned Random Forest with GridSearchCV

### Training Strategy
- Train-test split: 80/20
- Addressed class imbalance with SMOTE.
- Tools: Python, scikit-learn, XGBoost, PlotlyExpress, Streamlit.

### Deployment
- Web app deployed via Streamlit for user interaction with the predictive models.

<img width="1275" alt="Screenshot 2024-11-07 at 2 28 53 PM" src="https://github.com/user-attachments/assets/a5867720-73ea-43b6-9569-ea2ae13de5ec">

<img width="1245" alt="Screenshot 2024-11-07 at 2 29 16 PM" src="https://github.com/user-attachments/assets/53e28e67-cbe2-49bb-8389-2436a059b417">

<img width="904" alt="Screenshot 2024-11-07 at 2 30 04 PM" src="https://github.com/user-attachments/assets/fdf68797-cb31-4920-8266-0acd753eb92e">

<img width="845" alt="Screenshot 2024-11-07 at 2 30 42 PM" src="https://github.com/user-attachments/assets/1e9e7573-5955-4b09-ae48-08902d99bb95">

<img width="853" alt="Screenshot 2024-11-07 at 2 31 02 PM" src="https://github.com/user-attachments/assets/34ba8aa1-8ffc-45ec-b9b0-cd844c3098d0">

<img width="743" alt="Screenshot 2024-11-07 at 2 31 13 PM" src="https://github.com/user-attachments/assets/37ff4cfb-7aa3-4394-a482-bbbd4c16d33d">


### Evaluation Metrics
- Accuracy, Precision, Recall, F1-Score.

<img width="849" alt="Performance metrics" src="https://github.com/user-attachments/assets/444b8c50-c457-4cf0-9e5a-188c90396c7a">


## Conclusion

### Key Findings
- Improved prediction accuracy with ensemble models like Random Forest and XGBoost.
- Feature importance analysis revealed critical factors like `purchase_lead` and `trip_type`.
- Better prediction leads to better strategies which help in booking conversion rates.
- This inturn translates to better buisness outcomes.

### Limitations
- Imbalanced dataset required synthetic oversampling techniques (SMOTE).
- Potential biases in feature engineering.

### Future Work
- Incorporating additional features like customer demographics.
- Experimenting with advanced ensemble techniques and external data sources.

## References

- https://docs.streamlit.io
- https://docs.streamlit.io/get-started

