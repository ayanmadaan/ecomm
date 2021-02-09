var UpdateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i < UpdateBtns.length; i++){
    UpdateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            UpdateUserOrder(productId, action)
        }
    })
}

function UpdateUserOrder(productId, action){
    console.log('User is authenticated, sending data...')

    var url = '/updateitem/'

    fetch(url, {
        method:'POST',
        headers: {            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })

        .then((response) =>{
            return response.json()
        })

        .then((data) =>{
            console.log('data:', data)
        })
}