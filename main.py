import argparse

parser = argparse.ArgumentParser()

parser.add_argument('database', 'data', '--DB', help='link to the database file')

if __name__ == "__main__":
    args = parser.parse_args()
    pass
