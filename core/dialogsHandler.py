import os


def subscribeDialogs(path: str):
    def getFilesInDirectory(path):
        files = []
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            if os.path.isfile(filepath):
                files.append(
                    {
                        "basename": os.path.basename(filepath).replace(".py", ""),
                        "path": os.path.relpath(filepath)
                        .replace("\\", ".")
                        .replace(".py", ""),
                    }
                )
        return files

    def importDialog(path: str):
        module = __import__(path, fromlist=["getResponse"])
        getResponse = getattr(module, "getResponse")
        return getResponse

    files = getFilesInDirectory(path)
    dialogs = {}
    for filename in files:
        dialogs[filename["basename"]] = importDialog(filename["path"])

    return dialogs


import dialogs.no as no
import dialogs.yes as yes
import dialogs.yesorno as yesorno


def subscribeDialogsByHands():
    return {
        'no': no.getResponse,
        'yes': yes.getResponse,
        'yesorno': yesorno.getResponse,
    }
