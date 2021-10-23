import typing as t

from json import loads as load_json
from blockdatas import convert_to_block


GLOBAL_STYLES = r'<style>a{text-decoration:underline;}code{background:rgba(250, 239, 240, 0.78);color:#b44437;padding:3px 4px;border-radius:5px;margin:0 1px;};</style>'



def load(json: t.Union[str, bytes, dict], add_global_styles: bool=True) -> t.Optional[str]:
    """
        Loads the Editor.js data and returns a HTML string.

        ### Parameters:
        - `json` - The Editor.js output data.
        - `add_global_styles` - Whether or not to add a leading `<style>` tag to make the output HTML look more as it is in the editor.
    """

    data = load_json(json) if not isinstance(json, dict) else json # type: dict
    blocks = data.get("blocks", [])
    result = f"{GLOBAL_STYLES}\n" if add_global_styles else ''

    if len(blocks) <= 0:
        return None


    for raw_block in blocks:
        block = convert_to_block(raw_block)

        if block:
            result += f"{block.as_html}\n"


    return result
        


if __name__ == "__main__":
    with open("example.json", 'r', encoding='UTF-8') as DUMMY_FILE:
        DUMMY_JSON = DUMMY_FILE.read()

    with open("example.html", 'w', encoding='UTF-8') as result_file:
        result_file.write(load(DUMMY_JSON))


    print("Done!")
