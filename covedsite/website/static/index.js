

$("document").ready(function(){

    window.addEventListener('scroll',function(){
        const nav = document.getElementById('navContainerx');
        var elements;
        if(window.pageYOffset>10){
          nav.classList.add("addShadowx");
          nav.style.backgroundColor="#ffffff";
          nav.style.color = "#000000"
          elements = document.getElementsByClassName("s");
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.backgroundColor="#000000";
                }
          

        }else{
          nav.classList.remove("addShadowx");
          nav.style.backgroundColor="#002244"
          nav.style.color = "#ffffff";
          elements = document.getElementsByClassName("s");
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.backgroundColor="#ffffff";
                }
        }
      });

    if (window.location.hash != null && window.location.hash != ''){
        scrollToElem(window.location.hash);
    }
     
    

    $("#covedNAV").on('click', function(){
        var duration = getDuration(0);
        $("HTML, BODY").animate({
            scrollTop: 0
        }, duration);
    });

    $("#covedIMG").on('click', function(){
            var duration = getDuration(0);
            $("HTML, BODY").animate({
                scrollTop: 0
            }, duration);
        });

    $('#aboutusLink').on('click', function(){
        scrollToElem('#aboutus');
    });

    $('#signupLink').on('click', function(){
        scrollToElem('#signup');
    });

    $('#contactusLink').on('click', function(){
        scrollToElem('#contactus');
    });

    $('#faqLink').on('click', function(){
        scrollToElem('#faq');
    });


    $("#enrolbtn").on('click', function(){
        window.location = "studentSignUp.html";
    });

    $("#joinusbtn").on('click', function(){
        window.location = "mentorSignUp.html";
    });

    $('#studenttpbtn').on('click', function(){
        scrollToElem('#studentsignup');
    });

    $('#mentortpbtn').on('click', function(){
        scrollToElem('#mentorsignup');
    });


    var sideopen = false;
    $('#nav-icon3').click(function(){
    $(this).toggleClass('open');
    if(sideopen){
        closeNav();
    } else{
        document.getElementById("sidenavx").style.width = "250px";
        sideopen = true;
    }
    
    });

    $('#aboutusLinkS').on('click', function(){
        $('#nav-icon3').toggleClass('open');
        closeNav();
        scrollToElem('#aboutus')
    });

    $('#studentsLinkS').on('click', function(){
        $('#nav-icon3').toggleClass('open');
        closeNav();
        scrollToElem('#studentsignup')
    });

    $('#mentorsLinkS').on('click', function(){
        $('#nav-icon3').toggleClass('open');
        closeNav();
        scrollToElem('#mentorsignup')
    });

    $('#contactusLinkS').on('click', function(){
        $('#nav-icon3').toggleClass('open');
        closeNav();
        scrollToElem('#contactus')
    });

    $('#faqLinkS').on('click', function(){
        $('#nav-icon3').toggleClass('open');
        closeNav();
        scrollToElem('#faq')
    });

    $('#resourcesLinkS').on('click', function(){
        window.location="resources.html"
    });

    $('#resourcesLink').on('click', function(){
        window.location="resources.html"
    });

    $('#teamLinkS').on('click', function(){
        window.location="aboutUs.html"
    });

    $('#teamLink').on('click', function(){
        window.location="aboutUs.html"
    });

    /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
    function closeNav() {
        sideopen = false;
        document.getElementById("sidenavx").style.width = "0";
    }


    $('#finsta').on('click', function(){
        window.location = "https://www.instagram.com/covedindia/?igshid=byec8gpb97es";
    }); 

    $('#ffb').on('click', function(){
        window.location = "https://www.facebook.com/CovEd-India-105360627792093/";
    }); 

    $('#fmail').on('click', function(){
        window.location = "mailto:covedindia@gmail.com";
    }); 

});

function scrollToElem(element){
var position = $(element).offset().top;
var duration = getDuration(position);
$("HTML, BODY").animate({
    scrollTop: (position-60)
}, duration);
}

function getDuration(target) {
var currentTop = $(window).scrollTop(), rate = 0.5, distance;
distance = Math.abs(currentTop - target);
return distance * rate;
}
