$(document).ready(function() {

    var carouselBanner = $('.container-banner');
    carouselBanner.each(function() {

        $(this).slick({
            dots: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: true
        })
    })
})