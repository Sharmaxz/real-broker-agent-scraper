# Real Broker Agent Scrapper

This project fetches agent data from a specified API and writes the data to a CSV file.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Building Executable for Windows](#building-executable-for-windows)
- [License](#license)

## Prerequisites

- Python 3.x
- `requests` library
- `pyinstaller` (for building executables)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Sharmaxz/real-broker-agent-scrapper.git
    cd real-broker-agent-scrapper
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Unix/MacOS
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script and fetch agent data, simply execute:

```sh
python main.py
```

This will create a CSV file named one_real_agents.csv with the fetched data.

## Building Executable for Windows

To build a standalone executable for Windows using `pyinstaller`, follow these steps:

1. Install `pyinstaller`:

    ```sh
    pip install pyinstaller
    ```

2. Run `pyinstaller` to build the executable:

    ```sh
    pyinstaller --onefile main.py
    ```

3. The executable will be created in the `dist` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
