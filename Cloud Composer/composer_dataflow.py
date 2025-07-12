# Import required modules and methods
import argparse
import logging
import apache_beam as beam
import re
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.transforms.sql import SqlTransform
from apache_beam.options.pipeline_options import PipelineOptions
import json
import ast
#import ultimo_archivo as arch

# Setting up the Apache Beam pipeline options.
beam_options = PipelineOptions(
    save_main_session=True,
    #runner='DirectRunner',
    runner='DataflowRunner',
    project='sesion04-461702',
    temp_location='gs://beam_dataflow_cl/temp',
    region='us-central1',
    zone= 'us-central1-c',
    autoscaling_algorithm='NONE',  # Disable autoscaling
    num_workers=1,  # Use only 1 worker
    worker_machine_type='n1-standard-64',  # Small machine type
    )

def contar_palabras(element):
  return element

class WordExtractingDoFn(beam.DoFn):
  """Parse each line of input text into words."""
  def process(self, element):
    """Returns an iterator over the words of this element.

    The element is a line of text.  If the line is blank, note that, too.

    Args:
      element: the element being processed

    Returns:
      The processed element.
    """
    return re.findall(r'[\w\']+', element, re.UNICODE)

# Entry Function to run Pipeline
def run():
    # Set `save_main_session` to True so DoFns can access globally imported modules.
    #ultimo_archivo = arch.obtener_ultimo_archivo("beam_scc", prefix="input/")

    with beam.Pipeline(options=beam_options) as p:

        lines =( p 
                | 'Read' >> ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')
                #| 'print log1'>>beam.Map(print)
               )
                    
        counts = (
        lines
        | 'Split' >> (beam.ParDo(WordExtractingDoFn()).with_output_types(str))
        | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum)
        | 'write final results into GCS bucket' >> beam.io.WriteToText('gs://beam_dataflow_cl/results/composer_dataflow_results.txt')
        #| 'print log3'>>beam.Map(print)
        )
        
if __name__ == "__main__":
    #logging.getLogger().setLevel(logging.INFO)
    run()

