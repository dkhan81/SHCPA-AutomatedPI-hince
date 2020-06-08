import os

def delete_file(path, file_to_delete):
  for filename in os.listdir(path):
    if file_to_delete == filename:
      os.remove(path + "/" + filename)
      return

def change_latest_filename(path, newName):
  try:
    latest_file_name = max([path + '/' + f for f in os.listdir(path)], key=os.path.getctime)
    os.rename(latest_file_name, path + "/" + newName)
  except ValueError:
    pass

