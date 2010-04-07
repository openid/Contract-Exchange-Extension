#!/bin/bash

rm *.inc
for f in *.xml* ; do
     echo ".. code-block:: xml" > $f.inc 
     echo "" >> $f.inc
     cat $f  | while read line  ; do echo "    $line" >> $f.inc ; done
done
