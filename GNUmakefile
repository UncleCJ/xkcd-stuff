default: all

PNGS=tech_support_cheat_sheet_sv.png

all: $(PNGS)

%.png: %.svg
	inkscape -z --export-width=732 --export-height=823 --export-png="$@" "$<"
