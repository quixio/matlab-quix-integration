# Starter transformation

[This code sample](...) demonstrates how to generate a wheel out of a simulink model and then run it from quix consuming and producing input and output data to kafka topics.

## How to build the wheel

### 01 - Modify Your Simulink Model
- Create one **Inport** block per input signal. The port numbers define the input order.
- Add **Outport** blocks for the signals you want to output.
- Configure **Data Import/Export** settings:
  - **Load from workspace**: all options **unchecked**
  - **Save to workspace or file**:
    - ✅ Output → saved as `yout`
    - ✅ Data stores → saved as `dsmout`
    - ✅ Single simulation output → saved as `out`
- Save the model after applying these settings.

### 02 - Copy Auxiliary Files
- Copy all files from the `aux-files` folder into the same directory as your Simulink model.
- Open MATLAB from that directory.

### 03 - Wrap the Simulink Model
- Open `simulink_wrapper.m` and set the `mdl` variable (first line) to your Simulink model's name.
- At the matlab console, create an `inputMatrix`, e.g. `[0, x1, x2, ..., xn]`, where `x1` is the value for Inport 1, and so on.  
  Example: `inputMatrix = [0, 1, 1, pi/2]`
- Run `simulink_wrapper(inputMatrix)` to compile the model for the first time. Make sure the output order and format are as expected.

### 04 - Compile for Quix
Now that the Simulink model is wrapped inside a MATLAB function, you can compile it using the Quix compiler.
Run the `quix_compiler.m` replacing the arguments if needed:
quix_compiler('simulink_wrapper', 'py')
This will generate a folder (py) containing the Python-compatible code.
If you used MATLAB Online, download and unzip the compiled folder (py.zip) to your local machine.
Once the compilation is complete, you can close MATLAB.

### 05 - Build the wheel
From your terminal, navigate to the (py) folder and run:
./build_wheel.sh
This script will create a .whl file. This file is the package you’ll deploy to Quix.

### 06 - Update the .whl in the quix app
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