$(document).ready(() => {
  $('#carousel').hover(
    function () {
      $(this).carousel('pause');
    },
    function () {
      $(this).carousel('cycle');
    }
  );

  function carouselResize() {
    let $inner = $('#carousel .carousel-inner');
    let $items = $('#carousel .carousel-inner .carousel-item')
    let $imgs = $('#carousel .carousel-inner .carousel-item img')
    let max = 0;

    $imgs.each(function () {
      let $this = $(this);
      let width = this.naturalWidth;
      let height = this.naturalHeight;
      let newWidth = Math.min(width, $(window).width());
      let newHeight = Math.min(height, height * $(window).width() / width);

      $this.width(newWidth);
      $this.height(newHeight);

      max = newHeight > max ? newHeight : max;
    });

    $('#carousel .carousel-inner, #carousel .carousel-inner .carousel-item')
      .css('height', `${max}px`);
  }

  carouselResize();
  $(window).on('resize orientationchange', carouselResize);
});
