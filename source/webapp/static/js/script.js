async function makeRequest(url, method = 'GET') {
    let headers = {};
    if (method !== 'GET'){
        const csrfToken = await getCookie('csrftoken');
        headers['X-CSRFToken'] = csrfToken;
    }
    let response = await fetch(url, {
        "method": method,
        "headers": headers,
    })
    if (response.ok) {
        return await response.json();
    } else {
        let error = await response.json()
        throw new Error(error.message)
    }
}

async function onClick(event) {
    event.preventDefault();
    let a = event.target;
    let url = a.href;
    let buttonText = a.innerText;
    let method = 'POST';
    if(buttonText === 'Дизлайк'){
        method = 'DELETE';
    }
    let response = await makeRequest(url, method);
    let span = a.parentElement.getElementsByTagName("span")[0];
    span.innerText = response.likes_count;
    a.innerText = buttonText === 'Дизлайк' ? "Лайк" : "Дизлайк"
}

function onLoad() {
    let links = document.querySelectorAll('[data-like="like"]');
    for (let link of links) {
        link.addEventListener("click", onClick);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


window.addEventListener("load", onLoad)
