# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self.diary = diary

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.diary.locked == True:
            return 'Go away!'
        return self.diary.contents

    def lock(self):
        # Locks the diary
        # Returns nothing
        pass

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.diary.locked = False
