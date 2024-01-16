$(document).ready(function() {

    const silderSitetourOutstanding = $('.slider-sitetour-outstanding');

    silderSitetourOutstanding.each(function() {

        $(this).slick({
            dots: false,
            slidesToShow: 2,
            slidesToScroll: 1,
            autoplay: false,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })

    const slider1 = $('.slider1');

    slider1.each(function() {

        $(this).slick({
            dots: false,
            slidesToShow: 3,
            slidesToScroll: 1,
            autoplay: false,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })

    const slider2 = $('.slider2');

    slider2.each(function() {

        $(this).slick({
            dots: false,
            slidesToShow: 3,
            slidesToScroll: 1,
            autoplay: false,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })
})