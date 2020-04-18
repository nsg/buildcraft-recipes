
run: source .env black
	. .env/bin/activate && python generate.py

.env:
	virtualenv -p python3 .env
	. .env/bin/activate && pip install black

black: .env
	. .env/bin/activate && black generate.py

source:
	git clone -b 8.0.x-1.12.2 https://github.com/BuildCraft/BuildCraft.git source

clean:
	rm -rf source .env
