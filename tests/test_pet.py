import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
import time

# import your pet_game module
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pet.py import Pet, start_interaction


@pytest.fixture
def sample_pet():
    """Fixture to create a sample Pet object."""
    birthdate = datetime(2020, 5, 1)
    return Pet("bella", birthdate)


def test_feed_increases_hunger(sample_pet):
    sample_pet.hunger = 50
    sample_pet.feed()
    assert sample_pet.hunger > 50
    assert "fed" in sample_pet.interactions


def test_exercise_reduces_energy_and_hunger(sample_pet):
    start_energy = sample_pet.energy
    start_hunger = sample_pet.hunger
    sample_pet.exercise()
    assert sample_pet.energy < start_energy
    assert sample_pet.hunger <= start_hunger
    assert "exercised" in sample_pet.interactions


def test_check_energy_output(sample_pet, capsys):
    sample_pet.energy = 10
    sample_pet.check_energy()
    output = capsys.readouterr().out
    assert "tired" in output


def test_feed_sets_is_full(sample_pet):
    sample_pet.hunger = 90
    sample_pet.feed()
    assert sample_pet.is_full is True


def test_change_behavior_happy(sample_pet, capsys):
    sample_pet.hunger = 100
    sample_pet.energy = 100
    sample_pet.change_behavior()
    output = capsys.readouterr().out
    assert "happy" in output


@patch("builtins.input", side_effect=["Buddy", "2020", "5", "1", "8"])
def test_start_interaction_exits_immediately(mock_input, capsys):
    start_interaction()
    output = capsys.readouterr().out
    assert "welcomee" in output