import os
import sys

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My First Project-ccf4469590bb.json"

def predict(content, project_id, model_id):
    """Classify the content."""
    # [START automl_language_predict]
    # TODO(developer): Uncomment and set the following variables
    project_id = 'dogwood-baton-240611'
    compute_region = 'us-central1'
    model_id = 'TCN5526896291447140535'

    from google.cloud import automl_v1beta1 as automl

    automl_client = automl.AutoMlClient()

    # Create client for prediction service.
    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl_client.model_path(
        project_id, compute_region, model_id
    )

    # Set the payload by giving the content and type of the file.
    payload = {"text_snippet": {"content": content, "mime_type": "text/plain"}}

    # params is additional domain-specific parameters.
    # currently there is no additional parameters supported.
    params = {}
    response = prediction_client.predict(model_full_id, payload, params)
    print("Prediction results:")
    for result in response.payload:
        print("Predicted class name: {}".format(result.display_name))
        print("Predicted class score: {}".format(result.classification.score))

if __name__ == '__main__':
  content = sys.argv[1]
  project_id = sys.argv[2]
  model_id = sys.argv[3]

  predict(content, project_id,  model_id)
