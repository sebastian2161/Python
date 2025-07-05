python pb.py \
  --runner DataflowRunner \
  --project=sesion04-461702 \
  --region=us-central1 \
  --temp_location=gs://beam_dataflow_cl/temp \
  --template_location=gs://beam_dataflow_cl/templates/pipeline_template