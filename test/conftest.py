"""Defines test fixtures."""

import pytest

from yapycrf.io.dataset import Dataset
from yapycrf.io.vocab import Vocab
from yapycrf.model import CharLSTM, CRF, Tagger


LABELS = ["O", "B-NAME", "I-NAME"]


@pytest.fixture(scope="session")
def vocab():
    return Vocab(LABELS, cache="test/.vector_cache")


@pytest.fixture(scope="session")
def dataset(vocab):
    dataset = Dataset()
    dataset.load_file("test/data/sample_dataset.txt", vocab)
    return dataset


@pytest.fixture(scope="session")
def crf():
    return CRF(len(LABELS))


@pytest.fixture(scope="session")
def char_lstm(vocab):
    return CharLSTM(vocab.n_chars, 50)


@pytest.fixture(scope="session")
def tagger(vocab, char_lstm, crf):
    return Tagger(vocab, char_lstm, crf, hidden_dim=50)
