import tests.browser_tests as browser_tests
import tests.email_tests as email_tests
import tests.music_tests as music_tests

def begin_tests():
    browser_tests.begin()
    email_tests.begin()
    music_tests.begin()

if __name__ == '__main__':
    begin_tests()
