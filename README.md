# CoinPicker

Determine most profitable cryptocurrency

## Usage

```bash
python coinPicker.py --coin Ethereum --file ./approvedCoinFile
``` 
## Docker

```bash
docker build -t torpus/coinPicker .
docker run --rm -it torpus/coinPicker -c Ethereum -f approvedCoinList
```

To make executable, add to shell's .rc file(`~/.bashrc`):

```bash
alias 'coinPicker'='docker run --rm -it torpus/coinPicker -f approvedCoinList'
```

Then reload your shell by running:

```bash
source ~/.bashrc
```

Then use by:

```
coinPicker -c Ethereum
```

## Requirements

Add coins you're interested in to a file, separated by \n
