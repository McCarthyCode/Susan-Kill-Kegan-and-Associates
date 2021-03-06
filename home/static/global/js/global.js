const sleep = (milliseconds) => {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
};

$(document).ready(() => {
  const breakpointMd = 768;

  console.log('This site brought to you by McCarthy Code.');
  console.log('https://mccarthycode.com/');

  // external link icon
  $('a.external-link').after(
    '<span class="user-select-none"> <i class="fas fa-external-link-alt" title="External Link"></i></span>',
  );

  // resize title
  async function resizeTitle() {
    const $container = $('#title .container');
    let height = $container.outerHeight();

    while (height < 100) {
      await sleep(50);
      height = $container.outerHeight();
    }

    $('#grid').css({
      'grid-template-rows': `[top] ${height}px [title-bottom] auto [bottom]`,
    });
  }

  // resize content
  function resizeContent() {
    const viewportHeight = $(window).outerHeight();
    const titleHeight = $('#title').outerHeight();
    const navbarHeight = $('#navbar').outerHeight();
    const carouselHeight = $('#carousel').outerHeight();
    const footerHeight = $('#footer').outerHeight();

    const height =
      viewportHeight -
      titleHeight -
      navbarHeight -
      (carouselHeight === undefined ? 0 : carouselHeight) -
      footerHeight;

    $('#content .container').css({
      'min-height': `${height}px`,
    });
  }

  // combine resized title and content
  function resize() {
    resizeTitle();
    resizeContent();
  }

  resize();
  $(window).on('resize orientationchange', resize);

  // navbar menu
  $('#navbarMenuButton').click(() => {
    $('#navbarCollapse').slideToggle();
  });
  $(window).on('resize orientationchange', () => {
    if ($(this).width() >= breakpointMd) {
      $('#navbarCollapse').css('display', 'inline');
    } else {
      $('#navbarCollapse').hide();
    }
  });
});
