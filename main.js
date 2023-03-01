let modals = ()=>{
    let number_text = document.querySelectorAll('#nums');
    let titles = document.querySelectorAll('#title');
    let modal1 = document.getElementById('maodals');
    modal1.style.display = "flex";
    a = [];
    for(let i=0; i<number_text.length; i++){
     a.push(number_text[i].textContent);
     let number1 = document.querySelectorAll('#numbers');
     number1[i].innerHTML = a[i];
     if (a[i] == 0){
      titles[i].style.display = "none";
     } else {
      titles[i].style.display = "table-row";
     }
    }
 }

  let product = document.querySelectorAll('#product');
  let product_price = document.querySelectorAll('#product_price');
  let numbers = document.querySelectorAll('#nums');  
  let per = document.querySelectorAll('#per');
  let price = document.querySelectorAll('#price');// querySelectorAll은 배열로 반환 이걸로 해야전체를 찾을수 있다 ㅠㅠ
  
  price = Array.from(price);

  let point = document.querySelectorAll('#point');
  let result_price = document.querySelector('#result_price');
  let total_point = document.querySelector('#total_point');
  let total_price = document.querySelector('#total_price');
  let result_count = document.querySelector('#result_count');
  let buttons = document.querySelectorAll('#btn')
  
console.log(buttons);
console.log(buttons[0]);
console.log(buttons[1]);

  product_price = Array.from(product_price);
  //console.log("Array를 변경하면 "+ product_price);
  
   // 화살표 함수표현식은 function calc(){} ->  const calc = () =>{} 와 같이 사용할 수 있다.

   const calc = () => {
    let sum_price = 0;
    let sum_point = 0;
    let count = 0;
    
    product_price.forEach((contents, index) => {
      let b = price[index].textContent;
      b = b.replace(/,/g, '');
      b = parseInt(b);
      let n = parseInt(product[index].querySelector('#nums').textContent);
      let p = parseInt(point[index].textContent);
      sum_price += b * n;
      sum_point += p * n;
      count += n;

    });
    total_price.innerHTML = sum_price.toLocaleString() + '원';
    total_point.innerHTML = sum_point.toLocaleString() + 'P';
    result_count.innerHTML = count.toLocaleString() + '개';
    buttons[0].style.display = "flex";
    buttons[1].style.display = "flex";


  // 포인트 당 가격 계산
  let avg_price_per_point = sum_price / sum_point;
  avg_price_per_point = avg_price_per_point.toFixed(0);
  avg_price_per_point = avg_price_per_point.toLocaleString();

  // 포인트 당 가격 출력
  let price_per_point = document.querySelector('#price_per_point');
  price_per_point.innerHTML = avg_price_per_point + '원/P';    
  }
  

  
  //for문 시작
  for (let i = 0; i <73; i++) {

      // "+" 버튼 생성
      let addButton = document.createElement('button');
      addButton.textContent = '+';
      addButton.id = 'btn1';
      addButton.className = 'btn btn-primary btn-sm';
      product[i].appendChild(addButton);

      // 숫자 텍스트 생성
      //let numberText = document.createTextNode(0);
      let nums = document.createElement('h6');
      nums.textContent = 0;
      nums.id = 'nums';
      product[i].appendChild(nums);
      
      
      // "-" 버튼 생성
      let minusButton = document.createElement('button');
      minusButton.textContent = '-';
      minusButton.id = 'btn1';
      minusButton.className = 'btn btn-danger btn-sm';      
      product[i].appendChild(minusButton);

      // "+" 버튼에 이벤트 리스너 추가
      addButton.addEventListener('click', function() {
        let number = parseInt(nums.textContent);
        number++;
        nums.textContent = number;
        calc();
      });

      // "-" 버튼에 이벤트 리스너 추가
      minusButton.addEventListener('click', function() {
        let number = parseInt(nums.textContent);
        number--;
        nums.textContent = number;
        calc();
      });

      let price_value = price[i].textContent;
      price_value = price_value.replace(/,/g, ''); // 콤마 제거
      price_value = parseInt(price_value); // 문자열을 숫자로 변환

      let point_value = point[i].textContent;
      point_value = point_value.replace(/point/g, ''); // point 제거
      point_value = parseInt(point_value); // 문자열을 숫자로 변환

      let point_per = price_value/point_value;
      //소수점 0자리까지 표시
      point_per = point_per.toFixed(0);
      per[i].innerHTML = point_value ==0 ? "포인트없음" : point_per.toLocaleString() + '원/P';

  
      // 가격과 숫자를 곱한 값을 보여주는 부분
      document.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON') {
          let priceV = price[i].textContent;
          priceV = priceV.replace(/,/g, ''); // 콤마 제거
          priceV = parseInt(priceV); // 문자열을 숫자로 변환

          let priceP = point[i].textContent;
          priceP = priceP.replace(/point/g, ''); // point 제거
          priceP = parseInt(priceP); // 문자열을 숫자로 변환

          let number = nums.textContent;
          number = parseInt(number);
          let result_price = priceV * number;
          let result_point = priceP * number;
          
          product_price[i].innerHTML = result_price.toLocaleString() + '원 / '+ result_point + 'P';
          //product_price[i].innerHTML = result_price.toLocaleString() + '원 / '+ result_point + 'P';
         
        }
      });
    }
    //for문 끝

