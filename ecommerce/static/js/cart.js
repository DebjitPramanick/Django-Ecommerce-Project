var updateBtn = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        
        if(user === 'AnonymousUser'){
            console.log("Not logged in")
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}


// Fetching number of items using this function

const updateUserOrder = (id, action) => {
    var url = '/updateitem/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': id, 'action': action})
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)
        location.reload()
    })
}