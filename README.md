# Algerian Forest Fire Prediction

### Project Overview
This is a Machine Learning web application that predicts the **Fire Weather Index (FWI)** for Algerian forests. The model is built using a Ridge Regression algorithm to help authorities predict fire risks based on environmental factors.

### Technical Stack
* **Language:** Python 3.8
* **Web Framework:** Flask
* **Machine Learning:** Scikit-Learn (Ridge Regression)
* **Data Handling:** Pandas, NumPy
* **Frontend:** HTML5 with Jinja2 templates

### Project Structure
* `application.py`: The main Flask entry point.
* `model/`: Contains the trained `ridge.pkl` and `scaler.pkl` files.
* `notebooks/`: Data cleaning and model training experiments.
* `templates/`: HTML files for the user interface.
* `requirements.txt`: List of required Python libraries.

### How to Run Locally
1. Clone the repository:
   `git clone https://github.com/rajan7838/Algerian-Forest-Fire-Prediction.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `python application.py`
