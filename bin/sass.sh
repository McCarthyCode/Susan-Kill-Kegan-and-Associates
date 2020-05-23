#!/bin/bash

sass_input_home="home/static/home/sass/base.sass"
sass_output_home="home/static/home/css/home.css"
sass_output_home_compressed="home/static/home/css/home.min.css"

sass_input_gallery="gallery/static/gallery/sass/base.sass"
sass_output_gallery="gallery/static/gallery/css/gallery.css"
sass_output_gallery_compressed="gallery/static/gallery/css/gallery.min.css"

declare -a args=(
  "$sass_input_home:$sass_output_home"
  "--style=compressed $sass_input_home:$sass_output_home_compressed"
  "$sass_input_gallery:$sass_output_gallery"
  "--style=compressed $sass_input_gallery:$sass_output_gallery_compressed"
)

for i in "${args[@]}"; do
  sass --watch $i &
done

clear
