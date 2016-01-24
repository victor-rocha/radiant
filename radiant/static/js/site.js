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

    //$('.hero-wrapper').on('click', function() {
    //    var $this = $(this),
    //        $video = $this.find('video');
    //    if (!$this.hasClass('fullscreen')) {
    //        $this.toggleClass('fullscreen');
    //        $video.attr('controls', 'controls');
    //        //$video.first().play();
    //    } else {
    //
    //    }
    //});
    //
    //$('.hero-wrapper .close').click(function() {
    //    $('.hero-wrapper').removeClass('fullscreen');
    //    event.preventDefault();
    //    event.stopPropagation();
    //});
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
        $this.text(text == "Show Less" ? "Read More" : "Show Less")
    });


    // animate text on page load
    animateText('.article-inner-wrapper');

    function animateText(elem) {
        var $elem = $(elem);
        options = {
            in: {
                // set the effect name
                effect: 'bounceIn',

                // set the delay factor applied to each consecutive character
                delayScale: 1,

                // set the delay between each character
                delay: 20,

                // set to true to animate all the characters at the same time
                sync: false,

                // randomize the character sequence
                // (note that shuffle doesn't make sense with sync = true)
                shuffle: true,

                // reverse the character sequence
                // (note that reverse doesn't make sense with sync = true)
                reverse: false,

                // callback that executes once the animation has finished
                callback: function () {}
            },

            // out animation settings.
            out: {
                effect: 'bounceOutDown',
                delayScale: 1.5,
                delay: 50,
                sync: false,
                shuffle: false,
                reverse: false,
                callback: function () {}
            }
        };

        $elem.find('p').textillate(options);
        $elem.find('h2').textillate(options);
        $elem.toggleClass('hidden');
    }
})(jQuery);
