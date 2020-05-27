# franc
franc aspect of masters thesis

clone this directory onto your chpc account

create a conda environment for python 2, the dependencies can be downloaded with the code below:

```shell
conda create --name py2 --file requirements.txt
```

Then, in the run_it.slurm file change the working directory to the your franc directory

Then, change the SCRDIR to have your uID instead of mine.

Download the folders inp_files and odb_files and put them in your scratch directory or /scratch/kingspeak/serial/YOURUID/franc/

Download standard_channel_L10_4.inp and place it in this directory.

To run the job type:
```shell
sbatch run_it.slurm
```

To check the status of your job:
```shell
squeue -u YOURUID
```

Regularly clean up your scratch directory on jobs that failed.

When a job fails and you need to just change parameters and continue the crack. change the SCRDIR in continue_it.slurm to the scratch directory that failed and change initial_crack in crack_growth.py to False.

Then change the previous_step to the last successful crack growth step and make sure that previous_step + steps = 10

This definitely won't be smooth when it fails because then you will need to only finish the model it failed on and start it new with initial_crack=True and previous_step=1

Something that might be useful is a way to keep track of the files that have already been successfully run.
