all : smoothdoom-powerpistol.pk3
smoothdoom-powerpistol.pk3 : src/*
	cd src && zip -r ../smoothdoom-powerpistol.pk3 .
clean :
	rm *.pk3
