import os

import xml.etree.ElementTree as ET
from collections import defaultdict

fp = r"D:\Python\geom\rhino\default.xml"
cmds_path = r"D:\Python\geom\rhino\commands_full.txt"
cmds_keys_path = r"D:\Python\geom\rhino\commands.txt"

tree = ET.parse(fp)
root = tree.getroot()


def write_all_macros():
    macros = root.find("macros")

    macro_items = macros.findall("macro_item")

    # scripts = [mi.find("script") for mi in macro_items]
    # scripts = [s.text for s in scripts if s is not None]

    skipped_scripts = 0

    commands = []
    grouped_commands = defaultdict(list)

    for mi in macro_items:
        script = mi.find("script")
        if script is not None:
            text = script.text
            if text.startswith("! "):
                text = text[2:]
            elif text.startswith("!"):
                text = text[1:]

            prefix = text.split(" ")[0].replace(" ", "").replace("\'", "")
            grouped_commands[prefix].append(text.replace("\'", ""))
            commands.append(text)
        else:
            skipped_scripts += 1

    print("commands", len(commands))

    cmds_names = list(grouped_commands.keys())

    print("grouped_commands", len(cmds_names))
    for s in cmds_names[:10]:
        print(s)

    cmd_keys = sorted(list(grouped_commands.keys()))

    lines = []
    for cmd_name in cmd_keys:
        lines.append(cmd_name + "\n")
        full_cmds = grouped_commands[cmd_name]

        if len(full_cmds) == 1 and full_cmds[0] == cmd_name:
            continue

        for cmd in full_cmds:
            lines.append("\t" + cmd + "\n")

    with open(cmds_path, "w") as f:
        f.writelines(lines)

    lines = []
    for cmd_name in grouped_commands.keys():
        cmd_name = cmd_name.replace(" ", "").replace("-", "").replace("_", "")
        lines.append(cmd_name + "\n")

    lines = sorted(list(set(lines)))

    with open(cmds_keys_path, "w") as f:
        f.writelines(lines)


def get_all_toolbars():
    toolbars = root.find("tool_bars").findall("tool_bar")

    out = defaultdict(list)
    for tb in toolbars:
        text = tb.find("text")
        if text is not None:
            tb_item = text.find("locale_1033")
            if tb_item is not None:
                tb_name = tb_item.text

                for tbi in tb.findall("tool_bar_item"):
                    tx_item = tbi.find("text")
                    if tx_item is not None:
                        icon_name = tx_item.find("locale_1033").text

                        commands_items = [icon_name]
                        left = tbi.find("left_macro_id")
                        right = tbi.find("right_macro_id")

                        if left is not None:
                            cmd_guid = left.text
                            commands_items.append(("left:", cmd_guid))
                        else:
                            commands_items.append(("left:", None))

                        if right is not None:
                            cmd_guid = right.text
                            commands_items.append(("right:", cmd_guid))
                        else:
                            commands_items.append(("right:", None))

                        out[tb_name].append(commands_items)

    return out


def get_macros_guids_dict():
    macros = root.find("macros")
    macro_items = macros.findall("macro_item")

    out = dict()

    for mi in macro_items:
        guid = mi.get("guid")
        name = mi.find("text").find("locale_1033").text
        script = mi.find("script")
        if script is not None:
            script_text = script.text
            out[guid] = name, script_text
    return out


if __name__ == '__main__':
    folder = r"D:\Python\geom\rhino\toolbars_commands"
    if not os.path.exists(folder):
        os.makedirs(folder)

    toolbars = get_all_toolbars()
    macro_items = get_macros_guids_dict()
    # for tb in toolbars:
    #     print(tb)
    print("---------------Extrude----------------")
    items = toolbars["Extrude"]
    for tb_name, items in toolbars.items():
        lines = []
        for tbi in items:
            mi_name, l, r = tbi

            lines.append("\n" + mi_name + "\n")

            l_guid = l[1]
            r_guid = r[1]

            lname, lcmd = "", ""
            rname, rcmd = "", ""
            if l_guid is not None:
                l_data = macro_items.get(l_guid)
                if l_data:
                    lname, lcmd = l_data
                    lcmd = lcmd.replace("\n", " ")
                    # lines.append(f"\tleft: {lcmd}\n")
                    lines.append(f"\t{lcmd}\n")

            if r_guid is not None:
                r_data = macro_items.get(r_guid)
                if r_data:
                    rname, rcmd = r_data
                    rcmd = rcmd.replace("\n", " ")
                    # lines.append(f"\tright: {rcmd}\n")
                    lines.append(f"\t{rcmd}\n")

        tb_fpath = os.path.join(folder, tb_name + ".txt")
        with open(tb_fpath, "w") as tb_file:
            tb_file.writelines(lines)
