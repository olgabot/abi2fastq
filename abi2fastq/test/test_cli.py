import os

from click.testing import CliRunner
import pytest


@pytest.fixture
def data_folder():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


@pytest.fixture
def example_prefix():
    return 'ZN-1_ZNif1__2017-06-07_B01'


@pytest.fixture
def example_ab1(data_folder, example_prefix):
    return os.path.join(data_folder, example_prefix + '.ab1')


@pytest.fixture
def example_fastq(data_folder, example_prefix):
    return os.path.join(data_folder, example_prefix + '.fastq')


def test_cli_help():
    from abi2fastq.cli import cli

    runner = CliRunner()
    test = runner.invoke(cli, ['--help'])

    true_output = """Usage: cli [OPTIONS] FILENAME

  Convert Sanger sequencing format (.ab1) to FASTQ, writes to stdout

  Trimming is performed using the Mott algorithm -
  http://www.phrap.org/phredphrap/phred.html

Options:
  --verbose                  Show progress messages
  --no-trim                  Don't trim nucleotides with error probability >0.05  # noqa
                             for 20 or more nucleotides in a row
  --min-trim-length INTEGER  Minimum length of "bad" sequencing scores in a
                             segment
  --max-error-prob FLOAT     Bases with error rates higher than this are likely
                             to be trimmed
  --help                     Show this message and exit.
"""

    assert test.output.strip() == true_output.strip()


def test_cli_with_arguments(example_ab1, example_fastq):
    from abi2fastq.cli import cli

    runner = CliRunner()
    test = runner.invoke(cli, [example_ab1])

    with open(example_fastq) as f:
        true_output = f.read()
    assert test.output.strip() == true_output.strip()
