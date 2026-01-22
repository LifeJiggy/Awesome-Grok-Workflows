---
version: "1.0.0"
created: "2024-01-01"
updated: "2024-01-01"
author: "Grok-Workflow-Builder-v1"
purpose: "Few-shot examples for ML/AI model development and deployment"
---

# ML Examples

## Example 1: Model Selection

**Problem**: Predict customer churn for a SaaS company

**Analysis (Example)**:
```markdown
## Model Selection for Churn Prediction 🎯

### Data Characteristics
- 50,000 customers with 50 features
- 15% churn rate (imbalanced)
- Mix of categorical and numerical
- Temporal component (subscription history)

### Candidate Models

| Model | Accuracy | F1-Score | Train Time | Interpretability | Recommendation |
|-------|----------|----------|------------|------------------|----------------|
| Logistic Regression | 82% | 0.71 | 2s | High | ✅ Baseline |
| Random Forest | 89% | 0.81 | 15s | Medium | ✅ Good |
| XGBoost | 91% | 0.85 | 45s | Low | ✅ Best |
| Neural Network | 90% | 0.83 | 2min | Very Low | ⚠️ Overkill |
| Gradient Boosting | 90% | 0.84 | 30s | Low | ✅ Alternative |

### Recommended Approach

**Phase 1: Baseline**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

model = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])),
    ('classifier', LogisticRegression(class_weight='balanced'))
])
```

**Phase 2: XGBoost**
```python
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    scale_pos_weight=(1/churn_rate - 1),  # Handle imbalance
    eval_metric='logloss'
)
```

### Evaluation Strategy
- Time-based split (train on past, predict future)
- Stratified K-fold cross-validation
- Focus on F1-score for minority class
- AUC-ROC for threshold selection
```

## Example 2: Data Leakage Detection

**Problem**: Model shows 99% accuracy - suspicious!

**Analysis (Example)**:
```markdown
## Data Leakage Investigation 🔍

### Suspicious Signs
- 99% accuracy with only 15% positive class
- Training time very short
- Perfect predictions on validation set

### Common Leakage Sources

| Source | Detection | Fix |
|--------|-----------|-----|
| Leak in features | Check feature importance | Remove leaky features |
| Time contamination | Check train/test overlap | Proper temporal split |
| Duplicate rows | Check for duplicates | Remove duplicates |
| Target leakage | Check feature leakage | Remove leaky columns |
| Preprocessing on full data | Check scaler fit | Use only training data |

### Investigation Code
```python
# 1. Check for data leakage features
from sklearn.feature_selection import mutual_info_classif

X = data.drop('churn', axis=1)
y = data['churn']

# High mutual information might indicate leakage
scores = mutual_info_classif(X, y)
leaky_features = [f for f, s in zip(X.columns, scores) if s > 0.9]

# 2. Check target leakage
for col in X.columns:
    if 'churn' in col.lower() or 'cancel' in col.lower():
        print(f"Potential leakage: {col}")
```

### Example Leak Found
```python
# Leaky feature - calculated AFTER churn!
data['days_since_last_payment'] = (churn_date - payment_date).days

# Fix: Use only features available at prediction time
data['days_since_last_payment'] = (prediction_date - last_payment_date).days
```

### Prevention Strategy
1. Use Pipeline for preprocessing
2. Time-based splits only
3. Feature selection by domain expert
4. Cross-validation with time awareness
```

## Example 3: Model Deployment Checklist

**Problem**: Deploy ML model to production

**Checklist (Example)**:
```markdown
## Production Deployment Checklist ✅

### Model Readiness
- [ ] Model performance meets business requirements
- [ ] A/B test results show improvement
- [ ] Model card documented
- [ ] Model versioned and registered
- [ ] Drift detection baseline established

### Code Quality
- [ ] Code reviewed by 2+ engineers
- [ ] Unit tests for preprocessing (90% coverage)
- [ ] Integration tests for pipeline
- [ ] No hardcoded paths or credentials
- [ ] Type hints throughout

### Monitoring Setup
- [ ] Prediction latency tracking
- [ ] Error rate monitoring
- [ ] Data drift detection
- [ ] Model performance monitoring
- [ ] Feature distribution alerts

### Scaling & Reliability
- [ ] Load tested for peak traffic
- [ ] Fallback strategy documented
- [ ] Rate limiting configured
- [ ] Circuit breaker implemented
- [ ] Horizontal scaling tested

### Security
- [ ] Input validation implemented
- [ ] Output sanitization
- [ ] PII redaction
- [ ] API authentication
- [ ] Audit logging

### Rollback Plan
- [ ] Previous model version archived
- [ ] Rollback script tested
- [ ] Traffic switch mechanism ready
- [ ] Rollback criteria defined
- [ ] Stakeholder notification plan

### Documentation
- [ ] API documentation complete
- [ ] Example requests/responses
- [ ] Error code documentation
- [ ] SLA documented
- [ ] On-call runbook created
```

---

# Template for ML Projects

## Structure
```
1. Problem Definition
2. Data Exploration
3. Feature Engineering
4. Model Selection
5. Training & Evaluation
6. Deployment Checklist
7. Monitoring Plan
8. Limitations & Future Work
```

## Metrics by Problem Type

| Problem Type | Primary Metric | Secondary Metrics |
|--------------|----------------|-------------------|
| Classification | F1-Score | Accuracy, AUC-ROC |
| Regression | RMSE | MAE, R² |
| Ranking | NDCG | MRR, Precision@K |
| Clustering | Silhouette | Calinski-Harabasz |
| Anomaly Detection | F1-Score | Precision, Recall |
