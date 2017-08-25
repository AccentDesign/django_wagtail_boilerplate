$(document).ready(function () {

    // shrinking header on scroll
    $(document).on('scroll', function() {
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            shrinkOn = 300,
            header = $("header");
        if (distanceY > shrinkOn) {
            header.addClass('smaller');
        } else {
            if (header.hasClass('smaller')) {
                header.removeClass('smaller');
            }
        }
    });

    // owl carousel
    var owlLength = $('.owl-carousel').children().length;

    $('.owl-carousel').owlCarousel({
        loop: owlLength > 1,
        mouseDrag: owlLength > 1,
		touchDrag: owlLength > 1,
		pullDrag: owlLength > 1,
        margin: 10,
        nav: false,
        responsive: {
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
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
            "href": "http://link-to-your-policy-page.com/"
        }
    });

});

