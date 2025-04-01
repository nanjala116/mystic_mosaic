# Mystic Mosaic: Data Science Test Case

This repository contains a comprehensive take-home assignment designed to assess proficiency in data engineering, machine learning, model deployment, MLOps, computer vision, and natural language processing. The project is built with a strong focus on an object-oriented programming (OOP) approach, ensuring modular, reusable, and well-structured code across all tasks.

## Project Approach

- **Object-Oriented Design:**  
  Each major task (data cleaning, model training, deployment, image classification, etc.) is encapsulated in its own class. This OOP approach promotes code reusability, easier maintenance, and improved readability. For example, the `ImageClassifier` class handles the entire pipeline for computer vision tasks, from data loading and preprocessing to building, training, fine-tuning, and saving the model.

- **Modularity:**  
  The project separates concerns into different folders and files:

  - **Notebooks** are used for exploratory data analysis, model development, and prototyping.
  - **Scripts** contain production-ready code for API deployment, Named Entity Recognition (NER), and other automation tasks.
  - **Models** folder stores serialized model artifacts.

- **Cloud and CI/CD Integration:**  
  Our approach also leverages GitHub Actions and Azure (or alternative cloud platforms) for automated deployment, ensuring a robust MLOps pipeline for continuous integration, model retraining, and monitoring.

- **Best Practices:**  
  The repository includes Dockerfiles for containerized deployments (both for API and Streamlit applications), a detailed MLOps strategy document (`MLOps_Strategy.md`), and version-pinned dependencies for reproducibility.

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
  - **Deliverables:** `notebooks/data_cleaning.ipynb`, `data/cleaned_data.csv`.

- **SQL Query Optimization**:
  - Optimized queries to retrieve top customers and detect potential fraud.
  - **Deliverable:** `scripts/sql_queries.sql`.

### 2. Machine Learning & Model Development

- **Predictive Model Development**:

  - Performed exploratory data analysis (EDA).
  - Developed and evaluated classification models using Logistic Regression, Random Forest, and XGBoost.
  - **Deliverables:** `notebooks/loan_prediction_model.ipynb`, `models/loan_model.pkl`.

- **Model Deployment**:
  - Created an API to serve the trained model using FastAPI.
  - **Deliverables:** `scripts/loan_api.py`, Deployed Link (if available).

### 3. MLOps & DevOps

- **CI/CD & Model Monitoring**:
  - Developed a strategy for automating model training and retraining using MLflow.
  - Containerized the application using Docker and deployed on Kubernetes/Azure.
  - **Deliverable:** `MLOps_Strategy.md`.

### 4. Computer Vision & NLP

- **Image Classification**:

  - Trained a CNN-based classifier using transfer learning (EfficientNetB0) with fine-tuning to achieve at least 90% accuracy.
  - **Deliverables:** `notebooks/image_classification.ipynb`, `models/cnn_model.h5`.

- **Named Entity Recognition (NLP)**:
  - Developed an NER model using SpaCy/Hugging Face Transformers to extract Person, Organization, and Location entities.
  - **Deliverable:** `scripts/ner_extraction.py`.

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
   - Optionally, use Pipenv or Poetry to manage dependencies and enforce Python 3.11.8.

4. **Run Notebooks and Scripts**:
   - Explore the Jupyter Notebooks in the `notebooks/` directory for data processing and model development.
   - Run API and NER scripts from the `scripts/` directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

We appreciate your interest in this project. For questions, suggestions, or contributions, please open an issue or submit a pull request.
