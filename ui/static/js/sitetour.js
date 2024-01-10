$(document).ready(function() {

    const silderSitetourOutstanding = $('.slider-sitetour-outstanding');

    silderSitetourOutstanding.each(function() {

        $(this).slick({
            dots: false,
            slidesToShow: 2,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })
})