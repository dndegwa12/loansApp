from __future__ import absolute_import
from app.celery import app
from app.util import LoansReader
from app.util import CSVOutput

from app import logger

"""
we import the app defined in the previous celery module and use it as a decorator for our task method.
"""

@app.task
def process_loan(input_path, output_path):
    reader = LoansReader(input_path)
    logger.info('Loans reader with %i rows and %i MSISDNs'% (len(reader), len(reader.msisdns)))

    header = ['Network', 'Product', 'Date', 'Sum', 'Count']

    CSVOutput.csv_out(header, reader.aggregate_loans, output_path)

