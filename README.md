[![Build Status](https://travis-ci.org/olgabot/abi2fastq.svg?branch=master)](https://travis-ci.org/olgabot/abi2fastq)[![PyPI Versions](https://img.shields.io/pypi/pyversions/abi2fastq.svg)]()
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

Here is the help output for `abi2fastq`:

```
$ abi2fastq --help
Usage: abi2fastq [OPTIONS] FILENAME

  Convert Sanger sequencing format (.ab1) to FASTQ, writes to stdout

  Trimming is performed using the Mott algorithm -
  http://www.phrap.org/phredphrap/phred.html

Options:
  --verbose                  Show progress messages
  --no-trim                  Don't trim nucleotides with error probability
                             >0.05 for 20 or more nucleotides in a row
  --min-trim-length INTEGER  Minimum length of "bad" sequencing scores in a
                             segment
  --max-error-prob FLOAT     Bases with error rates higher than this are
                             likely to be trimmed
  --help                     Show this message and exit.
```

### Example

Here is an example conversion using an `.ab1` file included with this
repository. Notice that is written to standard out.

```
$ abi2fastq abi2fastq/test/data/ZN-1_ZNif1__2017-06-07_B01.ab1 
@ZN-1_ZNif1_
ATGCGAAAAACTTTCTGATCAGTTCCTGTTGATTCCCAAGGTATGCATATGGTAGCCGGGCACGACGCCAATGATGCTGTCATAAGCAATAGCGTTGCGCAAGCGCGATTTTCAGGGCTTCTGATCGTGAAAACAGTTCTCGATCATATTCTGCAAAAGACAGAACGCGGCGTCCGATTGCATCCTCTCGCACGGACGGCTAAGGTGAAAAATGAGGTCAACTCTTTCAAGGCCGCACTGAGCTCTCTGGCAAAACACGGGGAATATGCCCCATTCGCGAGACTGCTTAATTTGTCTGGAGTCAACAATCTGGAGCATGGGCTTTTTCCGCAACTTAGTGCGATTGCCCTGGGGGTAGCTACAGCACACGGTAGCACTTTGGCCGGCGTTAACGTCGGTGAGCAATATCAACAACTGCGAGAAGCAGCGACGGAGGCAGAGAAACAACTGCAACAGTATGCCGAGTCTAGGGAACTGGATCACCTCGGTCTGGATGACCAGGAAAAGAAAATTCTCATGAACTTTCATCAAAAGAAGAACGAGATATCATTTCAGCAGACTAATGCGATGGTCACTCTTCGGAAAGAGCGACTTGCTAAACTCACAGAAGCGATAACAGCAGCATCCTTGCCGAAGACATCAGGCCACTATGACGACGACGACGATATTCCCTTTCCGGGTCCGATTAACGATGACGATAACCCGGGTCATCAAGACGATGATCCCACAGACTCCCAGGACACCACCATCCCCGATGTAGTTGTGGATCCTGATGATGGCTCATACGGCGAGTACCAAAGCTATAGTGAGAATGGCATGAACGCCCCGGGACGATTTGGTATTGTTCGACCTCGATGAAGATGACGAGGATACTAAGCCTGTACCCAACCGAAGTACCAAAGGGCG
+
/5E:.1'&&&1VVK/BP)',&,J^PPG^PX^/--+,**4GPP^R^RXX^^^^X^^^P^^^P^^^\\^^R-\^\L\^^^^\>L\X^\R\^^^^^^^\\^^^^\R^^^^\?\^^3L^^\^^^^^^RR\^^^^^^^^\^^^^^^^\MLD^^^\\^^^^^^^RR^^\\^^\^^^^^^^^^\\^^^^^^^^^^^^^^^^\M\^^^\\^^^^^^^^^^^^^^^^\\\\^^^^^\\^^^^^^^^\^^\\^\^^^^^^^^^^^^^^^^^^\^^^^\^^^^^^^^^^^\RL\^^^^^^\^^^^^^^^^\\^\\^^^^^^^^^RR^^^^^XX^XX^^^^^^^^R^^^^^^^^^^^^^^^^^^^^^^^^^RR^^^^^^^^^^^^^^^^^X^^^^^^^^^^^^^^^^^^^^^^^^^^^^^PP^^^^^^^^^^PP^^^^^^^^^^^>A^^^^LGL^P^^^^^^^^V^^^^^^^^^^^P^^^^^^^^^K^^^KHGI^^^^^^^^^ZZHKZZKE?ZZPFPZKOZZVUZZZEVZZZCPZZZ?LTEIZZP9PZPVAKVZVENVZEJZZZ;FZVZVEAEBPVZVUVSZUJBGOLOZZUZZJLUIE<ZGVIZZVGLAZUIZAUVVPJOCZPUUBPZPZVVSVUZHUZZU<ZUVU2>GDZ@UNZG8AIUFVVIG4UV5VM0NQ9VV<LMEZHZZO@ZBOVNMZBD0=DJG?P??HC:MQ@MAC<OTMP:CI??N?>::OEHI:LO<>E>@48QCT?E0?<>>>>>@:>G;TTPP;5OBE?<EJ4LL=>=>>O98?DA>C9O5D>>A8L18J;;8B31J6;>><L>=>L>=>>8DO;>DG;8H>>TOH-E0562>4TA>;5=JJE40>=:+=D08558E>371;==-=7G==5A74G>C@=A1.8K>524?=9::64>B'G+BT6?8
```

To save the output as a file, use `>` to redirect the output:

```
$ abi2fastq abi2fastq/test/data/ZN-1_ZNif1__2017-06-07_B01.ab1 > ZN-1_ZNif1__2017-06-07_B01.fastq
```
