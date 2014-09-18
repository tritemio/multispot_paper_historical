"""
This modules defines two functions to be used inside an IPython Notebook
in order to execute other notebooks.

These functions uses [runipy](https://pypi.python.org/pypi/runipy/)
to run a a single notebook or a template notebook several times
(with different data files as input).

For the template notebooks the result of each execution (including data and
plots) are saved as a new notebooks. A parameter (`data_id`) is passed to the
notebook through an environment variable (`NB_DATA_FILE`). The notebook used
as template (for example [usALEX-5samples](usALEX-5samples.ipynb)) reads the
environment variable NB_DATA_FILE to decide which file to process.
"""

import os
from runipy.notebook_runner import NotebookRunner
from IPython.nbformat.current import read, write
from IPython.display import display, FileLink
import pandas as pd


def run_single_notebook(notebook_name):
    """Runs the notebook `notebook_name` (file name with no extension).

    This function executes notebook with name `notebook_name` (no extension)
    and saves the fully executed notebook in a new file appending "-out"
    to the original file name.

    It also displays links to the original and executed notebooks.
    """
    nb_name_full  = notebook_name + '.ipynb'
    display(FileLink(nb_name_full))

    with open(nb_name_full) as f:
        notebook = read(f, 'json')
    out_nb_name = notebook_name + '-out.ipynb'

    r = NotebookRunner(notebook)
    try:
        r.run_notebook()
    except Exception, e:
        msg = 'Error executing the notebook "%s".\n\n' % notebook_name
        msg += 'See notebook "%s" for the traceback.' % out_nb_name
        print msg
        raise e
    finally:
        with open(out_nb_name, 'w') as f:
            write(r.nb, f, 'json')
        display(FileLink(out_nb_name))


def run_notebook_ALEX(notebook_name, remove_out=True,
                      data_ids=['7d', '12d', '17d', '22d', '27d']):
    """Run a template ALEX notebook for all the 5 samples.

    Fit results are saved in the folder 'results'.
    For each sample, the evaluated notebook containing both plots
    and text output is saved in the 'out_notebooks' folder.
    """
    data_fname = 'results/' + notebook_name + '.txt'
    if remove_out and \
       os.path.exists(data_fname):
            os.remove(data_fname)

    nb_name_full  = notebook_name + '.ipynb'
    display(FileLink(nb_name_full))

    for data_id in data_ids:
        os.environ['NB_DATA_FILE'] = data_id
        with open(nb_name_full) as f:
            notebook = read(f, 'json')
        out_nb_name = 'out_notebooks/' + notebook_name + \
                      '-out-%s.ipynb' % data_id

        r = NotebookRunner(notebook)
        try:
            r.run_notebook()
        except:
            msg = 'Error executing the notebook for sample "%s".\n\n' % data_id
            msg += 'See notebook "%s" for the traceback.' % out_nb_name
            raise RuntimeError(msg)
        finally:
            with open(out_nb_name, 'w') as f:
                write(r.nb, f, 'json')
            display(FileLink(out_nb_name))
    display(pd.read_csv(data_fname, sep="\s+").set_index('sample'))