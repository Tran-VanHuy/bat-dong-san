let items = document.querySelectorAll('.carousel .carousel-item')

items.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i = 1; i < minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
            next = items[0]
        }
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})

$(document).ready(function() {
    var myCarousel = $(".slider-partner");
    myCarousel.each(function() {
        $(this).slick({
            dots: false,
            slidesToShow: lengthPartner >= 6 ? 6 : lengthPartner,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        });
    });
});