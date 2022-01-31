# fixpgn

This tool fixes player name casing in PGN files. It solves the problem where the same name with different casing might lead a player being identified as different players.

## Usage

Create and activate a virtual environment with:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Install the `chess` package:

```shell
pip install chess
```

Running the script will fix all the PGN files in the current directory and it will output the new contents to the console. The output will merge the contents for all the input files.

```shell
mkdir result
python fixpgn.py > result/db.pgn
```

NOTE: it is important to store the resulting file in a different directory than the current one.
