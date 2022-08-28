

//popular doctors_index_page
function owlComments() {
    jQuery('#owl-Comments').owlCarousel({
        rtl: true,
        loop: true,
        nav: true,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 4000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 1,
            },
            768: {
                items: 2,
            },
            //600: {
            //    items: 5,
            //},
            //700: {
            //    items: 6,
            //},
            //847: {
            //    items: 7,
            //},
            //992: {
            //    items: 5,
            //},
            1200: {
                items: 4
            }
              , 1367: {
                  items: 5,
              }
        }
    });
}


//popular doctors_index_page
function owltopblog() {
    jQuery('#owl-topblog').owlCarousel({
        rtl: true,
        center: true,
        loop: true,
        nav: true,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 4000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 1,
            },
            768: {
                items: 2,
            },
            //600: {
            //    items: 5,
            //},
            //700: {
            //    items: 6,
            //},
            //847: {
            //    items: 7,
            //},
            //992: {
            //    items: 5,
            //},
            1200: {
                items: 2
            }
              , 1367: {
                  items: 3,
              }
        }
    });
}



function owlsecondevent() {
    jQuery('#owl-secondevent').owlCarousel({
        rtl: true,
        //center: true,
        loop: true,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout:5000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 2,
            },
            768: {
                items: 3,
            },
            //600: {
            //    items: 5,
            //},
            //700: {
            //    items: 6,
            //},
            //847: {
            //    items: 7,
            //},
            //992: {
            //    items: 5,
            //},
            1200: {
                items: 4
            }
              , 1367: {
                  items:5,
              }
        }
    });
}






//popular doctors_index_page
function owltoparticle() {
    jQuery('#owl-toparticle').owlCarousel({
        rtl: true,
        loop: true,
        nav: true,
        autoplay: true,
        smartSpeed: 2000,
        autoplayTimeout: 6000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 1,
            },
            768: {
                items: 2,
            },
            //600: {
            //    items: 5,
            //},
            //700: {
            //    items: 6,
            //},
            //847: {
            //    items: 7,
            //},
            //992: {
            //    items: 5,
            //},
            1200: {
                items: 4
            }
              , 1367: {
                  items: 4,
              }
        }
    });
}


//popular doctors_index_page
function owltopnevis() {
    jQuery('#owl-topnevis').owlCarousel({
        rtl: true,
        loop: true,
        nav: true,
        autoplay: false,
        smartSpeed: 2000,
        autoplayTimeout: 6000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 2,
            },
            768: {
                items: 3,
            },
            //600: {
            //    items: 5,
            //},
            //700: {
            //    items: 6,
            //},
            //847: {
            //    items: 7,
            //},
            //992: {
            //    items: 5,
            //},
            1200: {
                items: 5
            }
              , 1367: {
                  items: 5,
              }
        }
    });
}

//popular doctors_index_page
function owltoppost() {
    jQuery('#owl-toppost').owlCarousel({
        rtl: true,
        center: true,
        loop: true,
        nav: true,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 4000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 1,
            },
            768: {
                items: 2,
            },
            //600: {
            //    items: 5,
            //},
            //700: {
            //    items: 6,
            //},
            //847: {
            //    items: 7,
            //},
            //992: {
            //    items: 5,
            //},
            1200: {
                items: 3
            }
              , 1367: {
                  items: 3,
              }
        }
    });
}

function owlslider() {
    jQuery('#owl-slider').owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        nav: true,
        autoplayTimeout: 3000,
        animateOut: 'fadeOut',
    });
}


/*************************
All function are called here 
*************************/
$(document).ready(function () {

    owltopblog(),
    owlsecondevent(),
    owltopnevis(),
    owltoparticle(),
    owltoppost(),
    owlslider(),
    owlComments();

});


