const box = document.querySelector('.shadow');
let isRMoved = false;
let isLMoved = false;

const moveRight = document.querySelector('.moveRight');
const moveLeft = document.querySelector('.moveLeft');

moveLeft.classList.add("hidden")

let moveCount = 0
moveRight.addEventListener('click', function() {
  if (!isRMoved) {
    if (moveCount == 0){
        if(window.innerWidth < 500){
            box.style.transform = 'translateY(200px)'; // Sağa doğru 200px kaydır
        isRMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
        isLMoved = false
        moveCount +=1
        moveLeft.classList.remove("hidden")
        moveRight.classList.add("hidden")
        box.style.backgroundImage = " linear-gradient(to right, #e8aa40, #e8aa40, #f000a4, #8b12eb)";

      
        }else{
        box.style.transform = 'translateX(200px)'; // Sağa doğru 200px kaydır
        isRMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
        isLMoved = false
        moveCount +=1
        moveLeft.classList.remove("hidden")
        moveRight.classList.add("hidden")
        box.style.backgroundImage = " linear-gradient(to right, #e8aa40, #e8aa40, #f000a4, #8b12eb)";
        }
        
    }else{
        if(window.innerWidth < 500){box.style.transform = 'translateY(200px)'; // Sağa doğru 200px kaydır
        isRMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
        isLMoved = false
        moveLeft.classList.remove("hidden")
        moveRight.classList.add("hidden")
        box.style.backgroundImage = " linear-gradient(to right, #e8aa40, #e8aa40, #f000a4, #8b12eb)";

         }else{
        box.style.transform = 'translateX(200px)'; // Sağa doğru 200px kaydır
        isRMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
        isLMoved = false
        moveLeft.classList.remove("hidden")
        moveRight.classList.add("hidden")
        box.style.backgroundImage = " linear-gradient(to right, #e8aa40, #e8aa40, #f000a4, #8b12eb)";

}

    }
    
}
});
moveLeft.addEventListener('click', function() {
    if (!isLMoved) {
        if (moveCount == 0){
            if(window.innerWidth < 500){
                box.style.transform = 'translateY(-200px)'; // Sağa doğru 200px kaydır
            isLMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
            isRMoved = false
            moveCount +=1
            box.style.backgroundImage="linear-gradient(to right, #6fd007, #b6c65b, #ff9d00, #ff9d00)"

            moveRight.classList.remove("hidden")
            moveLeft.classList.add("hidden")

            }else{
            box.style.transform = 'translateX(-200px)'; // Sağa doğru 200px kaydır
            isLMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
            isRMoved = false
            moveCount +=1
            box.style.backgroundImage="linear-gradient(to right, #6fd007, #b6c65b, #ff9d00, #ff9d00)"
            moveRight.classList.remove("hidden")
            moveLeft.classList.add("hidden")
                    }

          
        }else{
            if(window.innerWidth <500){
                box.style.transform = 'translateY(0px)'; // Sağa doğru 200px kaydır
            isLMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
            isRMoved = false
            moveRight.classList.remove("hidden")
            moveLeft.classList.add("hidden")
            box.style.backgroundImage="linear-gradient(to right, #6fd007, #b6c65b, #ff9d00, #ff9d00)"

            }else{
            box.style.transform = 'translateX(0px)'; // Sağa doğru 200px kaydır
            isLMoved = true; // Kutu hareket ettirildiğinde, bir daha hareket etmemesi için kontrol ekleyin
            isRMoved = false
            box.style.backgroundImage="linear-gradient(to right, #6fd007, #b6c65b, #ff9d00, #ff9d00)"

            moveRight.classList.remove("hidden")
            moveLeft.classList.add("hidden")}

        }
   
    
    }
  });
  function checkScreenWidth() {
    const circleIcon = document.querySelector('.fa-rotate-180');
    const second = document.querySelector(".rounded-full")

    // Ekran genişliği 500px'den küçükse rotate-270 sınıfını ekle
    if (window.innerWidth < 500) {
      circleIcon.classList.add('fa-rotate-270');
      second.classList.add('fa-rotate-90');

    } else {
      // Ekran genişliği 500px veya daha büyükse rotate-270 sınıfını kaldır
      circleIcon.classList.remove('fa-rotate-270');
      second.classList.remove('fa-rotate-90');

    }
  }

  // Sayfa yüklendiğinde ve ekran boyutu değiştiğinde kontrol et
  window.addEventListener('DOMContentLoaded', checkScreenWidth);
  window.addEventListener('resize', checkScreenWidth);


let span = document.getElementById("passwordSpan")
let input = document.getElementById("passwordInput")
const validatePassword=()=>{
    let inputValue = input.value
    
   

    if (inputValue.length == 0){
        span.innerHTML = "" 
    }else if(inputValue.length >= 8){
        span.innerHTML ='<i class="fa-solid fa-circle-check" style="color: #8cdd6e;"></i>'
    }
    else{
        span.innerHTML = "Min 8 chars"
    }
}


  
