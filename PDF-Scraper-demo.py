import re

import pdfplumber
import pandas as pd
from collections import namedtuple

Line = namedtuple('Line', 'company_id company_name doctype reference currency voucher inv_date due_date open_amt_tc open_amt_bc current months1 months2 months3')
