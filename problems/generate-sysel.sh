#!/usr/bin/env bash
for d in ./mh_*/; do
    echo $d;
    python3 ${d}gen.py > ${d}/data.in;
    python ${d}sol.py < ${d}data.in > ${d}data.out;
done
