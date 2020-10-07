import json


def save_json(save_file, data, sort_key=True):
    """Save json

    Parameters
    ----------
    save_file : str
    data : list or dict
    sort_key : bool, optional
        by default True
    """
    with open(save_file, 'w') as f:
        json.dump(data, f, ensure_ascii=False,
                  indent=4, sort_keys=sort_key, separators=(',', ': '))


def load_json(file):
    """Load json file

    Parameters
    ----------
    file : str
        input json file

    Returns
    -------
    data : dict
    """
    with open(file, 'r') as f:
        data = json.load(f)
    return data
