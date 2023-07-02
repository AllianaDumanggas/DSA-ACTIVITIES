class ComboLock():
    def __init__(self, secret1, secret2, secret3):
        self._secrets = [self.assign_secret(secret1), self.assign_secret(secret2), self.assign_secret(secret3)]
        self._dial = 0

    def assign_secret(self, secret):
        if secret > 39:
            return 39
        elif secret < 0:
            return 0
        return secret

    def reset(self):
        self._dial = 0

    def turn_right(self, ticks):
        self._dial = self.dial_scrolling(ticks)
        self.should_unlock(self.get_secret(1))
        if self.get_secret(1) is True:
            print("Secret 1 unlocked.")
            if self.get_secret(2) is True:
                self.should_unlock(self.get_secret(3))
                if self.get_secret(3) is True:
                    print("Combo lock unlocked.")

    def get_secret(self, id):
        return self._secrets[id-1]

    def turn_left(self, ticks):
        self._dial = self.dial_scrolling(-ticks)
        if self.get_secret(1) is True:
            self.should_unlock(self.get_secret(2))
            if self.get_secret(2) is True:
                print("Secret 2 unlocked")

    def should_unlock(self, secret):
        if self.get_dial() == secret:
            secret = True
            return True
        return False

    def get_dial(self):
        return self._dial

    def dial_scrolling(self, ticks):
        dial_pos = 0
        dial = self.get_dial()
        if dial + ticks > 39:
            if ticks >= 39:
                dial_pos += ticks - 39
            elif dial >= 39:
                dial_pos += dial - 40 + ticks
        elif dial + ticks < 0:
            dial_pos = 40 + ticks
        else:
            dial_pos += ticks
        return dial_pos