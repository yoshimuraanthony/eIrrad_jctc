import matplotlib.pyplot as plt
from inspect import stack

# eIrrad modules
from eIrrad.plotScatter import ScatterPlot

# constants, unit conversions, and dictionaries
from constants import *

# hBNdir = "/p/lustre1/yoshia/radEffects/materials/hBN/qe/Eb/040000/03x03x01"
hBNdir = "/p/lustre1/yoshia/radEffects/materials/hBN/qe/Eb/040000/18x18x01"

pinfile = 'newprob.txt'
kinfile = 'kpts.txt'
hBNpinfile = f'{hBNdir}/{pinfile}'
hBNkinfile = f'{hBNdir}/{kinfile}'
hBNexroot = f'{hBNdir}/tmp/hBN.export'

def scatterDirHBN(
        outfile = 'auto',
        markersize = 2,
        figsize=(6, 5),
        ):
    """One color."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(figsize=figsize, forslides=False, clip_on=True, logy=True)
    plot.readData(pinfile=hBNpinfile, kinfile=hBNkinfile, top=hBNdir)
    plot.plot(transition='direct', color='tab:orange', markersize=markersize,
            label='direct', zorder=4)
    plot.plot(transition='indirect', color='tab:blue', markersize=markersize,
            label='indirect', zorder=3)
    plot.decorate(title=None, grid=False, legend=True,
            xlim=(0, 35), ylim=None, xticks=None, yticks=None,
            ylabel='probability density ($\AA^6$)',
            )
    plot.save(outfile=outfile, writedate=False)
    plot.show()


def scatterHBN(
        outfile = 'auto',
        markersize = 1,
        ):
    """One color."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(forslides=False, clip_on=True, logy=True)
    plot.readData(pinfile=hBNpinfile, kinfile=hBNkinfile, top=hBNdir)
    plot.plot(transition='all', color='tab:blue', markersize=markersize,
            label='hBN', zorder=3)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 35), ylim=None, xticks=None, yticks=None,
            ylabel='probability density ($\AA^6$)',
            )
    plot.save(outfile=outfile, writedate=False)
    plot.show()


def scatterZoomHBN(
        outfile = 'auto',
        markersize = 1,
        ):
    """One color."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(forslides=True, clip_on=True, logy=True)
    plot.readData(pinfile=hBNpinfile, kinfile=hBNkinfile, top=hBNdir)
    plot.plot(transition='all', color='tab:blue', markersize=markersize,
            label='hBN', zorder=3)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 30), xticks=(0, 10, 20, 30),
            ylim=(1e-5, 1e1), yticks=(1e-5, 1e-2, 1e1),
            ylabel='probability density ($\AA^6$)',
            )
    plot.save(outfile=outfile, writedate=False)
    plot.show()
