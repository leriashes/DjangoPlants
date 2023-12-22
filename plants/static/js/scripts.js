function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: (xhr, settings) => {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
})


function add_to_fav() {
    $('.add-to-fav').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault();

            const type = $(el).data('type')
            const id = $(el).data('id')

            if ($(el).hasClass('added-to-fav')) {
                $.ajax({
                    url: '/favourites/add/',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        type: type,
                        id: id,
                    },
                    success: (data) => {
                        $(el).removeClass('added-to-fav')
                        let ele = document.getElementById(id)
                        ele.innerHTML = '<i class="bi bi-heart fav"></i>';

                        $('#fav-filter').load("rastlist");
                    },
                })
            } else {
                $.ajax({
                    url: '/favourites/add/',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        type: type,
                        id: id,
                    },
                    success: (data) => {
                        $(el).addClass('added-to-fav')
                        let ele = document.getElementById(id)
                        ele.innerHTML = '<i class="bi bi-heart-fill fav"></i>';
                    },
                })
            }
        })
    })
}

$(document).ready(function(){
    console.log('my message');
    add_to_fav();
})