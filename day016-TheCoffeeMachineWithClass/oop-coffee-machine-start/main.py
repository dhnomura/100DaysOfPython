key_value=''
def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        global key_value
        key_value="{}.{}".format(key_value, key) 
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key_value, ":", value)
            # key_value='diogo'

nested_dictionary = {"dict1": {"a": 1, "values": {"x":1,"y":2}},"dict2": {"b": 2}}


get_all_values(nested_dictionary)