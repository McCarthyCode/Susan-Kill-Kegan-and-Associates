#!/bin/bash

closure_compiler="/opt/closure-compiler/closure-compiler-v20190929.jar"

js_input_global="home/static/home/js/global.js"
js_output_global="home/static/home/js/global.min.js"

js_input_carousel="home/static/home/js/carousel.js"
js_output_carousel="home/static/home/js/carousel.min.js"

declare -a commands=(
  # "java -jar $closure_compiler --js $js_input_global --js_output_file $js_output_global"
  # "java -jar $closure_compiler --js $js_input_carousel --js_output_file $js_output_carousel"
)

for i in "${commands[@]}"; do
  echo "$i"
  $i
done
