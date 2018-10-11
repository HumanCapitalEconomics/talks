#!/usr/bin/env python
"""This module compiles the lecture notes."""
import subprocess
import argparse
import shutil
import glob
import os


def compile_single(group, is_update):
    """Compile a single lecture."""
    for task in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
        subprocess.check_call(task + ' main', shell=True)

    tgt = '../../distribution/' + group + "/" + os.getcwd().split('/')[-1] + '.pdf'
    if is_update:
        shutil.copy('main.pdf', tgt)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(' Create slides for lecture')

    parser.add_argument('--update', action='store_true', dest='update',
	                    help='update public slides')

    is_complete = os.getcwd().split('/')[-1] in ['research_skills', 'seminal_papers', 'overviews']
    is_update = parser.parse_args().update

    if is_complete:
        group = os.getcwd().split('/')[-1]
        for dirname in glob.glob("0*"):
            os.chdir(dirname)
            compile_single(group, is_update)
            os.chdir('../')
    else:
        group = os.getcwd().split('/')[-2]
        compile_single(group, is_update)
