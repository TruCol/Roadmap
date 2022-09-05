"""List of cost model parameters."""


# pylint: disable=R0903

params = {
    "wages": {
        "blockchain_dev": 75 + 1,
        "front_end_dev": 40 + 1,
        "human_resources": 35 + 1,
    },
    # Bounties used to attract initial protocol users.
    "bounty_subsidising": 100000,
    "buffer": 100000,  # Buffer to take unknown costs into account.
}


def dict_to_latex_table(
    the_params: dict, key_header: str, value_header: str, caption: str
):
    """Writes a dict to a latex file.

    :param the_params: dict:
    :param key_header: str:
    :param value_header: str:
    :param caption: str:
    """

    tuples = dict_to_latex_tuples(the_params)
    with open("latex/Tables/params_table.tex", "w", encoding="utf-8") as f:
        backreturn = "\\\\\n" + " " * 4

        content = backreturn.join(
            [f"{_tuple[0]} & {_tuple[1]}" for _tuple in tuples]
        )

        f.write(
            f"""
\\begin{{longtable}}{{@{{}}cp{{.7\\textwidth}}@{{}}}}
    \\caption{{{caption}\\label{{table:nonlin}}}}\\\\
    \\toprule
    {{\\bfseries {key_header}}} & {{\\bfseries {value_header}}} \\\\ \\midrule
    \\endfirsthead
    \\caption{{{caption} (continued)}}\\\\
    \\toprule
    \\multicolumn{{2}}{{l}}{{\\scriptsize\\emph{{\\ldots{{}} continued}}}}\\\\
    {{\\bfseries {key_header}}} & {{\\bfseries {value_header}}} \\\\ \\midrule
    \\endhead
    \\multicolumn{{2}}{{r}}{{\\scriptsize\\emph{{to be continued\\ldots}}}}\\\\
    \\bottomrule
    \\endfoot
    \\bottomrule
    \\endlastfoot
    {content}\\\\
\\end{{longtable}}
    """.strip()
        )


def flatten_dict(some_dict: dict):
    """Flattens a dict that contains values and dicts.

    :param some_dict: dict:
    """
    flat_dict = {}
    # Flatten dict
    for key, value in some_dict.items():
        if isinstance(value, dict):
            for newKey, newValue in value.items():
                flat_dict[newKey] = newValue
        else:
            flat_dict[key] = value
    print(f"flattend_params={flat_dict}")
    return flat_dict


def dict_to_latex_tuples(some_dict: dict):
    """Converts a dict to a list of key,value tuples without underscores.

    :param some_dict: dict:
    """
    flat_dict = flatten_dict(some_dict)
    tuples = []
    for key, value in flat_dict.items():
        if isinstance(key, str):
            key = key.replace("_", " ")
        if isinstance(value, str):
            value = value.replace("_", " ")
        tuples.append((key, value))
    return tuples
