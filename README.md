# Survival Prediction Repository

Welcome to the **Survival Prediction Repository**! This project leverages machine learning to predict whether a person is likely to survive in a specific scenario based on various input factors. Below, you'll find an overview of the repository's contents and instructions for usage.

## Repository Contents

### 1. Notebook: `1.ipynb`
This Jupyter Notebook contains the following:
- **Data Preprocessing**: Steps to clean and prepare the data for analysis.
- **Feature Engineering**: Encoding categorical variables and feature scaling.
- **Model Training**: Building and evaluating the machine learning model.
- **Model Saving**: Exporting the trained model for deployment.

### 2. Streamlit App: `app_streamlit.py`
This Python script serves as the front-end interface for the survival prediction model. Users can input data and view predictions in real time using a simple web app built with Streamlit.

### 3. Model File: `Survival_model.pkl`
This file contains the pre-trained survival prediction model. It is used by the Streamlit app to make predictions based on user inputs.

#### Key Features of the App:
- **User Inputs**:
  - Age
  - Gender
  - Socio-economic Status (Class)
  - Fare
  - Embark Town
- **Prediction Output**:
  - Displays whether the person is predicted to be "Saved" or "Not Saved."

## How to Use

### Prerequisites
Make sure you have the following installed:
- Python 3.8+
- Jupyter Notebook
- Streamlit
- Required libraries: `joblib`, `numpy`, `pandas`, `sklearn`

### Running the Notebook
1. Clone this repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook 1.ipynb
   ```
3. Execute the cells sequentially to train the model or analyze the process.

### Running the Streamlit App
1. Ensure the pre-trained model file (`Survival_model.pkl`) is in the same directory as `app_streamlit.py`.
2. Run the Streamlit app:
   ```bash
   streamlit run app_streamlit.py
   ```
3. Open the link provided in the terminal to access the app in your web browser.

## Example Workflow
1. Use the pre-trained model (`Survival_model.pkl`) directly or train a new model using the notebook.
2. Launch the Streamlit app to interact with the trained model.
3. Input the required features (e.g., Age, Gender, Fare) and click "Predict" to see the results.

## File Structure
```
.
├── 1.ipynb               # Jupyter Notebook for data processing and model training
├── app_streamlit.py      # Streamlit app for model deployment
├── Survival_model.pkl    # Pre-trained model
├── README.md             # Project documentation
```

## Contributions
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact Information
For further inquiries or collaboration, feel free to reach out:

**Muhammad Taha**  
- Email: [contact.taha2005@gmail.com](mailto:contact.taha2005@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/muhammad-taha-b88807248/)  
- [X (formerly Twitter)](https://x.com/M_Taha093589350)  
