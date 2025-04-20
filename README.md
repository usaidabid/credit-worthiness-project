# credit-worthiness-project

Dataset Preprocessing Steps:

The dataset was first cleaned by handling missing values using median imputation. To tackle class imbalance, I used the SMOTE (Synthetic Minority Over-sampling Technique) method. This ensured that both reliable and unreliable borrower classes were represented equally during training, improving the model's ability to generalize.

Model Selection and Rationale

I selected XGBoost for model training because it is highly efficient, handles missing values internally, and performs well on structured/tabular data. XGBoost also provides robust handling of class imbalance and overfitting, making it ideal for credit risk prediction tasks.

Challenges Faced and Solutions

One of the main challenges was the class imbalance in the dataset, which was solved using SMOTE. Another issue was ensuring the correct mapping of input features for prediction, which I handled by matching input fields with training data columns carefully. Deployment also posed a challenge due to file path errors, which were fixed by correctly uploading the model file and referencing it properly in the Streamlit app.
