function quix_compiler(function_name, destination_folder)
    % compileAndPackage Compiles a MATLAB function, copies a shell script, and zips the output.
    % Inputs:
    %   function_name - Name of the MATLAB function file (e.g., 'myfunc')
    %   destination_location_name - Destination folder for the compiled output (e.g., 'build_output')

    % Define subfolder for mcc output
    out_folder = fullfile(destination_folder, 'out');

    % Step 0: Create folders if they don’t exist
    if ~exist(out_folder, 'dir')
        mkdir(out_folder);
    end

    % Step 1: Compile using mcc into destination_folder/out
    try
        fprintf('Compiling %s.m into %s...\n', function_name, out_folder);
        mcc('-W', ['python:quixmatlab,' function_name], ...
            '-d', out_folder, ...
            [function_name, '.m']);
    catch ME
        error('Compilation failed: %s', ME.message);
    end

    % Step 2: Copy build_wheel.sh to destination_folder
    script_name = 'build_wheel.sh';
    if exist(script_name, 'file') == 2
        try
            copyfile(script_name, destination_folder);
            fprintf('Copied %s to %s.\n', script_name, destination_folder);
        catch ME
            error('Failed to copy script: %s', ME.message);
        end
    else
        warning('%s not found in current directory.\n', script_name);
    end

    % Step 3: Zip destination_folder
    zip_name = [destination_folder, '.zip'];
    try
        zip(zip_name, destination_folder);
        fprintf('Created zip file: %s\n', zip_name);
    catch ME
        error('Failed to create zip: %s', ME.message);
    end

    fprintf('All tasks completed successfully.\n');
end