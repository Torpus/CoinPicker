#!/usr/bin/env python3
import pytest
from src.coinPicker import *

def test_checkFileExists():
    assert checkFileExists(__file__) == True

def test_fetchCoinJson():
    try:
        fetchCoinJson('Ethereum','./approvedCoinFile')
    except:
        pytest.fail("Unexpected Error")
