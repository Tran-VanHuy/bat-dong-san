$(document).ready(function(){
    $('.carousel').slick(); // Khởi tạo carousel

    // Hiển thị carousel sau khi đã được khởi tạo
    $('.carousel').show();
  });

  function showSlide(index) {
    $('.carousel').slick('slickGoTo', index); // Di chuyển đến slide tương ứng
  }