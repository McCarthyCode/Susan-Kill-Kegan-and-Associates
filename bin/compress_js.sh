#!/bin/bash

set -e

closure_compiler="bin/closure-compiler-v20201102.jar"

declare -a path=(
  "home/static/global/js"
  "home/static/home/js"
  "gallery/static/gallery/js"
)

trap 'echo -e "\nExiting…" >&2; pkill $$; exit' SIGINT

while true; do
  for dir in ${path[@]}; do
    files=$(ls -1 $dir/*.js | sed '/.*\.min\.js/d')

    for input in $files; do
      output=$(echo $input | sed -r 's/(.*)\.js/\1\.min\.js/')
      cmd="java -jar $closure_compiler --language_in=STABLE --js $input --js_output_file $output"

      if [ $input -nt $output ]; then
        echo "[$(date -Iseconds)] $cmd" >&2
        $cmd
      fi
    done
  done

  sleep 1
done
