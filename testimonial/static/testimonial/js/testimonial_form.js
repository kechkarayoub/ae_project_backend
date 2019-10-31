(function($) {
    setTimeout(function(){
        $("#testimonial_form .submit-row .default").val("Return");
        $("#testimonial_form .submit-row input[name=_continue]").addClass("hidden");
        $("#testimonial_form .submit-row .deletelink-box").addClass("hidden");
        $("#testimonial_form").find("input, textarea").attr("readonly", true);
    }, 0);
})(django.jQuery);