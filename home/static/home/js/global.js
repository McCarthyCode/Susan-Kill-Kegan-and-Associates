$(document).ready(() => {
  const breakpointMd = 768;

  console.log('This site brought to you by McCarthy Web Design.');
  console.log('https://mccarthywebdesign.com/');

  // external link icon
  $('a.external-link')
    .after(' <i class="fas fa-external-link-alt" title="External Link"></i>');

  // resize title
  let $container = $('#title .container');
  let $grid = $('#grid');

  function resizeTitle() {
    let height = $container.outerHeight() + 16 * 2;

    $grid.css({
      'grid-template-rows': `[top] ${height}px [title-bottom] 56px [nav-bottom] auto [bottom]`
    });

  }

  resizeTitle();
  setTimeout(resizeTitle, 500); // insurance measure
  $(window).on('resize orientationchange', resizeTitle);

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
