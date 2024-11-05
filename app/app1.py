# -*- coding: utf-8 -*-
"""app1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pj3wrxo1rnf3Qf49U4-FLK2R1I_89gt_
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
import plotly.express as px

# Load the dataset
file_path = 'customer_booking.csv'
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
        logistic_model = LogisticRegression(random_state=42)
        logistic_model.fit(X_train, y_train)
        y_pred = logistic_model.predict(X_test)
        report = classification_report(y_test, y_pred)
        st.text("Classification Report:\n" + report)

        # Feature importance for Logistic Regression
        coef = logistic_model.coef_[0]
        feature_importance = pd.DataFrame({'Feature': features.columns, 'Importance': coef})
        feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

        # Plot with Plotly Express
        fig = px.bar(feature_importance, x='Feature', y='Importance', title='Feature Importance (Logistic Regression)')
        st.plotly_chart(fig)

    elif model_choice == "Random Forest":
        rf_model = RandomForestClassifier(random_state=42)
        rf_model.fit(X_train, y_train)
        y_pred = rf_model.predict(X_test)
        report = classification_report(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:, 1])
        st.text("Classification Report:\n" + report)
        st.text(f"ROC-AUC Score: {roc_auc}")

        # Feature importance for Random Forest
        importances = rf_model.feature_importances_
        feature_importance = pd.DataFrame({'Feature': features.columns, 'Importance': importances})
        feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

        # Plot with Plotly Express
        fig = px.bar(feature_importance, x='Feature', y='Importance', title='Feature Importance (Random Forest)')
        st.plotly_chart(fig)

    elif model_choice == "XGBoost":
        xgb_model = XGBClassifier(random_state=42, n_estimators=200, learning_rate=0.1, max_depth=6)
        xgb_model.fit(X_train, y_train)
        y_pred = xgb_model.predict(X_test)
        report = classification_report(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, xgb_model.predict_proba(X_test)[:, 1])
        st.text("Classification Report:\n" + report)
        st.text(f"ROC-AUC Score: {roc_auc}")

        # Feature importance for XGBoost
        importances = xgb_model.feature_importances_
        feature_importance = pd.DataFrame({'Feature': features.columns, 'Importance': importances})
        feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

        # Plot with Plotly Express
        fig = px.bar(feature_importance, x='Feature', y='Importance', title='Feature Importance (XGBoost)')
        st.plotly_chart(fig)

    elif model_choice == "Voting Classifier":
        rf_model = RandomForestClassifier(random_state=42)
        xgb_model = XGBClassifier(random_state=42, n_estimators=200, learning_rate=0.1, max_depth=6)
        voting_clf = VotingClassifier(estimators=[('rf', rf_model), ('xgb', xgb_model)], voting='soft')
        voting_clf.fit(X_train, y_train)
        y_pred = voting_clf.predict(X_test)
        report = classification_report(y_test, y_pred)
        st.text("Classification Report:\n" + report)

        # Feature importance is not available for Voting Classifier directly
        st.write("Feature importance is not directly available for Voting Classifier. You can view individual model importances above.")

st.write("Explore the model performance and metrics using the options above.")