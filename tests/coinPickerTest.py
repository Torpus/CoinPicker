#!/usr/bin/env python3
import pytest
from src.coinPicker import *

def test_checkFileExists():
    assert checkFileExists('approvedCoinFile') == True
    assert checkFileExists('approvedCoinFile') == False

def test_fetchCoinJson():
    assert fetchCoinJson('Ethereum','approvedCoinFile')
