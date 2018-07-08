window.onload = function () {
    $('.basket').on('click','input[type=number]', function (event) {
        var input = event.target;

        $.ajax({
            url:'/basket/edit/'+input.name + '/'+ input.value + '/',
            succes: function(data){
                $('.basket').html(data.result)
            }
                });
        event.preventDefault();

    })
};