import sys

from Bio import SeqIO
import click


def trim(record, min_trim_length=20, max_error_prob=0.05):
    """Remove low-quality bases from the sequence

    Modified from Biopython

    Parameters
    ----------
    record : biopython.SeqRecord
        The ABI sequence
    min_trim_length : int
        Minimum sequence of bad quality scores to find before trimming
    max_error_prob : float
        Maximum allowable probability that this base was incorrectly sequenced

    Returns
    -------
    trimmed : biopython.SeqRecord
        Sequence with bad bases removed
    """
    # Has trimming begun?
    start = False

    # Index of first "good" base
    trim_start = 0

    if len(record) <= min_trim_length:
        return record
    else:
        # calculate base score
        score_list = [max_error_prob - (10 ** (qual / -10.0)) for qual in
                      record.letter_annotations['phred_quality']]

        # calculate cummulative score
        # if cummulative value < 0, set it to 0
        # first value is set to 0, because of the assumption that
        # the first base will always be trimmed out
        cummul_score = [0]
        for i in range(1, len(score_list)):
            score = cummul_score[-1] + score_list[i]
            if score < 0:
                cummul_score.append(0)
            else:
                cummul_score.append(score)
                if not start:
                    # trim_start = value when cumulative score is first > 0
                    trim_start = i
                    start = True

        # trim_finish = index of highest cumulative score,
        # marking the end of sequence segment with highest cummulative score
        trim_finish = cummul_score.index(max(cummul_score))

        return record[trim_start:trim_finish]


def maybe_trim(no_trim, verbose, record, min_trim_length, min_quality):
    if not no_trim:
        # Remove bases with probability score less than 0.05
        if verbose:
            click.echo('\tTrimming bases with probability score '
                       '> {min_quality} ...'.format(min_quality=min_quality))

        trimmed = trim(record, min_trim_length, min_quality)

        if verbose:
            click.echo('\tBefore trimming: ' + str(len(record)) +
                       '\tAfter trimming: ' + str(len(trimmed)))
    else:
        trimmed = record
    return trimmed


@click.command()
@click.argument('filename')
@click.option('--verbose', is_flag=True, help="Show progress messages")
@click.option('--no-trim', is_flag=True,
              help="Don't trim nucleotides with error probability >0.05 for "
                   "20 or more nucleotides in a row")
@click.option('--min-trim-length', default=20,
              help='Minimum length of "bad" sequencing scores in a segment')
@click.option('--max-error-prob', default=0.05,
              help='Bases with error rates higher than this are likely to '
                   'be trimmed')
def cli(filename, verbose=True, no_trim=False, min_trim_length=20,
        max_error_prob=0.05):
    """Convert Sanger sequencing format (.ab1) to FASTQ, writes to stdout

    Trimming is performed using the Mott algorithm
    - http://www.phrap.org/phredphrap/phred.html
    """
    # Open the Sanger sequencing trace
    if verbose:
        click.echo('Reading "{filename}" ...'.format(filename=filename))

    record = SeqIO.read(filename, 'abi')

    trimmed = maybe_trim(no_trim, verbose, record, min_trim_length,
                         max_error_prob)

    # Write the trimmed file to fastq format on standard out
    SeqIO.write(trimmed, sys.stdout, 'fastq')


if __name__ == "__main__":
    cli()
