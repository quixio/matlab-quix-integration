# Starter transformation

[This code sample](https://github.com/quixio/quix-samples/tree/main/python/transformations/starter_transformation) demonstrates how to consume and transform data from a Kafka topic
and publish these results to another Kafka topic, all using our `StreamingDataFrame`.

This boilerplate will run in Quix Cloud but largely has placeholder operations, so you 
will need to add your own to do something besides printing the data to console!

## How to run

Create a [Quix](https://portal.platform.quix.io/signup?xlink=github) account or log-in and visit the Samples to use this project.

Clicking `Edit code` on the Sample, forks the project to your own Git repo so you can customize it before deploying.

## Environment variables

The code sample uses the following environment variables:

- **input**: Name of the input topic to listen to.
- **output**: Name of the output topic to write to.

## Possible `StreamingDataFrame` Operations

Many different operations and transformations are available, so 
be sure to [explore what's possible](https://quix.io/docs/quix-streams/processing.html)!


## Contribute

Submit forked projects to the Quix [GitHub](https://github.com/quixio/quix-samples) repo. Any new project that we accept will be attributed to you and you'll receive $200 in Quix credit.

## Open source

This project is open source under the Apache 2.0 license and available in our [GitHub](https://github.com/quixio/quix-samples) repo.

Please star us and mention us on social to show your appreciation.

# MATLAB

Use this template to deploy transformations that use MATLAB and Simulink. 

## Requirements

To create Python packages from MATLAB functions you need the following MathWorks products
 - MATLAB
 - MATLAB Compiler
 - MATLAB Compiler SDK 

To create Python packages from Simulink products, in addition to the above list, you also need
 - Simulink
 - Simulink Compiler

## Environment variables
 - `input`: Kafka topic to receive input data from.
 - `output`: Kafka topic to write the results of the transformation.

## Preparing Python packages from MATLAB and Simulink

`MATLAB` directory in the project has pre-compiled packages from MATLAB and Simulink assets. So, you can simply deploy and run this project. However, if you'd like to create the Python package from the source files, you can find them in the `assets` directory of this project. You can compile them using the following command:

```
mcc -W python:quixmatlab engine.m rot.m -d ../MATLAB
```

You only need the package directory that contains the `__init__.py` and a `*.ctf` file, `pyproject.toml` and `setup.py` in the `MATLAB` directory in this template.

## Resources for MATLAB Compiler SDK and MATLAB Runtime APIs

 - [Call MATLAB functions from Python](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html?s_tid=CRUX_lftnav)
 - [MATLAB Arrays in Python](https://www.mathworks.com/help/matlab/matlab_external/matlab-arrays-as-python-variables.html)
 - [Pass data to MATLAB](https://www.mathworks.com/help/matlab/matlab_external/pass-data-to-matlab-from-python.html)
 - [MATLAB Compiler SDK reference](https://www.mathworks.com/help/compiler/mcc.html#d124e20858)
 - [Calling Simulink from Python](https://github.com/mathworks/Call-Simulink-from-Python)