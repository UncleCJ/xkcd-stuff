default: all

LANGS=sv en
PNGS=$(foreach lang,$(LANGS),tech_support_cheat_sheet_$(lang).png)

all: $(PNGS)

%.png: %.svg
	inkscape -z --export-width=732 --export-height=823 --export-png="$@" "$<"

tech_support_cheat_sheet_%.svg: transcription_%.yaml tech_support_cheat_sheet_template.svg
	./replace_textnodes.py --node-values "$<" --xml-file tech_support_cheat_sheet_template.svg > "$@"
