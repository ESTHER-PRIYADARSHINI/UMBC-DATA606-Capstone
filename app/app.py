# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12VHaEGAw2pv3quAYzKoUauBuDdvccjuh
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE

# Load the dataset
file_path = 'customer_booking.csv'  # Make sure this file is in the same directory
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Preprocess data
day_mapping = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
df['flight_day_encoded'] = df['flight_day'].map(day_mapping)

label_encoder_sales_channel = LabelEncoder()
label_encoder_trip_type = LabelEncoder()
df['sales_channel_encoded'] = label_encoder_sales_channel.fit_transform(df['sales_channel'])
df['trip_type_encoded'] = label_encoder_trip_type.fit_transform(df['trip_type'])

route_freq_encoding = df['route'].value_counts(normalize=True)
booking_origin_freq_encoding = df['booking_origin'].value_counts(normalize=True)
df['route_encoded'] = df['route'].map(route_freq_encoding)
df['booking_origin_encoded'] = df['booking_origin'].map(booking_origin_freq_encoding)

# Select features and target variable
features = df[['num_passengers', 'purchase_lead', 'length_of_stay', 'flight_hour',
               'flight_day_encoded', 'wants_extra_baggage', 'wants_preferred_seat',
               'wants_in_flight_meals', 'flight_duration', 'sales_channel_encoded',
               'trip_type_encoded', 'route_encoded', 'booking_origin_encoded']]
target = df['booking_complete']

# Feature scaling and SMOTE
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(features_scaled, target)
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Streamlit app
st.title("Customer Booking Prediction App")

# Model selection
model_choice = st.selectbox("Choose a model to train and run:", ["Logistic Regression", "Random Forest", "XGBoost", "Voting Classifier"])

if st.button("Train and Run Model"):
    if model_choice == "Logistic Regression":
        # Train Logistic Regression model
        logistic_model = LogisticRegression(random_state=42)
        logistic_model.fit(X_train, y_train)
        y_pred = logistic_model.predict(X_test)
        report = classification_report(y_test, y_pred)
        st.text("Classification Report:\n" + report)

    elif model_choice == "Random Forest":
        # Train Random Forest model
        rf_model = RandomForestClassifier(random_state=42)
        rf_model.fit(X_train, y_train)
        y_pred = rf_model.predict(X_test)
        report = classification_report(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:, 1])
        st.text("Classification Report:\n" + report)
        st.text(f"ROC-AUC Score: {roc_auc}")

    elif model_choice == "XGBoost":
        # Train XGBoost model
        xgb_model = XGBClassifier(random_state=42, n_estimators=200, learning_rate=0.1, max_depth=6)
        xgb_model.fit(X_train, y_train)
        y_pred = xgb_model.predict(X_test)
        report = classification_report(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, xgb_model.predict_proba(X_test)[:, 1])
        st.text("Classification Report:\n" + report)
        st.text(f"ROC-AUC Score: {roc_auc}")

    elif model_choice == "Voting Classifier":
        # Train Voting Classifier model
        rf_model = RandomForestClassifier(random_state=42)
        xgb_model = XGBClassifier(random_state=42, n_estimators=200, learning_rate=0.1, max_depth=6)
        voting_clf = VotingClassifier(estimators=[('rf', rf_model), ('xgb', xgb_model)], voting='soft')
        voting_clf.fit(X_train, y_train)
        y_pred = voting_clf.predict(X_test)
        report = classification_report(y_test, y_pred)
        st.text("Classification Report:\n" + report)

st.write("Explore the model performance and metrics using the options above.")