# Used Cars Price Prediction Application

## Objective
The goal of this project is to:
1. Build a machine learning regression model to predict the selling price of used cars based on various input features like fuel type, kilometers driven, and transmission type.
2. Deploy the trained machine learning model using the Flask framework.

## Dataset
- **Source:** [Kaggle](https://www.kaggle.com/)
- **Description:** The dataset contains information about used cars, including attributes such as fuel type, transmission type, kilometers driven, and selling price.

## Technologies Used
- **Programming Language:** Python
- **Machine Learning Libraries:**
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `scipy`
- **Visualization Tools:**
  - `matplotlib`
  - `seaborn`
- **Framework for Deployment:** Flask
- **Other Tools:**
  - `pickle` for model persistence

## Project Workflow
1. **Data Loading:**
   - Loaded the dataset (`car_data.csv`) using pandas.

2. **Exploratory Data Analysis (EDA):**
   - Visualized and analyzed data distributions using `seaborn` and `matplotlib`.
   - Handled missing values and removed outliers using statistical techniques (e.g., z-score).

3. **Data Preprocessing:**
   - Encoded categorical variables using `LabelEncoder`.
   - Split the data into training and testing sets using `train_test_split`.

4. **Model Building:**
   - Implemented a regression model using `RandomForestRegressor`.
   - Evaluated model performance using metrics such as `R^2` score.

5. **Model Deployment:**
   - Saved the trained model using `pickle`.
   - Created a Flask web application for prediction.

## How to Run the Project

### Prerequisites
1. Install Python (>= 3.8).
2. Install required Python libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

### Steps to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Ensure the dataset (`car_data.csv`) is in the project directory.
3. Train the model (if necessary):
   ```bash
   python train_model.py
   ```
4. Start the Flask application:
   ```bash
   python app.py
   ```
5. Access the web application in your browser at `http://127.0.0.1:5000`.

## Directory Structure
```
├── car_data.csv             # Dataset
├── app.py                   # Flask application script
├── model.pkl                # Saved ML model
├── templates/               # HTML templates for Flask
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
```

## Results
- Achieved a strong `R^2` score, indicating the model's effectiveness in predicting car prices.
- Successfully deployed the model using Flask, making it accessible via a web interface.

## Future Improvements
- Enhance the model by experimenting with different algorithms or hyperparameter tuning.
- Add more features to the dataset for better predictions.
- Improve the Flask application's user interface.

## Acknowledgments
- Dataset sourced from Kaggle.
- Developed using open-source Python libraries.
