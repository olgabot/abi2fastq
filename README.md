[![PyPI Versions](https://img.shields.io/pypi/pyversions/abi2fastq.svg)]()
[![PyPI License](https://img.shields.io/pypi/l/abi2fastq.svg)]()

# abi2fastq
abi2fastq is a small utility to convert Sanger sequencing reads in .abi (applied biosystems) format to FASTQ

## Installation


### With `conda`/`bioconda` (recommended)

As BioPython is a dependency of `abi2fastq`, it is recommended to use
`bioconda` to install because of the C libraries that are necessary in `numpy`,
a dependency of `bioconda.

```
conda install --channel bioconda abi2fastq
```

### With `pip`

Using `pip`, you can grab the latest version of `abi2fastq` from the Python
Package Index.

```
pip install abi2fastq
```

### Bleeding edge version (for advanced users)

To install this code, clone this github repository and use `pip` to install

    git clone https://github.com/olgabot/abi2fastq.git
    cd abi2fastq
    conda env create --file environment.yml
    source activate abi2fastq-env



## Usage