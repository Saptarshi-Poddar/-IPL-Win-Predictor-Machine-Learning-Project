# - IPL-Win-Predictor-Machine-Learning-Project
This project is a Machine Learning-based web application built to predict the win probability of an IPL team during a live match scenario. The app takes in real-time match inputs (teams, city, target, score, overs, wickets) and returns the predicted chances of both batting and bowling teams winning the match.The model was trained using historical IPL ball-by-ball and match data, with critical features engineered to reflect match dynamics like current run rate (CRR), required run rate (RRR), balls left, and wickets in hand. The model is deployed via Streamlit for an interactive web experience.<br>
## Features<br>
- Predicts win probability for any match scenario based on user inputs.<br>
- Calculates dynamic features like runs left, balls left, CRR, RRR.<br>
-  Displays both team probabilities in percentage format.<br>
-Real-time, interpretable results with input feedback.<br>
## Tech Stack Used<br>
### Category	      Tools & Libraries
- Programming     	     Python
- Data Handling	      Pandas, NumPy
- Visualization        	Streamlit
- ML Model	      Scikit-learn, Logistic Regression 
- Model Persistence       	Pickle
- Deployment	           Streamlit App
- IDE/Notebook     	Jupyter Notebook, VS Code
## How It Works (User Inputs)
- Select batting and bowling teams.<br>
- Choose match venue (city).<br>
- Enter target score, current score, overs completed, and wickets fallen.<br>
- Click Predict Probability to get:<br>
- Batting Team Win %<br>
- Bowling Team Win %<br>
