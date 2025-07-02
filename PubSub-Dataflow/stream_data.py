#'''
#CLI command to run this pipeline on dataflow

#python stream_data.py \
#  --input_topic=projects/sesion04-461702/topics/pubsub_dataflow_demo \
#  --output_path=gs://beam_dataflow_cl/results/
#'''

import argparse
import apache_beam as beam
import logging
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam import window
from datetime import datetime as dt
from apache_beam.transforms.window import FixedWindows
from apache_beam.io import fileio
import json

class AddWindowdtlsFn(beam.DoFn):
    def process(self, element, window=beam.DoFn.WindowParam):
        start = window.start.to_utc_datetime().strftime('%Y-%m-%d %H:%M:%S')
        end = window.end.to_utc_datetime().strftime('%Y-%m-%d %H:%M:%S')
        yield f'{start} - {end} : {element} eventos'

def run(input_topic, output_path, pipeline_args=None):
    # Set `save_main_session` to True so DoFns can access globally imported modules.
    pipeline_options = PipelineOptions(
        pipeline_args, 
        streaming=True, 
        save_main_session=True, 
        runner='DataflowRunner',#'DirectRunner', 
        project='sesion04-461702', 
        region='us-central1', 
        temp_location='gs://beam_dataflow_cl/temp'
    )
    with beam.Pipeline(options=pipeline_options) as p:
    #p = beam.Pipeline(options=options)
        (
         p | "Read Events stream data from Topic" >> beam.io.ReadFromPubSub(topic=input_topic)
           | "Covert from Bytes to String" >> beam.Map(lambda s: s.decode("utf-8")) 
           | 'Events Data' >> beam.Map(lambda x: {'event_nbr':x.split(',')[0],'event_time':dt.strptime(x.split(',')[1],'%Y-%m-%d %H:%M:%S.%f')})
           | 'Events with Timestamps' >> beam.Map(lambda events: beam.window.TimestampedValue(events['event_nbr'], events['event_time'].timestamp()))  
           | 'Events fixed Window' >> beam.WindowInto(window.FixedWindows(5))         
           #| 'No of events per Window' >> beam.combiners.Count.Globally().without_defaults()
           | "Add dummy key" >> beam.Map(lambda x: ('event_key', 1))  # clave común
           | "Count per key" >> beam.CombinePerKey(sum)
           | "Remove key" >> beam.Map(lambda kv: kv[1])
           | 'Final results with Window Info' >> beam.ParDo(AddWindowdtlsFn())
           | 'String To BigQuery Row' >> beam.Map(lambda s: {'window_count': s})
           | "Convert to JSON string" >> beam.Map(lambda x: json.dumps(x))
           | "Write to files" >> fileio.WriteToFiles(
                    path='gs://beam_dataflow_cl/results/windowed/',
                    shards=1,
                    sink=lambda dest: fileio.TextSink(),
                    file_naming=fileio.destination_prefix_naming()
              )
           #| 'Write to PubSub' >> beam.io.WriteToPubSub(topic=topic_sink)
           #| 'Write to BigQuery' >> beam.io.Write(beam.io.WriteToBigQuery( 
           #                                                                         '<your table>',
           #                                                                          dataset='<your dataset>',
           #                                                                          project='<your project>',
           #                                                                          schema ='window_count:STRING',
           #                                                                          create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
           #                                                                          write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
           #                                                                     )
           #                                                                     )
           #| beam.Map(print)

        ) 

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_topic", required=False, help="Pub/Sub topic")
    parser.add_argument("--output_path", required=False, help="Output GCS path")
    known_args, pipeline_args = parser.parse_known_args()
    run(known_args.input_topic, known_args.output_path, pipeline_args)