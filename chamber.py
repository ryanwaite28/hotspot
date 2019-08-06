import string, random, os

DATABASE_URL = os.environ.get('DATABASE_URL')

def uniqueValue():
  value = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(50))
  return value.lower()

