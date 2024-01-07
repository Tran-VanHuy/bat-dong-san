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

    var carouselProjectOutstanding = $('.container-item-projects-outstanding');
    carouselProjectOutstanding.each(function() {

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

    var carouselReviews = $('.slider-reviews');
    carouselReviews.each(function() {

        $(this).slick({
            dots: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })

    var sliderNewsProjects = $('.slider-news-projects');
      sliderNewsProjects.each(function() {

        $(this).slick({
            dots: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        })
    })
})