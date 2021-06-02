import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFiles(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.Ax4JI40gQl0TUrh8EvbvKf7VSNn05GuzidFqQUu01vEsSr5ppdgRfaxROUE6R2eEVAlednDpgzJ8bxyrZr7Vs6VHTC2bImWAiORw9-B4PMJWHQU06otKvzwzf1LcJienSIuEpYM'
    transferData = TransferData(accessToken)

    fileFrom = str(input("Enter the folder path to transfer : -"))
    fileTo = input("enter the full path to upload to dropbox:- ")  
    transferData.upload_file(fileFrom,fileTo)
    print("file has been moved !!!")

if __name__ == "__main__":
    main()