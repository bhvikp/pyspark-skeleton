"""
    Main script for application.
"""

__author__ = ['Bhavik Patel']
__version__ = "1.0.0"

from my_app import app


def main():
    # init main object
    print("Initializing script..")
    obj = app.App()

    print("Running app..")
    obj.run()


if __name__ == '__main__':
    main()
