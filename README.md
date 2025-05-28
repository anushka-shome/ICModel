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
To run the model, you have to run the IC SAM Control file.  




