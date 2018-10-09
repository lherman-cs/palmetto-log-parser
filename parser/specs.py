# These keys are generated
keys = [
    r'Volatile',
    r'Total',
    # It's in hex somehow
    r'GPU \d{8}:[0-9A-F]{2}:\d{2}\.\d',
    r'L1 Cache',
    r'Retired Pages',
    r'Double Bit ECC',
    r'Timestamp',
    r'Driver Version',
    r'Texture Shared',
    r'Pending',
    r'L2 Cache',
    r'Register File',
    r'Texture Memory',
    r'Device Memory',
    r'Aggregate',
    r'Single Bit ECC',
    r'ECC Errors',
    r'CBU',
    r'Current',
    r'Attached GPUs',
    r'Double Bit',
    r'Ecc Mode',
    r'Replays since reset',
    r'Single Bit'
]

specs = [
    ('COMMENT', r'=+.*=+'),  # done
    ('COLON', r':'),
    ('KEY', '|'.join(keys)),  # done
    ('FLOAT', r'-?\d*\.\d+'),  # done
    ('INT', r'-?\d+'),  # done
    ('BOOLEAN', r'Enabled|Disabled|Yes|No'),  # done
    ('DATE', r'\w{3} +?\w{3} +\d{1,2} +?\d{1,2}:\d{1,2}:\d{1,2} +?\d{4}'),
    ('NA', r'N/A'),
    ('SKIP', r'[ \t\r\n]+'),  # done
    ('UNKNOWN', r'.')  # done
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in specs)
