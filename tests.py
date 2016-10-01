import unittest

from rijndael import Rijndael


class TestRijndael(unittest.TestCase):
  """Test the Rijndael class."""

  def test_encdec(self):
    """Basic sanity check."""
    for blocklen in [16, 24, 32]:
      for key_size in [16, 24, 32]:
        secret = 'b' * blocklen
        key = 'a' * key_size
        r = Rijndael(key, blocklen)
        self.assertEqual(secret, r.decrypt(r.encrypt(secret)))
        self.assertEqual(secret, r.encrypt(r.decrypt(secret)))
        self.assertNotEqual(secret, r.encrypt(secret))
        self.assertNotEqual(secret, r.decrypt(secret))


if __name__ == '__main__':
  unittest.main()
