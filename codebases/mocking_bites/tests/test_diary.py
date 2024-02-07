from lib.secret_diary import SecretDiary
from unittest.mock import Mock

# File: lib/secret_diary.py

def test_read():
    diary = Mock()
    diary.locked = True
    secret_diary = SecretDiary(diary)
    assert secret_diary.read() == 'Go away!'
    # Raises the error "Go away!" if the diary is locked
    # Returns the diary's contents if the diary is unlocked
    # The diary starts off locked

def test_unlock():
    diary = Mock()
    diary.locked = True
    diary.contents = 'Test entry'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Test entry'
    # Unlocks the diary
    # Returns nothing
