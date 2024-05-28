import csv
import dropbox
from dropbox.exceptions import ApiError

csv_path = './students.csv'

# TODO: insert Dropbox Access token.
access_token = 'TODO'

# TODO: dropbox folder path
base_folder = '/CA_projects/2024'

# Initialize the Dropbox client.
dbx = dropbox.Dropbox(access_token)


def create_folder(folder_path):
    try:
        dbx.files_create_folder_v2(folder_path)
        print(f"Folder created: {folder_path}.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"The folder {folder_path} already exists.")
        else:
            print(f"Error during folder creation: {e}.")


def share_folder(folder_path, email):
    try:
        try:
            shared_folder_metadata = dbx.sharing_share_folder(folder_path)
        except:
            pass
        
        shared_folder_metadata = dbx.files_get_metadata(folder_path)
        shared_folder_id = shared_folder_metadata.shared_folder_id
        
        dbx.sharing_add_folder_member(
            shared_folder_id,
            [dropbox.sharing.AddMember(dropbox.sharing.MemberSelector.email(email),
                                       dropbox.sharing.AccessLevel.editor)])
        print(f"Folder {folder_path} shared with {email}.")
    except ApiError as e:
        print(f"Error during sharing of the folder: {e}")


with open(csv_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        email = row['Email']
        name = row['Name'].replace(' ', '_')
        user_name = email.split('@')[0]
        folder_path = f"{base_folder}/{name}_ca_project"

        create_folder(folder_path)
        share_folder(folder_path, email)
