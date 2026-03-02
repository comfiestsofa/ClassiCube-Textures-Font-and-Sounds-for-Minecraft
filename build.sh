#!/usr/bin/env bash
version="$(cat version.txt)"

./build-java.sh
./build-bedrock.sh

cd build
zip -9r "ClassiCube Textures, Font, and Sounds for Minecraft $version.zip" *.zip *.mcpack
exit
