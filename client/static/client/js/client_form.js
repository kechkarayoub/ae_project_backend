(function($) {
    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i = 0; i <ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
//    $.ajaxSetup({
//        headers: {
//            'X-CSRF-Token': getCookie("csrftoken")
//        }
//    });
    setTimeout(function(){
        var $ = $ || django.jQuery;
        $('.btn-import').on('click', function(event){
            var self = this;
            $(this).closest("li").find("input.import_input").click();
        });
        $("li").on('change', 'input.import_input[type=file]', function(event){
            var self = this;
            var files = event.target.files;
            if(files.length == 0){
                return;
            }
            var formdata = new FormData();
            formdata.append("file", files[0]);
            $.ajax({
                url: "/en/api/client/import",
                type: "POST",
                method : "POST",
                enctype: 'multipart/form-data',
                data: formdata,
                processData: false,
                contentType: false,
                success: function (result) {
                     if(result.success){
                        alert(result.message);
                     }
                },
                error: function(error) {
                        alert(error);
                }
            });
        });
    }, 500);
})(django.jQuery);