# Mystic Mosaic: Data Science Test Case

This repository contains a comprehensive take-home assignment designed to assess proficiency in data engineering, machine learning, model deployment, MLOps, computer vision, and natural language processing.

## Repository Structure

- `data/`: Contains datasets used for various tasks.
- `notebooks/`: Jupyter Notebooks for data cleaning, exploratory data analysis (EDA), and model development.
- `models/`: Serialized trained models for different tasks.
- `scripts/`: Python scripts for API development and Named Entity Recognition (NER).
- `MLOps_Strategy.md`: Document detailing strategies for CI/CD, model monitoring, and automation.
- `Dockerfile.api`: Dockerfile for deploying the loan prediction API.
- `Dockerfile.streamlit`: Dockerfile for deploying the Streamlit application.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `LICENSE`: MIT License for the project.
- `Procfile`: Configuration for deploying the application on platforms like Heroku.
- `README.md`: This file, providing an overview of the repository.

## Sections and Deliverables

### 1. Data Engineering & SQL

- **Data Cleaning & Transformation**:
  - Handled missing values.
  - Encoded categorical variables.
  - Normalized numerical features.
  - Deliverables: `notebooks/data_cleaning.ipynb`, `data/cleaned_data.csv`.

- **SQL Query Optimization**:
  - Optimized queries to retrieve top customers and detect potential fraud.
  - Deliverable: `scripts/sql_queries.sql`.

### 2. Machine Learning & Model Development

- **Predictive Model Development**:
  - Performed EDA.
  - Developed and evaluated classification models.
  - Deliverables: `notebooks/loan_prediction_model.ipynb`, `models/loan_model.pkl`.

- **Model Deployment**:
  - Created an API to serve the trained model.
  - Deliverables: `scripts/loan_api.py`, Deployed Link (if available).

### 3. MLOps & DevOps

- **CI/CD & Model Monitoring**:
  - Outlined strategies for automation and deployment.
  - Deliverable: `MLOps_Strategy.md`.

### 4. Computer Vision & NLP

- **Image Classification**:
  - Trained a CNN-based classifier using transfer learning.
  - Deliverables: `notebooks/image_classification.ipynb`, `models/cnn_model.h5`.

- **Named Entity Recognition (NLP)**:
  - Developed an NER model to extract entities.
  - Deliverable: `scripts/ner_extraction.py`.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nanjala116/mystic_mosaic.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd mystic_mosaic
   ```

3. **Set Up the Environment**:
   - Ensure Python 3.11.8 is installed.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run Notebooks and Scripts**:
   - Navigate to the `notebooks/` directory to explore Jupyter Notebooks.
   - Use scripts in the `scripts/` directory for API and NER tasks.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
