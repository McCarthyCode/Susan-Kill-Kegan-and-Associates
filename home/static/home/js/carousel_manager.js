$(document).ready(() => {
  // reorder images
  let $up = $('#imageList .controls :first-child');
  let $down = $('#imageList .controls :last-child');

  $up.click(function () {
    console.log('up');
    let $li = $(this).parents('li');

    if ($li.is(':first-of-type')) {
      console.log('first');
      return;
    }

    let $prev = $li.prev();

    $li.animate({'bottom': `${$prev.outerHeight() + 8}px`}, 500, function () {
      $(this).after($prev.detach()).prop('style', '');
    });

    $prev.animate({'top': `${$li.outerHeight() + 8}px`}, 500, function () {
      $(this).prop('style', '');
    });
  });

  $down.click(function () {
    console.log('down');
    let $li = $(this).parents('li');

    if ($li.is(':last-of-type')) {
      console.log('last');
      return;
    }

    let $next = $li.next();

    $li.animate({'top': `${$next.outerHeight() + 8}px`}, 500, function () {
      $(this).before($next.detach()).prop('style', '');
    });

    $next.animate({'bottom': `${$li.outerHeight() + 8}px`}, 500, function () {
      $(this).prop('style', '');
    });
  });
});
