#!/usr/bin/env bas
version="$(cat version.txt)"

./build-java.sh
./build-bedrock.sh

# modrinth is weird and only allows one file per version
cd build
zip -9r "ClassiCube Textures, Font, and Sounds for Minecraft $version.zip" *.zip *.mcpack
exit
