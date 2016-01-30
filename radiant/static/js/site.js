/* global jQuery */
// Avoid `console` errors in browsers that lack a console.
(function () {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

// Place any jQuery/helper plugins in here.
(function ($) {

    // CSRF helper functions taken directly from Django docs
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/i.test(method));
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Setup jQuery ajax calls to handle CSRF
    $.ajaxPrefilter(function (settings, originalOptions, xhr) {
        var csrftoken;
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    });

    $("body").floatingSocialShare({
        buttons: ["facebook", "twitter", "envelope"],
        title: $('meta[property="og:title"]').attr("content"), // your title, default is current page's title
        url: $('meta[property="og:url"]').attr("content"),  // your url, default is current page's url
        text: "share with ", // the title of a tags
        description: $('meta[property="og:description"]').attr("content"), // your description, default is current page's description
        media: $('meta[property="og:image"]').attr("content") // pinterest media
    });

    $('.collapser a').click(function() {
        var $this = $(this),
            text = $this.text();
        $this.text(text == "Show Less" ? "Read More" : "Show Less");
        $('.hidden-episodes').toggleClass('hidden');
    });

    new WOW().init();

    var $el, $ps, $p, $up, $targetElement, totalHeight, targetSelector;

    $(".toggle-btn-wrapper .button").click(function() {
        totalHeight = 0;
        $up = $(".sidebar-box");

        $el = $(this);
        targetSelector = $el.attr('data-toggle');
        $targetElement = $(targetSelector);
        $p  = $el.parent();
        $ps = $up.find("p:not('.read-more')");
        // measure how tall inside should be by adding together heights of all inside paragraphs (except read-more paragraph)
        $ps.each(function() {
            totalHeight += $(this).outerHeight();
        });

        $up
            .css({
              // Set height to prevent instant jumpdown when max height is removed
              "height": $up.height(),
              "max-height": 9999
            })
            .animate({
              "height": totalHeight
            });
        $targetElement.removeClass('hidden');
        $targetElement
            .css({
              // Set height to prevent instant jumpdown when max height is removed
              "height": $up.height(),
              "max-height": 9999
            })
            .animate({
              "height": totalHeight - $up.height()
            });

        // fade out read-more
        $p.remove();
        $(".read-more").remove();

        // prevent jump-down
        return false;

    });
})(jQuery);
