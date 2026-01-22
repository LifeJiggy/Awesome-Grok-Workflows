# AI/ML Development Rules

## General Safety

### 1. Data Privacy
- **Never use personal data without consent**
- Anonymize training data
- Remove PII from datasets
- Comply with GDPR, CCPA, etc.

### 2. Bias and Fairness
- **Test for bias across protected groups**
- Use diverse training data
- Monitor for disparate impact
- Document known biases

### 3. Model Safety
- **Never deploy without testing**
- Red teaming for adversarial attacks
- Input validation and sanitization
- Output filtering for harmful content

## Model Development

### Training Data
```python
# ✅ Good: Diverse, balanced dataset
train_data = BalancedDataset(
    source=production_data,
    balance_strategy="oversample_minority",
    protected_attributes=["race", "gender"],
    min_representation=0.1
)

# ❌ Bad: Biased dataset
train_data = Dataset(source=web_scraped, no_balance=True)
```

### Model Evaluation
| Metric | Description | Minimum |
|--------|-------------|---------|
| Accuracy | Overall correctness | 0.85 |
| F1-Score | Harmonic mean of precision/recall | 0.80 |
| AUC-ROC | Discrimination ability | 0.90 |
| Fairness | Equal opportunity across groups | 0.95 |

### Testing Requirements
1. Unit tests for all components
2. Integration tests for pipeline
3. Adversarial robustness tests
4. Bias testing across demographics
5. Edge case coverage

## Deployment Rules

### Model Serving
- **Version all models**
- A/B testing for new models
- Rate limiting on predictions
- Monitoring for drift
- Rollback capability

### Safety Checks
```python
prediction = model.predict(input_data)

# Validate output
if not is_valid_prediction(prediction):
    raise InvalidPredictionError("Prediction out of bounds")

# Rate limiting
if request_count > RATE_LIMIT:
    raise RateLimitExceeded()
```

### Monitoring
- Prediction latency
- Error rates by input type
- Demographic performance gaps
- Data drift detection
- Model staleness

## Documentation Requirements

### Model Cards
```yaml
model_card:
  name: "sentiment-classifier-v1"
  version: "1.0.0"
  task: "sentiment_analysis"
  training_data: "Social media posts, balanced 50/50 sentiment"
  performance:
    accuracy: 0.92
    f1_positive: 0.91
    f1_negative: 0.93
  limitations: "May misclassrate sarcasm"
  known_biases: "Slight bias toward formal language"
  use_cases: "Brand monitoring, not critical decisions"
```

### Known Limitations
- Document failure modes
- Provide confidence intervals
- List edge cases
- Define out-of-distribution detection

## Ethical AI Principles

### Transparency
- Disclose AI-generated content
- Explain model decisions when possible
- Provide model provenance
- Document training data sources

### Accountability
- Human oversight for critical decisions
- Clear escalation paths
- Incident response plan
- Regular audits

### Privacy
- Data minimization
- Secure storage
- Deletion on request
- Audit trails

### Fairness
- Test across demographic groups
- Fix disparate impacts
- Use fairness metrics
- Engage diverse stakeholders
