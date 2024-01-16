$(document).ready(function() {
    $('.carousel').slick(); // Khởi tạo carousel

    // Hiển thị carousel sau khi đã được khởi tạo
    $('.carousel').show();

    $('.slider3').slick(

        {
            dots: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 7 * 1000,
            mobileFirst: true,
            arrows: false
        }
    )
});

function showSlide(index) {
    $('.carousel').slick('slickGoTo', index); // Di chuyển đến slide tương ứng
}