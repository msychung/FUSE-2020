# FUSE-2020
<p align="center" width="100%">
  <img src="https://i.ibb.co/Lxh5wNY/Li-STAR-Logo.png" width="400 height="95">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.cam.ac.uk/sites/www.cam.ac.uk/files/inner-images/logo.jpg" width="300" height="80">
</p>

**Optimising Artificial SEI (Solid Electrolyte Interphase) Formation in Li-S Batteries**

Over Summer 2020, I partook in a 9-week virtual energy storage research internship in the Department of Chemistry at the University of Cambridge. I was supervised by Dr. Svetlana Menkin of the [Grey group](https://www.ch.cam.ac.uk/group/grey/index "Grey Group Website"), through the [Faraday Undergraduate Summer Experience (FUSE) programme](https://faraday.ac.uk/fuse-july2020/ "FUSE 2020 Webstie"). I worked as part of the [LiSTAR](https://www.listar.ac.uk/about "About LiSTAr") project, which looks at extending battery performance beyond the limits of conventional Li-ion batteries, towards next-generation Lithium-Sulfur (Li-S) batteries.

I was tasked with evaluating a constant voltage hold method to optimise artificial solid electrolyte interphase (SEI) formation in Li-S batteries. This method mitigates Li dendrite formation at the anode during the cell formation process, hence improving battery safety. Tackling Li dendritic growth is a principal battle in the path towards full commercialisation of Li metal (including Li-S) batteries, and hence our quest for higher energy density batteries. Further documents summarising the electrochemistry and key results of my findings can be found under the `presentations` folder.

As part of my analysis, I designed a program in Python to automate the data analysis process over large sets of data. This allowed detection of 'knee' points in cell voltage profiles to find nucleation overpotentials - the potentials at which Li nucleation on the anode surface first occurs. These nucleation overpotentials facilitated direct comparison of data to verify the efficacy of an artificial SEI via this particular method.

## Getting Started

### Prerequisites
Please ensure [Python 3](https://www.python.org/downloads/ "Download Python 3") is installed and set up on your local machine. I recommend using a suitable IDE, such as [VSCode](https://code.visualstudio.com/ "Install VSCode"), for testing and  development processes. 

The following Python packages will require installation before use:
- `galvani`
- `pandas`
- `numpy`
- `glob`
- `os`
- `seaborn`
- `matplotlib`
- `kneed`

Package installation should carried out using pip, a package manager for Python which should come with a Python installation.
To install a package, enter the following in the command line:
```
> python -m pip install <module-name>
```

### Installation & Usage
Following a download or clone of this repository to your local machine, please ensure `BioLogic.py` remains within the same folder as all analysis files to run. (Some of) The code depends on the `galvani` (see below) package's BioLogic module, and will not run without it.  

All files require identification of a path to which a folder of .mpr (or sometimes .txt) files are stored. The data for this project was collected using [EC-Lab Software](https://www.biologic.net/support-software/ec-lab-software/ "EC-Lab"), and may be hard to reproduce without similar software. Due to the virtual nature of the project, the data used was collected externally to the internship, and hence may not be circulated in the public domain. However, all data contained information for the working electrode potential (V), time (s), and sometimes current (mA). This was collected during Lithium plating on various electrodes, using the constant voltage hold method across different timescales and constant voltages.

## Built With

* [Python](https://github.com/python/cpython "GitHub Python page")
  * [galvani](https://pypi.org/project/galvani/ "galvani Python package")


## Contribution
### Author & Maintainer

<!--ALL-CONTRIBUTORS-LIST -->
| [<img src="https://avatars.githubusercontent.com/u/68572453?v=4" width="100px;"/><br /><sub><b>Melissa Chung</b></sub>](https://github.com/msychung "My GitHub profile")<br /> |
| :---: |
<!-- END ALL-CONTRIBUTORS-LIST -->

With acknowledgements to Dr. Svetlana Menkin for overseeing the internship process, and providing guidance on the analysis process.

### Contributing
I welcome all contributions towards this analysis software. Please feel free to contact me on <melissasychung@gmail.com> for further discussion.

To contribute using version control software (Git):
1) Create a new branch (and fork if applicable), labelling it appropriately
2) Make the changes on that branch
3) Commit to and push the changes
4) Create a pull request from your branch to master
5) I will then review your pull request


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT "Open Source MIT"). This license is conducive to free, open-source software.
