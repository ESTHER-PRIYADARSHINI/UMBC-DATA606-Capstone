# 1. Title and Author

## Project Title:
Enhancing Business Insights for British Airways: Predictive Modeling and Customer Feedback Analysis

**Prepared for:**  
UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

**Author Name:**  
Esther Priyadarshini

**GitHub Repository:**  
https://github.com/ESTHER-PRIYADARSHINI/UMBC-DATA606-Capstone

**LinkedIn Profile:**  
https://www.linkedin.com/in/estherpriyadarshini/

**PowerPoint Presentation:**  
[Link to PowerPoint presentation]

**YouTube Video:**  
[Link to YouTube video presentation]

---

# 2. Background

This project is focused on providing actionable business insights to British Airways by analyzing both customer review data and a dataset of customer bookings. Two main objectives are pursued:

1. **Customer Review Analysis**: Scrape and analyze reviews from Skytrax, focusing on common complaints and areas for improvement. This analysis will provide recommendations for enhancing customer experience.

2. **Booking Data Analysis**: Using a dataset provided by British Airways, analyze factors that influence whether a customer completes a booking. We aim to build a machine learning model to predict booking completion based on customer behavior and preferences.

### Why Does It Matter?

- Airlines operate in a highly competitive industry, and customer feedback is crucial for improving service quality.
- Understanding factors that drive or prevent customers from completing bookings can help British Airways refine its business strategies to increase customer conversion and loyalty.

### Research Questions

1. **Customer Reviews:**
   - What are the most common complaints or areas of praise in British Airways customer reviews?
   - How do customer sentiments correlate with various aspects of the airline service (e.g., in-flight meals, seat comfort, baggage policies)?

2. **Customer Bookings:**
   - What factors contribute the most to a customer completing a booking?
   - Can we predict whether a customer will complete a booking based on available data such as route, sales channel, or trip type?
   - How can British Airways improve its offerings to increase the likelihood of customers completing a booking?

---

# 3. Data

### 1. **Customer Reviews (Web Scraped)**

- **Source**: Skytrax (Airline review website)
- **Data Type**: Object type, containing customer reviews.
- **Data Size**: 3.5 MB
- **Data Shape**: 3858 rows and 2 columns
- **Time Period**: 2011 to 2024

### 2. **Customer Booking Dataset**

- **Source**: British Airways
- **Data Size**: 5.3 MB (50,000 rows, 14 columns)
- **Time Period**: The dataset is anonymised and does not specify the time period, but it represents recent booking data.
- **Row Representation**: Each row represents a customer booking attempt.

#### Data Dictionary:

| Column Name            | Data Type | Definition                                                              | Potential Values                      |
|------------------------|-----------|-------------------------------------------------------------------------|---------------------------------------|
| `num_passengers`        | int64     | Number of passengers traveling                                          | Integer                               |
| `sales_channel`         | object    | Sales channel the booking was made on                                   | Online, Mobile                        |
| `trip_type`             | object    | Type of trip (Round Trip, One Way, Circle Trip)                         | Categorical (Round Trip, One Way)     |
| `purchase_lead`         | int64     | Number of days between booking and travel date                          | Integer                               |
| `length_of_stay`        | int64     | Number of days spent at the destination                                 | Integer                               |
| `flight_hour`           | int64     | Hour of the flight departure                                            | Integer (0-23)                        |
| `flight_day`            | object    | Day of the week of flight departure                                     | Categorical (Monday-Sunday)           |
| `route`                 | object    | Flight route (Origin -> Destination)                                    | Categorical (e.g., JFK -> LHR)        |
| `booking_origin`        | object    | Country from where the booking was made                                 | Categorical (e.g., USA, UK)           |
| `wants_extra_baggage`   | int64     | If the customer wanted extra baggage                                    | Binary (1 = Yes, 0 = No)              |
| `wants_preferred_seat`  | int64     | If the customer wanted a preferred seat                                 | Binary (1 = Yes, 0 = No)              |
| `wants_in_flight_meals` | int64     | If the customer wanted in-flight meals                                  | Binary (1 = Yes, 0 = No)              |
| `flight_duration`       | float64   | Total flight duration (in hours)                                        | Float                                 |
| `booking_complete`      | int64     | Whether the customer completed the booking (Target Variable)            | Binary (1 = Yes, 0 = No)              |

**Target Variable:**  
`booking_complete` (1 = Booking Complete, 0 = Booking Incomplete)

**Potential Features for Modeling:**

- `num_passengers`
- `purchase_lead`
- `length_of_stay`
- `flight_hour`
- `flight_day`
- `route`
- `booking_origin`
- `wants_extra_baggage`
- `wants_preferred_seat`
- `wants_in_flight_meals`
- `flight_duration`
- `sales_channel`

