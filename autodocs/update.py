import gh_md_to_html.core_converter
import requests
import yaml
import os
import glob


try:
    os.mkdir("../docs")
except FileExistsError:
    for file in glob.glob("../docs/*"):
        os.remove(file)

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

with open("template.html", "r") as file:
    template = file.read()
    
for folder in config["folders"]:
    os.mkdir("../" + folder)

for path in config["files"]:
    for filen in glob.glob("../" + path):
        if filen.endswith(".md"):
            with open(filen, "r") as file:
                raw = file.read()
            html = gh_md_to_html.core_converter.markdown(raw)
            with open("../docs/" + filen.removeprefix("../").removesuffix(".md") + ".html", "w") as file:
                file.write(
                    template
                        .replace("%title%", filen)
                        .replace("%content%", html)
                )
        else:
            with open(filen, "rb") as file:
                raw = file.read()
            with open("../docs/" + filen.removeprefix("../"), "wb") as file:
                file.write(raw)
             
if "index" in config:
    with open("../" + config["index"], "r") as file:
        raw = file.read()
    html = gh_md_to_html.core_converter.markdown(raw)
    with open("../docs/index.html", "w") as file:
        file.write(
            template
                .replace("%title%", filen)
                .replace("%content%", html)
        )
