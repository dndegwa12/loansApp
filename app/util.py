from collections import Counter, namedtuple, defaultdict
import csv
from datetime import datetime

fields = ("MSISDN","Network","Date","Product","Amount")

class LoansRecord(namedtuple('LoansRecord_', fields)):

    @classmethod
    def parse(klass, row):
        row = list(row)
        row[2] = datetime.strptime(row[2], "%d-%b-%y").strftime('%b-%y') # Parse the "Date" to month-year format
        row[4] = int(row[4]) # Convert "Amount" to an integer
        return klass(*row)

class LoansReader(object):

    def __init__(self, path):
        self.path     = path

        self._length  = None
        self._counter = None

    def __iter__(self):
        self._length  = 0
        self._counter = Counter()

        with open(self.path, 'rU') as data:
            data.readline()  # Skips the header
            reader = csv.reader(data)  # Create a regular tuple reader
            for row in map(LoansRecord.parse, reader):

                self._length += 1
                self._counter[row[0]] += 1
                yield row


    def __len__(self):
        if self._length is None:
            for row in self: continue # Read the data for length and counter
        return self._length

    @property
    def counter(self):
        if self._counter is None:
            for row in self: continue # Read the data for length and counter
        return self._counter

    @property
    def msisdns(self):
        return self.counter.keys()

    def reset(self):
        """
        In case of partial seeks (e.g. breaking in the middle of the read)
        """
        self._length  = None
        self._counter = None

    @property
    def aggregate_loans(self):
        """
        Aggregate loans by (Network, Product, Month)
        """
        result = []
        aggregated = defaultdict(list)
        for row in self:
            keys = (row.Network, row.Product, row.Date)
            aggregated[keys].append(row.Amount)
        for key, values in aggregated.items():
            result.append(list(key) + [sum(values), len(values)])
        return result


class CSVOutput:

    @classmethod
    def csv_out(klass, header, rows, path):
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for row in rows:
                writer.writerow(row)