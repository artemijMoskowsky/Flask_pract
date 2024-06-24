const list_button = document.querySelectorAll(".product_button");
const basketCount = document.querySelector("#basket-count");
const list_rbuttons = document.querySelectorAll(".readmore")
const list_description = document.querySelectorAll(".read-more")
const productList = document.querySelectorAll("#p_object")
const dataReader = document.querySelector(".dataReader")

function updateBasketCount() {
    let cookies = document.cookie.split("=")[1].split(" ");
    let count = 0
    let validID = dataReader.getAttribute("data-products_ids").slice(1, -1).replace(/,/g, "").split(" ")


    for(let i = 0; i < cookies.length; i++){
        if( validID.includes(cookies[i])){
            count += 1
        }
    }
    basketCount.textContent = count
    if (count > 0){
        basketCount.style.display = "flex"
    } else {
        basketCount.style.display = "none"
    }

}

for (let i = 0; i < list_button.length; i++){
    let button = list_button[i];
    button.addEventListener("click", function() {
        if (document.cookie != ""){
            let products = document.cookie.split("=")[1]
            document.cookie = `products = ${products} ${button.id}; Path = /`
        }
        else{
            document.cookie = `products = ${button.id}; Path = /`
        }
        updateBasketCount()
        
    })
}

if (document.cookie == ""){
    basketCount.style.display = "None"
} else {
    updateBasketCount()
}

for (let i = 0; i < list_rbuttons.length; i++) {
    let button = list_rbuttons[i];
    button.addEventListener("click", function(){
        for (let j = 0; j < list_description.length; j++){
            let text = list_description[j]
            if (text.id == button.id){
                if (button.textContent == "Читати далі"){
                    text.style.overflow = "visible"
                    text.style.textOverflow = "clip"
                    text.style.whiteSpace = "normal"
                    button.textContent = "Згорнути"
                }
                else{
                    text.style.overflow = "hidden"
                    text.style.textOverflow = "ellipsis"
                    text.style.whiteSpace = "nowrap"
                    button.textContent = "Читати далі"
                }
            }  
        }
    })
}
document.body.style.overflowX = "hidden";