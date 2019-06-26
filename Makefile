all : smoothdoom-powerpistol.pk3
smoothdoom-powerpistol.pk3 : mod.py smoothdoom/**/* additional-files/**/*
	rm -r *.pk3 build/ 2> /dev/null || echo
	cp -r smoothdoom build
	cp -r additional-files/* build/
	./mod.py
	cd build && zip -r ../smoothdoom-powerpistol.pk3 .
clean :
	rm -r *.pk3 build/ 2> /dev/null || echo
