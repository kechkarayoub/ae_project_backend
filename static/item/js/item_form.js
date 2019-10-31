(function($) {
    setTimeout(function(){
        $("#images-group").on('change', '.field-image input[type=file]', function(event){
            var self = this;
            var files = event.target.files;
            for (var i = 0, f; f = files[i]; i++){
                if (!f.type.match('image.*')){
                    continue;
                }
                var reader = new FileReader();
                reader.onload = (function(){
                    return function(e){
                        var img = $(self).closest(".inline-related").find('.field-get_item_images_preview img');
                        if(img.length){
                            $(img).attr("src", e.target.result);
                        }
                        else{
                            $(self).closest(".field-image").prepend(
                                "<img src='" + e.target.result + "' width='150' height='150' style='object-fit: cover;'/>"
                            );
                        }

                    };
                })(f);
                reader.readAsDataURL(f);
            }
        });
        $(document).ready(function() {
        $("select").select2();
        });
    }, 2000);
})(django.jQuery);