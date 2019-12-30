let usr_inp = document.querySelector('#usr_inp')
let itm_add = document.querySelector('#itm_add')
let usr_lst = document.querySelector('#usr_lst')
let itm_cmp = document.querySelector('#itm_cmp')

itm_add.onclick = function() {
  let inp = usr_inp.value;

  usr_inp.value = '';

  let li = document.createElement('li');
  li.classList.add('usr_itm');

  let inp_div = document.createElement('div');
  inp_div.innerHTML = inp;
  
  let cmp_btn = document.createElement('button');
    
    cmp_btn.innerHTML = '&#x2615;';
  
    cmp_btn.onclick = function() {
        usr_lst.removeChild(this.parentElement);
        let li = document.createElement('li');
        li.innerText = inp;
        cmp_lst.appendChild(li);
    };
  
  let rm_btn = document.createElement('button');
 
     rm_btn.innerHTML = '&#x2620;';
     
     rm_btn.onclick = function() {
       usr_lst.removeChild(this.parentElement);
    };
  
  li.appendChild(inp_div);
  li.appendChild(cmp_btn);
  li.appendChild(rm_btn);
  
  usr_lst.appendChild(li);
}