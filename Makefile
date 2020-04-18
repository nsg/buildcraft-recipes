SHELL=/bin/bash

run: source .env black guidebook
	. .env/bin/activate && python generate.py

.env:
	virtualenv -p python3 .env
	. .env/bin/activate && pip install black

black: .env
	. .env/bin/activate && black generate.py

source:
	git clone -b 8.0.x-1.12.2 https://github.com/BuildCraft/BuildCraft.git source

.PHONY: guidebook
guidebook:
	echo -e '# guidebook screenshots\n\n' > guidebook.md
	for guide in $$(find guidebook -name *.png | sort); do echo -e "## [$$guide]($$guide)\n![]($$guide)"; done >> guidebook.md

clean:
	rm -rf source .env
