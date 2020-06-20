build:
	rm -rf ./dist ./dependencies
	mkdir ./dist
	pip install -t dependencies -r requirements.txt
	cp -r my_app ./dependencies/my_app
	cd ./dependencies && zip -r ../dist/dependencies.zip .
	cp ./Main.py ./dist
	rm -rf ./dependencies
