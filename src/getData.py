import os
import wget
import zipfile


def download():
    try:
        url = "https://archive.ics.uci.edu/ml/machine-learning-\
        databases/00275/Bike-Sharing-Dataset.zip"
        out_dir = "../data/"
        unzip_dir = "../data/BSD/"
        wget.download(url, out=out_dir)

        with zipfile.ZipFile(out_dir + "Bike-Sharing-Dataset.zip", "r") as zp:
            zp.extractall(unzip_dir)

        os.remove(out_dir + "Bike-Sharing-Dataset.zip")
    except Exception as ex:
        print(ex)


def main():
    download()


if __name__ == "__main__":
    main()
