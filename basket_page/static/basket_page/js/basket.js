const plus_buttons = document.querySelectorAll(".cart_buttons_p")
const minus_buttons = document.querySelectorAll(".cart_buttons_m")
const counters = document.querySelectorAll(".counter")
const price_list = document.querySelectorAll(".price") 
const price_sum_tag_h = document.querySelector("#p_priceT")
const list_p_content = document.querySelectorAll(".p_content")
const discount_tag_h = document.querySelector("#p_discountT")
const sum_tag_h = document.querySelector("#p_sumT")
const span_count = document.querySelector("#p_countT")
const basketCount2 = document.querySelector("#basket-count");

function updateBasketCount() {
    let count = document.cookie.split("=")[1].split(" ").length;
    basketCount2.textContent = count
    basketCount2.style.display = "flex"

}

// for(let id = 0; id < counters.length; id++){
//     let counter = counters[id]
//     let value = localStorage.getItem(plus_buttons[id].id)
//     if (value != null){
//         counter.textContent = value
//     }
// }

for(let id = 0; id < plus_buttons.length; id++){
    let button = plus_buttons[id]
    let counter = counters[id]
    button.addEventListener("click", function(){
        counter.textContent = parseInt(counter.textContent) + 1
        let cookie = document.cookie.split("=")[1]
        document.cookie = `products = ${cookie} ${button.id}`
        setPriceSum()
        setDiscount()
        setPrice()
        updateBasketCount()
    })
}

for(let id = 0; id < minus_buttons.length; id++ ){
    let button = minus_buttons[id]
    let counter = counters[id]
    button.addEventListener("click", function(){
        if(counter.textContent != "1"){
            //console.log(counter.textContent)
            counter.textContent = parseInt(counter.textContent) - 1
            let cookie = document.cookie.split("=")[1].split(" ")
            for (let i = 0; i < cookie.length; i ++){
                if (cookie[i] == button.id){
                    cookie.splice(i, 1)
                    break
                }
            }
            document.cookie = `products = ${cookie.join(" ")}`
            setPriceSum()
            setDiscount()
            setPrice()
            updateBasketCount()
        }
    })
}

function setPriceSum() {
    let price_sum = 0
    let counts = 0    
    for(let sum = 0; sum < price_list.length; sum++ ){
        let price = price_list[sum].textContent.split(" ")[0]
        let count = parseInt(counters[sum].textContent)
        counts += count
        price_sum += parseInt(price) * count

    }
    span_count.textContent = counts
    price_sum_tag_h.textContent = price_sum  + " грн"
}
setPriceSum()

function setDiscount(){
    let discount = 0
    for(let dis = 0; dis < price_list.length; dis++ ){
        let price = price_list[dis].textContent.split(" ")[0]
        let count = parseInt(counters[dis].textContent)
        let discount_percent = parseInt(list_p_content[dis].id)
        discount += parseInt(parseInt(price) / 100 * discount_percent * count)

    }
    discount_tag_h.textContent = discount + " грн"
}
setDiscount()

function setPrice(){
    sum_tag_h.textContent = parseInt(price_sum_tag_h.textContent.split(" ")[0]) - parseInt(discount_tag_h.textContent.split(" ")[0]) + " грн"
}
setPrice()