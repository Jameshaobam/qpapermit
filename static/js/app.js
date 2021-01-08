const navbar_small = document.querySelector('.nav-small');
const menu_btn = document.querySelector('.menu');
const close_btn = document.querySelector('.close h5');


navbar_small.style.right = '-1000px';

menu_btn.addEventListener('click',() => {
  
    if (navbar_small.style.right == '0px'){
        navbar_small.style.right = '-1000px';
    }
    else if(navbar_small.style.right != '0px'){
        navbar_small.style.right = '0px';
    }
  
    console.log('Working');


});

close_btn.addEventListener('click',() => {
    const msg = document.querySelector('.messages');
    msg.style.display = 'none';
    console.log('working')
});
