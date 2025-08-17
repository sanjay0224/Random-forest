🏷️ Random Forest – Customer Purchase Prediction
📌 Project Overview

This project is a Machine Learning web application built with Flask (backend) and HTML/CSS (frontend).
It uses a Random Forest Classifier to predict whether a customer is likely to purchase a product based on age, income, and browsing time.

Users can enter their details in the web form, and the model will output either "Likely to Purchase" or "Not Likely to Purchase".

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/randomforest_purchase_prediction.git
cd randomforest_purchase_prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model
python train_model.py

4️⃣ Run the Application
python app.py


The app will run on http://127.0.0.1:5000/.

🧠 Model Details

Algorithm: Random Forest Classifier

Library: scikit-learn

Dataset Features:

Age — Customer’s age

Annual Income — Estimated income in $

Browsing Time — Time spent on website (in minutes)

Purchase — Target variable (1 = Purchased, 0 = Not Purchased)

📊 Prediction Flow

User enters age, annual income, and browsing time.

Flask sends the input to the trained Random Forest model.

Model predicts whether the customer is likely to purchase.

Result is displayed on the output page.

📸 Screenshots
<img width="1600" height="750" alt="image" src="https://github.com/user-attachments/assets/b97aba70-9927-47ed-b76f-7159e36c010b" />

📌 Requirements
Flask
scikit-learn
pandas
numpy


Install with:

pip install Flask scikit-learn pandas numpy
