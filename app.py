import streamlit as st
import pandas as pd
import pickle

# Load model pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("IPL Win Predictor")

# Team and City options 
teams = sorted([
    'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans',
    'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians',
    'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bangalore',
    'Sunrisers Hyderabad'
])

cities = sorted([
    'Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Dharamsala', 'Dubai',
    'Hyderabad', 'Jaipur', 'Kolkata', 'Lucknow', 'Mohali', 'Mumbai',
    'Nagpur', 'Pune', 'Rajkot', 'Sharjah', 'Visakhapatnam'
])


col1, col2 = st.columns(2) # Create two columns for team selection
with col1:
    batting_team = st.selectbox("Select the batting team", teams)
with col2:
    bowling_team = st.selectbox("Select the bowling team", teams)

selected_city = st.selectbox("Select host city", cities)

target = st.number_input("Target", min_value=1)
col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input("Current Score", min_value=0)
with col4:
    overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input("Wickets Out", min_value=0, max_value=10)

# Predict
if st.button("Predict Probability"):  # Button to trigger prediction

    runs_left = target - current_score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_dict = {
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'current_score': [current_score],
        'target': [target],
        'ball_left': [balls_left],
        'wicket_left': [wickets_left],
        'current_runrate': [crr],
        'required_runrate': [rrr],
        'runs_left': [runs_left]
    }

    input_df = pd.DataFrame(input_dict) # Create DataFrame from input dictionary

    # Show user the input going to the model (debugging)
    st.write(" Input sent to model:")
    st.write(input_df)

    # Display the input DataFrame for debugging
    try:  # Predict using the loaded model
        result = pipe.predict_proba(input_df) # Predict probabilities
        loss = result[0][0]  # Probability of bowling team winning
        win = result [0][1]  # Probability of batting team winning

        st.success(f"{batting_team} Win Probability: {round(win * 100)}%")
        st.success(f"{bowling_team} Win Probability: {round(loss * 100)}%")

    except Exception as e: # Handle any errors during prediction
        st.error("Model prediction failed") # Display error message
        st.error(f"Error: {e}")  # Display the error message
        st.write("Make sure input column names and values match what the model was trained on.")
