$(document).ready(function() {

    const carouselVideoReview = $('.carousel-review-news');
    carouselVideoReview.each(function() {

        $(this).slick({
            dots: false,
            slidesToShow: 4,
            slidesToScroll: 2,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })
})