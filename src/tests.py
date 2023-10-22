import testing.browser_tests as browser_tests
import testing.email_tests as email_tests
import testing.music_tests as music_tests
import testing.general as general

def begin_tests():
    general.main()
    # music_tests.begin()
    # browser_tests.begin()
    # email_tests.begin()

if __name__ == '__main__':
    begin_tests()
