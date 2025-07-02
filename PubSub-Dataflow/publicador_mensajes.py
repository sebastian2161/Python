from google.cloud import pubsub_v1
import time
import datetime as dt

#get project details
project_id="sesion04-461702"
topic_id="pubsub_dataflow_demo"

#Publisher Client
publisher= pubsub_v1.PublisherClient()
topic_path= publisher.topic_path(project_id, topic_id)

for event_nbr in range(1,10):
    data_str= '{}.{}'.format(event_nbr,dt.datetime.now())
    #Data must be a bytestring
    data = data_str.encode("utf-8")
    time.sleep(1)
    #Add two atributes, origin and username to the message
    future = publisher.publish(topic_path, data, origin="python-sample", username="gcp")
    #print(future.result())
    print(data)

print(f"Published messages with custom attributes to {topic_path}.")
