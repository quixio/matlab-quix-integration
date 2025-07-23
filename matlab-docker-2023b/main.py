from quixstreams import Application
import math
import os

"""
import matlab.engine

print("Starting matlab")

eng = matlab.engine.start_matlab()

print("Calculate square root")
output = eng.sqrt(8.0)

print("Result:")
print (output)
"""

import matlab.engine
print("Starting matlab")
eng = matlab.engine.start_matlab()

# Define matlab function call
def matlab_processing(row: dict):
    print("Calculate square root")
    # Define the input vector and angle
    x = row["x"]
    y = row["y"]
    v = matlab.double([[x], [y]])  # column vector
    theta = math.pi / 4  # 45 degrees in radians
    print("Calling rot()...")
    output = eng.MATLAB.rot(v, theta)
    print("Result:")
    print(output)
    

def main():
    # Setup necessary objects
    app = Application(
        consumer_group="my_transformation",
        auto_create_topics=True,
        auto_offset_reset="earliest"
    )
    input_topic = app.topic(name=os.environ["input"])
    output_topic = app.topic(name=os.environ["output"])
    sdf = app.dataframe(topic=input_topic)
    

    # Do StreamingDataFrame operations/transformations here
    sdf.print_table()
    sdf = sdf.update(matlab_processing)
    sdf.print_table()

    # Finish off by writing to the final result to the output topic
    sdf.to_topic(output_topic)

    # With our pipeline defined, now run the Application
    app.run()


# It is recommended to execute Applications under a conditional main
if __name__ == "__main__":
    main()