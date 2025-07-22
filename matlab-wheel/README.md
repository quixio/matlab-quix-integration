# Starter transformation

[This code sample](...) demonstrates how to generate a wheel out of a matlab function and then run it from quix consuming and producing input and output data to kafka topics.

## How to build the wheel

### 01 - Your matlab function
Ensure you understand the type and number of inputs and outputs from your functino.

### 02 - Copy Auxiliary Files
- Copy all files from the `aux-files` folder into the same directory as your Matlab function.
- Open MATLAB from that directory.

### 03 - Compile for Quix
Let's compile the MATLAB function using the Quix compiler. Just run the `quix_compiler.m` replacing the arguments:
quix_compiler('function_name', 'py')
This will generate a folder (py) containing the Python-compatible code.
If you used MATLAB Online, download and unzip the compiled folder (py.zip) to your local machine.
Once the compilation is complete, you can close MATLAB.

### 04 - Build the wheel
From your terminal, navigate to the local (py) folder and run:
./build_wheel.sh
This script will create a .whl file. This file is the package you’ll deploy to Quix.

### 05 - Update the .whl in the quix app
Replace the existing .whl file in your Quix app with the new one you just built.
⚠️ If the new filename differs from the previous one, make sure to update the requirements.txt file accordingly.


## How to run

Create a [Quix](https://portal.platform.quix.io/signup?xlink=github) account or log-in and visit the Samples to use this project.

Clicking `Edit code` on the Sample, forks the project to your own Git repo so you can customize it before deploying.


## Environment variables

The code sample uses the following environment variables:

- **input**: Name of the input topic to listen to.
- **output**: Name of the output topic to write to.

## Contribute

Submit forked projects to the Quix [GitHub](https://github.com/quixio/quix-samples) repo. Any new project that we accept will be attributed to you and you'll receive $200 in Quix credit.

## Open source

This project is open source under the Apache 2.0 license and available in our [GitHub](https://github.com/quixio/quix-samples) repo.

Please star us and mention us on social to show your appreciation.