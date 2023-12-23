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
                        $('#fav-filter').load("rastlist", {'semeystvos' : data.semeystvos, 'gruppis' : data.gruppis, 'fav' : data.fav, 'day' : data.day});
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

function search_rast() {
    $('.searchbtn').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault();
    var els = document.getElementById("sem");
    var elg = document.getElementById("grup");


    if (els != null)
    {
        if (document.getElementById("fav-filter") != null)
            url = 'favourites';
        else
            url = 'all';
        console.log(url)
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: {
            semeystvos: els.value,
            gruppis: elg.value,
            fav: false, day: false
        },
        success: (data) => {
            console.log(data)
            $('#fav-filter').load("rastlist", {'semeystvos' : data.semeystvos, 'gruppis' : data.gruppis, 'fav' : data.fav, 'day' : data.day});
            $('#f-filter').load("rastlist", {'semeystvos' : data.semeystvos, 'gruppis' : data.gruppis, 'fav' : data.fav, 'day' : data.day});
        },
    })
    }
        })
    })
}

$(document).ready(function(){
    add_to_fav();
    search_rast();
})