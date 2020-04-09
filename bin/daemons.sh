#!/bin/bash

sass_input_home="home/static/home/sass/base.sass"
sass_output_home="home/static/home/css/home.css"
sass_output_home_compressed="home/static/home/css/home.min.css"

sass_input_gallery="gallery/static/gallery/sass/base.sass"
sass_output_gallery="gallery/static/gallery/css/gallery.css"
sass_output_gallery_compressed="gallery/static/gallery/css/gallery.min.css"

declare -a foo=()
declare -a daemons=(
  "source .env/bin/activate; python manage.py runserver 10.0.0.100:8000"
  "sass --watch $sass_input_home:$sass_output_home"
  "sass --watch --style=compressed $sass_input_home:$sass_output_home_compressed"
  "sass --watch $sass_input_gallery:$sass_output_gallery"
  "sass --watch --style=compressed $sass_input_gallery:$sass_output_gallery_compressed"
)

for i in "${daemons[@]}"; do
  foo+=(--tab -e "bash -c '$i; exec bash'")
done

gnome-terminal "${foo[@]}"
