(function($) {
    setTimeout(function(){
        $("#contactbuy_form .submit-row .default").val("Return");
        $("#contactbuy_form .submit-row input[name=_continue]").addClass("hidden");
        $("#contactbuy_form .submit-row .deletelink-box").addClass("hidden");
        $("#contactbuy_form").find("input, textarea").attr("readonly", true);
    }, 0);
})(django.jQuery);