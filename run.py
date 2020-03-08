from app.tasks import process_loan
import logging

INPUT_PATH = "app/data/Loans.csv"
OUTPUT_PATH = "app/data/Output.csv"

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    result = process_loan.delay(INPUT_PATH,OUTPUT_PATH)

    logger.info('Processing loans aggregates finished? %s',result.ready())
    logger.info('Processing loans aggregates result? %s', result.result)