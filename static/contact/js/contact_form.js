(function($) {
    setTimeout(function(){
        $("#contact_form .submit-row .default").val("Return");
        $("#contact_form .submit-row input[name=_continue]").addClass("hidden");
        $("#contact_form .submit-row .deletelink-box").addClass("hidden");
        $("#contact_form").find("input, textarea").attr("readonly", true);
    }, 0);
})(django.jQuery);