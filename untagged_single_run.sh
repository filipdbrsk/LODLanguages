#! /bin/bash
        docid="0c77296e83c678a8757669a19894bde6"
        downloadLink="http://download.lodlaundromat.org/$docid"
        echo $downloadLink
        curl -q -o - $downloadLink | zcat | grep '"' | nodejs untagged.js $docid
#	echo "done"