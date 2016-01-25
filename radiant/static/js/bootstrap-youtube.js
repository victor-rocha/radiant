// REQUIRED: Include "jQuery Query Parser" plugin here or before this point:
// 	     https://github.com/mattsnider/jquery-plugin-query-parser

$(document).ready(function () {
// BOOTSTRAP 3.0 - Open YouTube Video Dynamicaly in Modal Window
// Modal Window for dynamically opening videos
    $('.video-wrapper, .play').on('click', function (e) {
        // Store the query string variables and values
        // Uses "jQuery Query Parser" plugin, to allow for various URL formats (could have extra parameters)
        var queryString = $(this).attr('data-href').slice($(this).attr('data-href').indexOf('?') + 1);
        var queryVars = $.parseQuery(queryString);

        // if GET variable "v" exists. This is the Youtube Video ID
        if ('v' in queryVars) {
            // Prevent opening of external page
            e.preventDefault();

            // Variables for iFrame code. Width and height from data attributes, else use default.
            var vidWidth = 560; // default
            var vidHeight = 315; // default
            if ($(this).attr('data-width')) {
                vidWidth = parseInt($(this).attr('data-width'));
            }
            if ($(this).attr('data-height')) {
                vidHeight = parseInt($(this).attr('data-height'));
            }
            var iFrameCode = '<iframe width="' + vidWidth + '" height="' + vidHeight + '" scrolling="no" allowtransparency="true" allowfullscreen="true" src="https://www.youtube.com/embed/' + queryVars['v'] + '?rel=0&wmode=transparent&showinfo=1&autoplay=1" frameborder="0"></iframe>';

            // Replace Modal HTML with iFrame Embed
            $('#youtube-wrapper .iframe-wrapper').html(iFrameCode);
            // Open Modal
            $('#youtube-wrapper').addClass('fullscreen');
        }
    });
    $('.close').click(function() {
        $('#youtube-wrapper').removeClass('fullscreen');
        $('#youtube-wrapper .iframe-wrapper').html('');
    });
});
