# IC Model

## NEURON
Use the following link to get information and instructions about downloading NEURON: https://nrn.readthedocs.io/en/8.2.7/  
For the Mac, I had issues with the command line, so I used the pkg installer. But either one should work.  

Once this is done, download this repository and open it in an IDE. For this model, any Python IDE can be used. I used the Spyder IDE that is part of the Anaconda package.  

## Setting up .mod files
Using either your computer's terminal or your IDE's terminal, navigate to the folder with all the repository files. You can use type the command **pwd** to see which folder you're currently in, **cd ..** to go back to the previous folder and **cd <folder_name>** to go into the next folder. After you're in the folder, type the following command:
```
nrnivmodl
```
This should create a folder named after your computer architecture (like arm64 for mac) within your repository containing the compiled .c and .o files for each .mod file. For more help with this, look at the NEURON forum online

## Running the code
To run the model, you have to run the IC SAM Control file. You might be prompted to download more libraries, such as matplotlib.  

In the IC SAM Control file, the variable drvinputs represents the excitatory inputs and the variable drvIinputs represents the inhibitory inputs. In the current version of the file, there are two places where both of these are set (neglecting comments). The first place where the variables are assigned is the original code used for the model, which generates random inputs. The second place where they are set is the code used for generating the spike trains.  

The spike trains are made using functions in SpikeTrains.py. The main function to use is spike_trains_VS(), where the first parameter is the frequency, the second parameter is the spike rate, and the third parameter is the vector strength. The fourth and fifth parameters represent depth and syncrhonization (True/False), but they haven't been implemented yet, so you can put arbitrary inputs for them. If you want a vector strength <= 0.1, use spike_trains_VS_05(). This function uses more randomized spike times, while the function used for the other vector strengths chooses a time based on how far off the current vector strength is from the target.

To switch between the adapting and sustained models, use one of the two lines that intitialize the ICCell object right before the for loop definition.

Currently the IC Sam Control file saves a csv, but that code can be commented out. You can also print dot raster or PSTH plots using the commented out code located at the bottom of the file. They should work, but there might need to be a few adjustments of variables in the for loop. 


If you have any questions, please feel free to reach out to me at ashome@purdue.edu.



