# MATLAB 2025a

This code sample demonstrates how to run MATLAB 2025a functions in Quix using a MATLAB Engine instance.

## How to run your MATLAB function

- Save your `.m` function file in the `/MATLAB` directory of this template (like the rot.m examples).
- Update line 48 of the Dockerfile with your license server.
- Edit the `matlab_processing` function in `main.py` to accommodate your specific function's input and output variables.

## Environment variables
 - `input`: Kafka topic to receive input data from.
 - `output`: Kafka topic to write the results of the transformation.

## Contribute

Submit forked projects to the Quix [GitHub](https://github.com/quixio/quix-samples) repo. Any new project that we accept will be attributed to you and you'll receive $200 in Quix credit.

## Open source

This project is open source under the Apache 2.0 license and available in our [GitHub](https://github.com/quixio/quix-samples) repo.

Please star us and mention us on social to show your appreciation.