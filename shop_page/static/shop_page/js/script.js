const list_button = document.querySelectorAll(".product_button");
const basketCount = document.querySelector("#basket-count");
const list_rbuttons = document.querySelectorAll(".readmore")
const list_description = document.querySelectorAll(".read-more")

function updateBasketCount() {
    let count = document.cookie.split("=")[1].split(" ").length;
    basketCount.textContent = count
    basketCount.style.display = "flex"

}

for (let i = 0; i < list_button.length; i++){
    let button = list_button[i];
    button.addEventListener("click", function() {
        if (document.cookie != ""){
            let products = document.cookie.split("=")[1]
            // if (!products.includes(button.id)){
            document.cookie = `products = ${products} ${button.id}; Path = /`
            // }
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
        // let text = document.querySelector(`.read-more#${button.id}`)//.querySelector(`#${button.id}`)
        // console.log(text)
        
    })
}
document.body.style.overflowX = "hidden";