all : smoothdoom-powerpistol.pk3
smoothdoom-powerpistol.pk3 : mod.py src/**/*
	./mod.py
	cd src && zip -r ../smoothdoom-powerpistol.pk3 .
clean :
	rm *.pk3
