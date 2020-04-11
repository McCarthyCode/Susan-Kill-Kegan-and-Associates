$(document).ready(() => {
  // reorder images
  let $up = $('.image-list .controls :first-child');
  let $down = $('.image-list .controls :last-child');

  $up.click(function () {
    let $li = $(this).parents('li');

    if (!$li.is(':first-of-type')) {
      let $prev = $li.prev();

      $li.animate({'bottom': `${$prev.outerHeight() + 8}px`}, 500, function () {
        $(this).after($prev.detach()).prop('style', '');
      });

      $prev.animate({'top': `${$li.outerHeight() + 8}px`}, 500, function () {
        $(this).prop('style', '');
      });
    }
  });

  $down.click(function () {
    let $li = $(this).parents('li');

    if (!$li.is(':last-of-type')) {
      let $next = $li.next();

      $li.animate({'top': `${$next.outerHeight() + 8}px`}, 500, function () {
        $(this).before($next.detach()).prop('style', '');
      });

      $next.animate({'bottom': `${$li.outerHeight() + 8}px`}, 500, function () {
        $(this).prop('style', '');
      });
    }
  });

  // submit changes
  $('#submit').click(function () {
    let order = [];

    $('.image-list li').each(function () {
      order.push($(this).data('id'));
    });

    $.ajax('/carousel/reorder/', {
      'data': {'order': JSON.stringify(order)},
      'success': function (data) {
        window.location.reload(false);
      },
      'error': function (data) {
        window.location.reload(false);
      },
    });
  });
});
