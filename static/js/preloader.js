(function ($) {
  "use strict";

  /*============= preloader js css =============*/
  var cites = [];
  cites[0] =
    "We design and develope optimizing website rich in page views & engagement";
  cites[1] = "Crafting Seamless Digital Experiences.";
  cites[2] = "A web developer with a passion for creating immersive digital experiences.";

  var cite = cites[Math.floor(Math.random() * cites.length)];
  $("#preloader p").text(cite);
  $("#preloader").addClass("loading");

  $(window).on("load", function () {
    setTimeout(function () {
      $("#preloader").fadeOut(500, function () {
        $("#preloader").removeClass("loading");
      });
    }, 500);
  });
})(jQuery);
