import json
from io import StringIO
from zipfile import ZipFile

import pandas as pd

df = pd.read_xml(StringIO("log_000.xml"))
print(df.head())


##This function is written to process the log if they were json lines
##I would convert logs from xml to json and write this function


def ingest_logs(zip_filename: str) -> pd.DataFrame:
    with ZipFile(zip_filename) as archive:
        df = pd.DataFrame()
        malformed_lines = 0
        for filename in archive.namelist():
            if not filename.startswith("log"):
                print(f"not interested in {filename}")
                continue

            with archive.open(filename, "r") as f:
                log_lines = []
                for line in f:
                    try:
                        log_entry = json.loads(line)
                        log_lines.append(log_entry)
                    except json.JSONDecodeError:
                        malformed_lines += 1
                    except UnicodeDecodeError:
                        malformed_lines += 1

                if log_lines:
                    df = pd.concat([df, pd.DataFrame(log_lines)])

    return df
