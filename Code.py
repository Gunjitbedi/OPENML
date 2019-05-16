import sys

from google.cloud import automl_v1beta1 as automl
from google.cloud.automl_v1beta1.proto import service_pb2
from google.oauth2 import service_account

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My First Project-ccf4469590bb.json"

def get_prediction(content, project_id, model_id):
  compute_region = 'us-central1'
  automl_client = automl.AutoMlClient()
  prediction_client = automl.PredictionServiceClient()
  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  model_full_id = automl_client.model_path(project_id,compute_region ,model_id)
  payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':
  content = sys.argv[1]
  project_id = sys.argv[2]
  model_id = sys.argv[3]

  print (get_prediction(content, project_id,  model_id))

