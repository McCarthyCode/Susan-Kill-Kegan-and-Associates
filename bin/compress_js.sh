#!/bin/bash

closure_compiler="/opt/closure-compiler/closure-compiler-v20190929.jar"

js_input_global="home/static/home/js/global.js"
js_output_global="home/static/home/js/global.min.js"

declare -a commands=(
  # "java -jar $closure_compiler --js $js_input_global --js_output_file $js_output_global"
)

for i in "${commands[@]}"; do
  echo "$i"
  $i
done
