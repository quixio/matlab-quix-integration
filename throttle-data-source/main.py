# import the Quix Streams modules for interacting with Kafka.
# For general info, see https://quix.io/docs/quix-streams/introduction.html
# For sources, see https://quix.io/docs/quix-streams/connectors/sources/index.html
from quixstreams import Application
from quixstreams.sources import Source
import time
import os
import random, math

# for local dev, you can load env vars from a .env file
# from dotenv import load_dotenv
# load_dotenv()

class VectorGenerator(Source):

    def run(self):
        while self.running:
            event = {"throttle_angle": random.uniform(8, 12)}
            event_serialized = self.serialize(key="source-simulink", value=event)
            self.produce(key=event_serialized.key, value=event_serialized.value)
            time.sleep(float(os.environ["ms_to_sleep"])/1000)


def main():
    # Setup necessary objects
    app = Application(consumer_group="data_producer", auto_create_topics=True)
    memory_usage_source = VectorGenerator(name="vector-producer")
    output_topic = app.topic(name=os.environ["output"])

    # --- Setup Source ---
    app.add_source(source=memory_usage_source, topic=output_topic)

    # With our pipeline defined, now run the Application
    app.run()


#  Sources require execution under a conditional main
if __name__ == "__main__":
    main()
