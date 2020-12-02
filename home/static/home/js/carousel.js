const sleep = (milliseconds) => {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
};

$(document).ready(() => {
  $('#carousel').hover(
    function () {
      $(this).carousel('pause');
    },
    function () {
      $(this).carousel('cycle');
    },
  );

  function carouselResize() {
    const $carousel = $('#carousel');
    const $imgs = $carousel.find('img');

    let max = 0;
    $imgs.each(async function () {
      let width = this.naturalWidth;
      let height = this.naturalHeight;

      while (!width || !height) {
        await sleep(50);
        width = this.naturalWidth;
        height = this.naturalHeight;
      }

      const newWidth = Math.min(width, $(window).width());
      const newHeight = Math.min(height, (height * $(window).width()) / width);

      const $this = $(this);
      $this.width(newWidth);
      $this.height(newHeight);

      max = Math.max(newHeight, max);
    });

    $carousel.find('.carousel-inner, .carousel-item').css('height', `${max}px`);
  }

  carouselResize();
  $(window).on('resize orientationchange', carouselResize);
});
