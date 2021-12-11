# Dask-vs-Spark-NLP

Hi! And welcome to my repo where I'm comparing Dask and Spark in Natural Language Processing (NLP) pre-processing steps.

All of the information about this study can be found in [this google doc](https://docs.google.com/document/d/1YC-sEKb8ok6_ry22dsPY3j7wVkiWdCVaMrYmqy_SDNo/edit?usp=sharing)

## Navigating this repo
The main pieces of code to run (if you wanted to see the results for yourself) are found in `code/`.

The 369_project_MASTER.ipynb is a notebook file containing pipelines for all of the frameworks in one file. **I don't recommend running this** because it's a bit messy so I split it up into 3 different files with a python file `shared.py` that has common functions among them.

Those three files are `pandas_pipeline.ipynb`, `dask_pipeline.ipynb`, and `spark_pipeline.ipynb`.

You can run these individually and they should work out of the box, so long as you fix the path to your data files.