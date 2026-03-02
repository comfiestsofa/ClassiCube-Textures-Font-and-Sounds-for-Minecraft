#!/usr/bin/env bash
for pack in ClassiCube*/ bedrock/ClassiCube*/; do
	# double slash causes problems
	# https://stackoverflow.com/questions/9018723/what-is-the-simplest-way-to-remove-a-trailing-slash-from-each-parameter
	pack=${pack%/}
	cp -a LICENSE.md "$pack/"
done
exit
