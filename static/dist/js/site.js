$(document).ready(function () {

    // shrinking header on scroll
    $(document).on('scroll', function() {
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            shrinkOn = 200,
            header = $("header");
        if (distanceY > shrinkOn) {
            header.addClass('smaller');
        } else {
            if (header.hasClass('smaller')) {
                header.removeClass('smaller');
            }
        }
    });

    // swiper
    $(document).ready(function () {
        var slides = $('.swiper-slide').length;

        if (slides > 1) {
            // initialize swiper when document ready - assuming we have more than 1 slide
            var mySwiper = new Swiper('.swiper-container', {
                // Optional parameters
                direction: 'horizontal',
                loop: true,
                pagination: {
                    el: '.swiper-pagination',
                    type: 'bullets',
                    clickable: true,
                },
                autoplay: {
                    delay: 5000,
                }
            });
        }

    });

    // Cookie Policy (cookieconsent.insites.com)
    window.cookieconsent.initialise({
        "palette": {
        "popup": {
            "background": "#252e39"
        },
        "button": {
            "background": "#14a7d0"
        }
        },
        "position": "bottom",
        "content": {
            "message": "This website uses cookies to ensure you get the best experience on our website.",
            "dismiss": "Got it!",
            "link": "Learn More",
            "href": "https://cookiesandyou.com"
        }
    });

});

