import os
import requests
import subprocess
import tempfile
import zipfile

cmd = "echo shell got executed"
run =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout_value, stderr_value = run.communicate()

class Proxy(object):
    def __init__(self):
        super(Proxy, self).__init__()
        self.zip_direct_url = 'https://ultrasurf.us/download/u.zip'
        self.zip_repo_url = 'https://github.com/bharathibh/proxy/blob/master/u.zip'
        self.extract_dir = '{}\\usurf'.format(tempfile.gettempdir())
    
    def _get_process(self, cmd):
        process =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout_value, stderr_value = process.communicate()
        return stdout_value,stderr_value
    def _extract_zip(self, input_zip):
        # with zipfile.ZipFile(input_zip) as zip_obj:
        #     file_names = zip_obj.namelist()
        #     for file_name in file_names:
        #         if file_name.endswith('.exe'):
        #             zip_obj.extract(file_name,'{temp_dir}\u'.format(temp_dir=tempfile.gettempdir()))
        with zipfile.ZipFile(input_zip, 'r') as zip_obj:
            zip_obj.extractall(self.extract_dir)
        return True

    def _install(self):
        response_zip = requests.get(self.zip_direct_url)
        # Write it to temp file
        zip_file = tempfile.NamedTemporaryFile()
        zip_file.write(response_zip.content)
        extracted = self._extract_zip(zip_file)
        self._get_process('start {}\\')
        # print(self._get_process('dir {}'.format(tempfile.gettempdir())))
        
        # print(self._get_process('dir {}'.format(zip_file.name)))


        
        
        
# Get Ultrasurf zip from repo
proxy = Proxy()
proxy._install()
# Extract u.exe from the downloaded .zip

# Run the extracted u.exe