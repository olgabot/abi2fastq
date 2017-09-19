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


def test_cli_with_arguments(example_ab1, example_fastq):
    from abi2fastq.cli import cli

    runner = CliRunner()
    test = runner.invoke(cli, [example_ab1])

    with open(example_fastq) as f:
        true_output = f.read()
    assert test.output.strip() == true_output.strip()
