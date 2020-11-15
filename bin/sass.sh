#!/bin/bash

project_dir="$HOME/Repositories/Susan-Kill-Kegan-and-Associates"

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

declare -a path=(
  "home/static/global/sass"
  "home/static/home/sass"
  "gallery/static/gallery/sass"
)

includes=$(printf -- " -I $project_dir/%s" ${path[@]})
includes=${includes:1}

cd $project_dir

for i in "${args[@]}"; do
  cmd="sass --watch $includes $i"

  echo $cmd >&2
  $cmd &
done

trap 'echo -e "\nExiting…" >&2; pkill $$' SIGINT

wait
