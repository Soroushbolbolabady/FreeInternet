import re


# function for replace uuid in client config
def replace_new_uuid(uuid):
    # Read client config file and find the uuid
    with open("files/config.json", "r+") as file:
        data = file.read()
        new_data = re.sub('[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}', uuid, data)
        file.close()
    # Write new uuid in client config file
    with open("files/config.json", "w") as file:
        file.write(new_data)
        file.close()
