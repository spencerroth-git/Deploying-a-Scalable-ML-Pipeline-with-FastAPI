# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a supervised learning classification model that is trained to predict whether an individual's annual income exceeds $50,000 based on demographic and employment related features.

## Intended Use
The intended use of this model is for educational and exploratory purposes.

## Training Data
This model was trained using the US Census Income dataset, which contains the demographic and employment information necessary to train the model.

## Evaluation Data
This model was trained by separating a test dataset from the original dataset using a method known as a train-test split. Performance metrics were then gathered on the test dataset to determine how well the model operates independent of the entirety of the rest of the data.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
There were three metrics used to assess model performance:
-Precision
-Recall
-F1 Score

Below are the results of the test dataset according to those metrics:
Precision: .7485
Recall: .6484
F1 Score: .6949
## Ethical Considerations
The data from the Census Income dataset may inadvertently introduce bias into the model. With this in mind, evaluation should be done to evaluate the presence of any bias, and mitigate those factors if found.

## Caveats and Recommendations
One potential improvement would be using hyperparamter tuning and comparing additional models to the metrics found by using our selected model (RandomForestClassifier).
