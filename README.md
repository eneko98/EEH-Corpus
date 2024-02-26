# Egungo Euskararen Hiztegia (EEH) Corpus

This repository hosts a corpus derived from the Egungo Euskararen Hiztegia (EEH), a comprehensive Basque dictionary. The original dictionary data, in SQL format, was obtained from [Euskal Herriko Unibertsitatea](https://www.ehu.eus/eeh/), and has been processed into a JSON format to facilitate natural language processing and machine learning tasks. The corpus encompasses 69,538 words, with each entry featuring the word, its definition, and example sentences (where applicable).

## Contents

- `EEH-23-01-26.sql` - The original SQL file of the Egungo Euskararen Hiztegia, reflecting the dictionary's state as of January 26, 2023.
- `data_parser.py` - A Python script used to extract information from the SQL file and transform it into a structured JSON format.
- `basque_corpus.json` - The JSON format corpus, containing 69,538 words, each accompanied by definitions and, optionally, example sentences illustrating their use.

## Getting Started

To work with this corpus, familiarity with SQL and Python is recommended. You can visualize the original SQL file using tools like SQL Workbench, which offers an intuitive interface for exploring SQL databases.

### Prerequisites

- Python 3.x
- An SQL viewer like SQL Workbench or a similar tool for accessing the contents of the `EEH-23-01-26.sql` file.
- Standard Python libraries (`json`, `re`) for running the script. No external libraries are required.

### Usage

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/eneko98/EEH-Corpus.git
    ```

2. To explore the original SQL database, open the `EEH-23-01-26.sql` file using your preferred SQL database tool.
3. Modify the `data_parser.py` script to include the correct file paths for your system. This involves setting the path to the `EEH-23-01-26.sql` file and specifying the output path for the `basque_corpus.json` file.
4. Run the `data_parser.py` script to convert the SQL data into a structured JSON corpus:
    ```
    python data_parser.py
    ```


## Contributing

Your contributions to the EEH Corpus project are highly appreciated! Feel free to fork the repository, make your changes, and submit pull requests.

## Acknowledgments

- This corpus is based on data from the Egungo Euskararen Hiztegia (EEH), made available by [Egungo Euskararen Hiztegia](https://www.ehu.eus/eeh/).

