# import os
# import tarfile
# import ssl
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
   # getattr(ssl, '_create_unverified_context', None)):
   # ssl._create_default_https_context = ssl._create_unverified_context

# from six.moves import urllib
# download_root = "https://github.com/ageron/handson-ml/raw/master/"
# housing_path = "datasets/housing"
# housing_url = download_root+housing_path+"/housing.tgz"


# def fetch_housing_data(house_url = housing_url, house_path = housing_path):
   # if not os.path.isdir(house_path):
       # os.makedirs(house_path)
   # tgz_path = os.path.join(house_path, "housing.tgz")
   # urllib.request.urlretrieve(house_url, tgz_path)
   # housing_tgz = tarfile.open(tgz_path)
   # housing_tgz.extractall(path=house_path)
   # housing_tgz.close()
# fetch_housing_data()

import os
import subprocess
_popenKwds = {
    "stdin": subprocess.PIPE,
    "stdout": subprocess.PIPE,
    "stderr": subprocess.PIPE
}

REPO_URL = r"https://github.com/ageron/handson-ml.git"
REPO_BASE_PATH = os.getcwd()
# REPO_BASE_PATH = r"C:\Users\pmishra\Desktop\temp"

def git_pull(repo_directory):
    current_dir = os.getcwd()
    os.chdir(repo_directory)
    try:
        cmd_line = r'git pull'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = p.communicate()[0]
        print out
    finally:
        os.chdir(current_dir)
        
def git_clone(repo_directory):
    current_dir = os.getcwd()
    os.chdir(repo_directory)
    try:
        cmd_line = r'git clone ' + REPO_URL
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = p.communicate()[0]
        print out
    finally:
        os.chdir(current_dir)


def clone_repo():
    current_dir = os.getcwd()
    try:
        if not os.path.exists(os.path.join(REPO_BASE_PATH, 'handson-ml')):
            git_clone(REPO_BASE_PATH)
        else:
            git_pull(os.path.join(REPO_BASE_PATH, 'handson-ml'))
    except Exception:
        print traceback.print_exc()
        raise
    finally:
        os.chdir(current_dir)

def main():
    clone_repo()

if __name__ == "__main__":
    main()