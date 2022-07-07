from random import SystemRandom as sr ; import string as s; print(''.join(sr().choices(s.ascii_letters + s.punctuation,  k = 12 )))
