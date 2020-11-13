function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

$(() => {
  const $carousel = $('#carousel');
  $carousel
    .on('mouseenter', function () {
      $(this).carousel('pause');
    })
    .on('mouseleave', function () {
      $(this).carousel('cycle');
    })
    .on('slide.bs.carousel', function (event) {
      // console.log(event);
    });

  async function carouselResize() {
    const windowWidth = $(window).width();

    let count = 0;
    let maxHeight = 0;
    const $imgs = $carousel.find('img');
    $imgs.each(function () {
      const $img = $(this).one('load', function () {
        const width = this.naturalWidth;
        const height = this.naturalHeight;
        const newWidth = Math.min(width, windowWidth);
        const newHeight = Math.min(height, (height * windowWidth) / width);

        $img.width(newWidth);
        $img.height(newHeight);

        maxHeight = Math.max(newHeight, maxHeight);
        count++;
      });
    });

    let n = 0;
    while (count !== $imgs.length) {
      await sleep(100);
    }

    $carousel.find('.carousel-item').css('height', `${maxHeight}px`);
  }

  carouselResize();
  $(window).on('resize orientationchange', carouselResize);
});
